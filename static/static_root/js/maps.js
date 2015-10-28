$(function(){
    var mapProp = {
        center:new google.maps.LatLng(-15.8419612,-70.0176313),
        zoom:15//,
        //scrollwheel:false
    };
    var map=new google.maps.Map($('#map')[0], mapProp);
    /*var marker = new google.maps.Marker({
        position: {
            lat: -15.8419612,
            lng: -70.0176313
        },
        map: map,
        title: ''
    });*/
    var imagen = $.uri('img/house.png');
    console.log(imagen);
    $('#click').click(function(){
        var marker2 = new google.maps.Marker({
            position: {
                lat: -15.8419612+(Math.random()-0.5)/50,
                lng: -70.0176313+(Math.random()-0.5)/50
            },
            title: 'pepe',
            icon: imagen
        });
        marker2.setMap(map);
    });
});
