$(function(){
    var map=new google.maps.Map($('#map')[0], {
        center:new google.maps.LatLng(-15.8419612,-70.0176313),
        zoom:16//,
        //scrollwheel:false
    });

    var map_residencia= new google.maps.Map($('#map-residencia')[0], {
        center: new google.maps.LatLng(-15.8419612,-70.0176313),
        zoom: 16
    });

    google.maps.event.addListener(map_residencia, "idle", function(){
        google.maps.event.trigger(map_residencia, 'resize');
    });

    var size ={
        x: 30,
        y: 40
    };

    var icons={
        '1':{
            url: $.uri('img/icons/green.png'),
            size: new google.maps.Size(size.x, size.y),
            scaledSize: new google.maps.Size(size.x, size.y),
            origin: new google.maps.Point(0, 0),
            anchor: new google.maps.Point(size.x/2, size.y)
        },
        '2':{
            url: $.uri('img/icons/blue.png'),
            size: new google.maps.Size(size.x, size.y),
            scaledSize: new google.maps.Size(size.x, size.y),
            origin: new google.maps.Point(0, 0),
            anchor: new google.maps.Point(size.x/2, size.y)
        },
        '3':{
            url: $.uri('img/icons/yellow.png'),
            size: new google.maps.Size(size.x, size.y),
            scaledSize: new google.maps.Size(size.x, size.y),
            origin: new google.maps.Point(0, 0),
            anchor: new google.maps.Point(size.x/2, size.y)
        },
        '4':{
            url: $.uri('img/icons/red.png'),
            size: new google.maps.Size(size.x, size.y),
            scaledSize: new google.maps.Size(size.x, size.y),
            origin: new google.maps.Point(0, 0),
            anchor: new google.maps.Point(size.x/2, size.y)
        },
    };

    var nueva_residencia_marker = new google.maps.Marker({
        position: {
            lat: -15.8419612,
            lng: -70.0176313
        },
        title: 'Nueva Residencia',
        icon: icons['1'],
        draggable:true
    });

    nueva_residencia_marker.setMap(map_residencia);

    google.maps.event.addListener(nueva_residencia_marker, 'dragend', function(e){
        console.log(e.latLng.lat()+' '+e.latLng.lng());
    });

    $('#click').click(function(){
        var marker = new google.maps.Marker({
            position: {
                lat: -15.8419612+(Math.random()-0.5)/50,
                lng: -70.0176313+(Math.random()-0.5)/50
            },
            title: 'pepe',
            icon: icons['1']
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
            //console.log($this.fields);
            var marker = new google.maps.Marker({
                position: {
                    lat: $this.fields.latitude,
                    lng: $this.fields.longitude
                },
                title: $this.fields.description,
                icon: icons[$this.fields.tipo_residencia+3]
            });
            marker.addListener('click', function() {
                alert($this.pk);
            });
            marker.setMap(map);
        });
    }

    $('.sede').click(function(e){
        e.preventDefault();
        var $this = $(this);
        map.setCenter(new google.maps.LatLng($this.data('lat')*1, $this.data('lng')*1), 16);
    });

    $('#modal-nueva-residencia').click(function(e){
        e.preventDefault();
        $('#nueva-residencia').foundation('reveal', 'open');
        map_residencia.fitBounds(map_residencia.getBounds());
        google.maps.event.trigger(map_residencia, 'resize');
        map_residencia.setCenter(nueva_residencia_marker.getPosition());
        map_residencia.setZoom(16);
    });

    //google.maps.event.trigger(map, 'resize');

});
