var defaultline = getDefaultLine("fline");
function getDefaultLine(c_name){if (document.cookie.length>0){
c_start=document.cookie.indexOf(c_name + "=")
if (c_start!=-1){
c_start=c_start + c_name.length+1
c_end=document.cookie.indexOf(";",c_start)
if (c_end==-1) c_end=document.cookie.length
return unescape(document.cookie.substring(c_start,c_end))
}
}
return ""
}
//var j_date = new Date();
//if ((j_date.getHours()>=19) && (j_date.getHours()<=24)){
//var defaultgg ="google";
//var defaultww =400;
//var defaulthh =350;
//var defaultww2 =400;
//var defaulthh2 =350;
//}
//Else{
var defaultgg ="google";
var defaultww =400;
var defaulthh =300;
var defaultww2 =400;
var defaulthh2 =300;

//}
