function hidden_form(){
    document.getElementById("place-form").classList.toggle("hide");
}
mapboxgl.accessToken = 'pk.eyJ1IjoibWF4aW0yMjgiLCJhIjoiY2xpZGFqMzdqMDdzZDNkczA1OGhrcm41ciJ9.kTT3VXnvb9Ui1ENZitz0Cw';
var latitude;
var longitude;
var map = new mapboxgl.Map({
container: 'map', 
style: 'mapbox://styles/mapbox/streets-v11', // style URL
center: [92.869157, 56.009349], // starting position [lng, lat]
zoom: 11 // starting zoom
});
map.on('click', function(event) {
    var marker = new mapboxgl.Marker()
      .setLngLat(event.lngLat)
      .addTo(map);
  
    
      latitude = event.lngLat.lat;
      longitude = event.lngLat.lng;
      console.log(latitude);
      console.log(longitude);
});

 $('#place-form').submit(function (e){
    e.preventDefault();
    const data = {
        place_name:  $('.place_name').val(),
        comment: $('.comment').val(),
        latitude: latitude,
        longitude: longitude,
        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
    }
    console.log(data);
    $.ajax({
        url: '/user/',
        type: 'post',
        data: data,
        dataType: 'json',
        success: function(response) {
          console.log('Координаты отправились успешно!');
          document.getElementById('place-from').reset() ;       
        },
        error: function(response) {
          console.log('Координаты не удалось отправить на сервер');
        }
    });
});
