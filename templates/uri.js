{% load staticfiles %}
$.uri = function(url){
    return '{% static '' %}' + url;
}