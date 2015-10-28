$(function(){
    var mapProp = {
        center:new google.maps.LatLng(-15.8419612,-70.0176313),
        zoom:15//,
        //scrollwheel:false
    };
    var map=new google.maps.Map($('#map')[0], mapProp);
    var imagen = $.uri('img/house.png');
    //console.log(imagen);
    $('#click').click(function(){
        var marker = new google.maps.Marker({
            position: {
                lat: -15.8419612+(Math.random()-0.5)/50,
                lng: -70.0176313+(Math.random()-0.5)/50
            },
            title: 'pepe',
            icon: imagen
        });

        marker.addListener('click', function() {
            alert('pepe marika');
        });

        marker.setMap(map);
    });

    $.ajax({
        url: $.uri('../residencias/form/search/'),
        type:'get',
        dataType: 'json',
        success:function(json){
            updateMarkers(json);
        }
    });

    var updateMarkers = function(json){
        $.each(json, function(){
            var $this = this;
            console.log($this.fields);
            var marker = new google.maps.Marker({
                position: {
                    lat: $this.fields.latitude,
                    lng: $this.fields.longitude
                },
                title: $this.fields.description,
                icon: imagen
            });
            marker.addListener('click', function() {
                alert($this.pk);
            });
            marker.setMap(map);
        });
    }

});
