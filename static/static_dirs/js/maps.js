$(function(){
    var mapProp = {
        center:new google.maps.LatLng(51.508742,-0.120850),
        zoom:10,
        mapTypeId:google.maps.MapTypeId.ROADMAP
    };
    var map=new google.maps.Map($('#map')[0], mapProp);
});
