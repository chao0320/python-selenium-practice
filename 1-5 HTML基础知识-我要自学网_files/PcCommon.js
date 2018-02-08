//类级别
//异步请求封装
$.extend({
    AjaxMethod: function (options) {

        //默认设置
        var defaults = {
            type: "POST",
            url: "",
            data: {},
            dataType: "json",
            error: null,
            errorText: "网络异常,稍后再试",
            beforeSend: null,
            success: null,
            complete: null,
            isShowLoading: true,
            loadingText: "加载中"
        };
        options = $.extend(defaults, options);

        if ($.trim(defaults.url) != "") {

            var layerIndex;//加载层

            var Ajax = $.ajax({
                url: options.url,                                           //请求地址
                type: options.type ? options.type : "POST",                 //请求方式
                data: options.data,                                         //请求数据
                dataType: options.dataType ? options.dataType : "json",     //返回数据类型
                beforeSend: function () {                                   //请求前执行

                    if (options.isShowLoading) {
                        layerIndex = layer.msg(options.loadingText, { icon: 16, shade: 0.01, time: 0 });
                    }

                    if (options.beforeSend) {
                        options.beforeSend();
                    }
                },
                error: function () {                                        //错误回调

                    if (options.isShowLoading) {
                        layer.close(layerIndex);
                    }

                    if (options.error)
                        options.error();
                    else {
                        layer.msg(options.errorText, { shade: 0.01, time: 1500 });
                    }
                },
                success: function (data) {                                  //成功回调

                    if (options.isShowLoading) {
                        layer.close(layerIndex);
                    }

                    if (options.success)
                        options.success(data);
                },
                complete: function () {                                     //结束回调

                    if (options.complete)
                        options.complete();

                }
            });

            return Ajax;
        }
        else {
            console.log("异步请求地址为空");
        }
    }
});


//对象级别
//文件上传
(function ($) {
    $.fn.UpLoadFile = function (options) {

        //默认设置
        var defaults = {
            upLoadUrl: "",                                      //后台上传地址
            extraParams: {},                                    //额外输入参数
            allowAll: true,                                     //允许全部类型文件(默认)
            allowImage: false,                                  //允许图片类型文件
            allowZip: false,                                    //允许压缩类型文件
            allowDocument: false,                               //允许文档类型文件
            allowMedia: false,                                  //允许文档类型文件
            allowRepeat: false,                                 //允许上传文件重复
            isMulti: false,                                     //允许批量上传
            maxZize: 1,                                         //最大允许文件大小(默认1MB)
            error: null,                                        //错误时候触发
            beforeSend: null,                                   //初始化后触发
            beforeOnePicUpLoad: null,                           //在每张图片准备上传前触发
            success: null,                                      //在每张图片上传成功时触发
            complete: null,                                     //在所有图片上传成功时触发
            isShowLoading: true,                                //是否显示加载提示
            loadingText: "上传中,请稍等..."                     //加载提示内容
        };
        options = $.extend(defaults, options);

        //参数验证
        defaults.allowAll = defaults.allowImage ? false : defaults.allowZip ? false : defaults.allowDocument ? false : defaults.allowMedia ? false : defaults.allowAll;//如果指定某种上传文件类型，则默认全部类型则失效。

        if (defaults.upLoadUrl == "") {
            layer.msg("请指定上传地址", { shade: 0.01, time: 1500 });
            return;
        }
        else if (defaults.allowAll == false && defaults.allowImage == false && defaults.allowZip == false && defaults.allowDocument == false && defaults.allowMedia == false) {
            layer.msg("请指定上传文件类型", { shade: 0.01, time: 1500 });
            return;
        }

        var mimeTypes = new Array();
        if (options.allowAll && !options.allowImage && !options.allowZip && !options.allowDocument && !options.allowMedia) {
            mimeTypes.push({ title: "Image files", extensions: "jpg,gif,png" });
            mimeTypes.push({ title: "Zip files", extensions: "zip,rar,tar" });
            mimeTypes.push({ title: "Document files", extensions: "doc,docx,xls,xlsx,ppt,pptx,pdf,txt" });
            mimeTypes.push({ title: "Media files", extensions: "mp3,mp4" });
        }
        else {
            if (options.allowImage)
                mimeTypes.push({ title: "Image files", extensions: "jpg,gif,png" });

            if (options.allowZip)
                mimeTypes.push({ title: "Zip files", extensions: "zip,rar,tar" });

            if (options.allowDocument)
                mimeTypes.push({ title: "Document files", extensions: "doc,docx,xls,xlsx,ppt,pptx,pdf,txt" });

            if (options.allowMedia)
                mimeTypes.push({ title: "Media files", extensions: "mp3,mp4" });
        }

        //初始化上传对象
        var uploader = new plupload.Uploader({
            browse_button: $(this)[0], //触发文件选择对话框的按钮，为那个元素id
            url: options.upLoadUrl, //服务器端的上传页面地址
            multipart_params: options.extraParams,
            flash_swf_url: '/Others/plupload-2.3.1/js/Moxie.swf', //swf文件，当需要使用swf方式进行上传时需要配置该参数
            silverlight_xap_url: '/Others/plupload-2.3.1/js/Moxie.xap', //silverlight文件，当需要使用silverlight方式进行上传时需要配置该参数
            multi_selection: options.isMulti,//允许批量上传
            filters: {
                mime_types: mimeTypes,
                max_file_size: options.maxZize > 20 ? 20 + "MB" : options.maxZize <= 0 ? "1MB" : options.maxZize + "MB", //最大上传空间
                prevent_duplicates: options.allowRepeat ? false : true //不允许选取重复文件
            },
            resize: {
                quality: 80,//若图片文件，则自动保留图片质量为80%
            }
        });

        //在实例对象上调用init()方法进行初始化
        uploader.init();
        var layerIndex;//加载层

        //绑定各种事件，并在事件监听函数中做你想做的事
        //当Init事件发生后触发  
        uploader.bind('PostInit', function (uploader) {

            if (options.beforeSend) {
                options.beforeSend(uploader);
            }

        });

        //当队列中的某一个文件正要开始上传前触发 
        uploader.bind('BeforeUpload', function (uploader, file) {

            if (options.isShowLoading) {
                layerIndex = layer.msg(options.loadingText, { icon: 16, shade: 0.01, time: 0 });
            }

            if (options.beforeOnePicUpLoad) {
                options.beforeOnePicUpLoad(uploader, file);
            }

        });

        //当上传队列发生变化后触发
        uploader.bind('FilesAdded', function (uploader, files) {

            uploader.start(); //调用实例对象的start()方法开始上传文件，当然你也可以在其他地方调用该方法

        });

        //在上传文件过程中，不断触发，专门用来显示进度
        uploader.bind('UploadProgress', function (uploader, file) {
        });

        //在完成一个文件上传时候触发
        uploader.bind('FileUploaded', function (uploader, file, responseObject) {

            if (options.success)
                options.success(uploader, file, responseObject);

        });

        //在完成所有文件上传时候触发
        uploader.bind('UploadComplete', function (uploader, files) {

            if (options.isShowLoading) {
                layer.close(layerIndex);
            }

            if (options.complete)
                options.complete(uploader, files);

        });

        //在发生错误时候触发
        uploader.bind('Error', function (uploader, errObject) {

            if (options.isShowLoading) {
                layer.close(layerIndex);
            }

            if (options.error) {
                options.error(uploader, errObject);
            }
            else {
                if (errObject.code === -600)
                    layer.msg("文件大小超过了" + options.maxZize + "M限制", { shade: 0.01, time: 1500 });
                else
                    layer.msg(errObject.message, { shade: 0.01, time: 1500 });
            }

        });

        //销毁对象前触发
        uploader.bind('Destroy', function (uploader) {
        });

        return uploader;
    }
})(jQuery);

//其他函数
//登录
function login(successToDo) {
    $("#loginForm")[0].reset();
    $(".login .error").text("");
    $(".login").fadeIn(
        function () {

            $(this).find(".login_tk02").css({
                "top": "180px",
                "left": ($(document.body).width() / 2 - 200) + "px"
            });

            $("#loginForm .btn.green").on("click", function () {

                $(".login .error").text("");
                if ($.trim($("#uid").val()) == "" || $.trim($("#psw").val()) == "")
                    $(".login .error").text("用户名或密码不能为空");
                else {
                    $.ajax({
                        url: "http://www.51zxw.net/usercenter/login_uc.asp",
                        type: "post",
                        dataType: "json",
                        data: { uid: escape($("#uid").val()), psw: $("#psw").val(), isrember: $("#rember")[0].checked },
                        error: function () {
                            $(".login .error").text("登录异常，稍后再试");
                        },
                        beforeSend: function () {
                            $(".login .error").removeClass("success");
                            $(".login .error").text("");
                        },
                        success: function (response) {
                            if (response.isSuccess) {
                                if (successToDo) {
                                    successToDo(response);
                                }
                                else {
                                    $(".login .error").addClass("success");
                                    $(".login .error").text("欢迎您回来 " + unescape(response.userId));
                                    setTimeout(function () {
                                        $('.login').hide();
                                        //$("#username").val(unescape(response.userId));
                                        $("#currentUser").text(unescape(response.userId));
                                    }, 1500);
                                }
                            }
                            else {
                                $(".login .error").text(unescape(response.backMes));
                            }
                        }
                    });
                }

            });

        });
}