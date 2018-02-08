//Pop-it menu- By Dynamic Drive - Modified by Wbird
//For full source code and more DHTML scripts, visit http://www.dynamicdrive.com
//This credit MUST stay intact for use

var menuOffX=0;	//菜单距连接文字最左端距离
var menuOffY=18;	//菜单距连接文字顶端距离

var fo_shadows=new Array();
var linkset=new Array();

////No need to edit beyond here

var menuIE4=document.all;
var ie55up = IsIE55Up();
var menuNS6=document.getElementById&&!document.all;
var menuNS4=document.layers;
var overIframe = null;
var jsdone = false;	// 未执行其它js前不出菜单

function showmenu(e,index,p,paging){
	if (!jsdone)
		return false;
	//p为当前页数,paging为当前是不是翻页
	if (!document.all&&!document.getElementById&&!document.layers)
		return;

  switch(index){
  	case 3:long=0;dh=100;break;
  	case 8:long=0;dh=100;break;
  	case 14:long=0;dh=125;break;
  	case 390:long=20;dh=75;break;
  	case 28:long=0;dh=100;break;
  	case 18:long=0;dh=50;break;
  	case 35:long=10;dh=125;break;
  	case 471:long=20;dh=50;break;
  	case 29:long=360;dh=25;break;
  	case 44:long=300;dh=50;break;
  	case 293:long=500;dh=25;break;
  	case 53:long=0;dh=50;break;
  	case 351:long=0;dh=75;break;
  	case 451:long=0;dh=75;break;
  	default:long=100;dh=50;break;
  }
	which=linkset[index];
	var pSize=50;	//每页连接数
	var pNum=Math.floor((which.length-1)/pSize)+1;		//页数
	
	//设置菜单内容
	if (pNum==1){
		which = getItemString(which);
	}else{
		which=which.slice( (p-1)*pSize, p*pSize );
		which = getItemString(which);
		if (p==1){
			which+="<font face='Wingdings' color='gray'>&ccedil;</font> ";
		}else{
			which+="<font face='Wingdings' style='cursor:hand' onclick='showmenu(event,"+ index +","+ (p-1) +",true)'>&ccedil;</font> ";
		}
		if (p==pNum){
			which+="<font face='Wingdings' color='gray'>è</font>";
		}else{
			which+="<font face='Wingdings' style='cursor:hand' onclick='showmenu(event,"+ index +","+ (p+1) +",true)'>è</font>";
		}
	}
	
	menuobj=menuIE4? document.all.popmenu : menuNS6? document.getElementById("popmenu") : menuNS4? document.popmenu : "";
	
	menuobj.innerHTML="<div id='navsub2'><div class='l'></div><div class='r'></div><div class='m' style='height:"+dh+"px'><div style='font-size:12px;padding-left:"+long+"px'>"+which+"</div></div></div>";

	

    

	return false;
}

function getItemString(arr)
{
	var str="";
	for(var i=0; i<arr.length; i++){
		var a = arr[i];
		var o_c=document.createElement("DIV");
		var o_a=document.createElement("A");
		o_a.href=urlPrefix+a[1];
		if (a[2])
			o_a.target="_blank";
		o_a.innerHTML=a[0];
		o_c.appendChild(o_a);
		str += o_c.innerHTML;
	}
	return str;
}


function contains_menuNS6(a, b) {
	if (b){
		while (b.parentNode){
			if ((b = b.parentNode) == a){
				return true;
			}
		}
	}
	return false;
}

// 是否IE5.5以上版本
function IsIE55Up () {
	var agt = navigator.userAgent.toLowerCase();
	var isIE = (agt.indexOf("msie")!=-1);
	if (isIE)
	{
		var stIEVer = agt.substring(agt.indexOf("msie ") + 5);
		var verIEFull = parseFloat(stIEVer);
		return verIEFull >= 5.5;
	}
	return false;
}

function delayhidemenu(){
}
