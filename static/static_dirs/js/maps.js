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

    var update_nueva_residencia = function(){
        $('#latitud').val(nueva_residencia_marker.getPosition().lat());
        $('#longitud').val(nueva_residencia_marker.getPosition().lng());
    }

    google.maps.event.addListener(nueva_residencia_marker, 'dragend', function(e){
        update_nueva_residencia();
    });

    var updateMap = function(){
        $.ajax({
            url: $.uri('../residencias/form/search/'),
            type:'get',
            dataType: 'json',
            success:function(json){
                updateMarkers(json);
            }
        });
    }

    updateMap();

    var updateMarkers = function(json){
        var html = '';
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
            html += '<tr>';
            html += '<td>'+$this.fields.tipo_residencia+'<td>';
            html += '<td>'+$this.fields.title+'<td>';
            html += '<td>'+$this.fields.gender+'<td>';
            html += '</tr>';
        });
        $('#lista-residencias').html(html);
    }

    $('.sede').click(function(e){
        e.preventDefault();
        var $this = $(this);
        map.setCenter(new google.maps.LatLng($this.data('lat')*1, $this.data('lng')*1), 16);
    });

    $('#modal-nueva-residencia').click(function(e){
        e.preventDefault();
        $('#nueva-residencia').foundation('reveal', 'open');
        update_nueva_residencia();
        map_residencia.fitBounds(map_residencia.getBounds());
        google.maps.event.trigger(map_residencia, 'resize');
        map_residencia.setCenter(nueva_residencia_marker.getPosition());
        map_residencia.setZoom(16);
        $('#form-nueva-residencia').trigger("reset");
    });

    //google.maps.event.trigger(map, 'resize');

    $('#form-nueva-residencia').submit(function(e){
        e.preventDefault();
        var $this = $(this);
        $.ajax({
            url:$.uri('../residencias/form/save'),
            data:$this.serialize(),
            type:'get',
            dataType:'json',
            success:function(r){
                updateMap();
                $('#nueva-residencia').foundation('reveal', 'close');
            }
        });
    });

});
