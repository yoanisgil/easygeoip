"use strict";

var map = null;
var currentMarker = null;

function initMap() {
    $(':input[type="submit"]').prop('disabled', false);
}

(function () {
    $('form').on('submit', function (evt) {
        if (map == null) {
            map = new google.maps.Map(document.getElementById('map'), {
                zoom: 4
            });
        }

        evt.preventDefault();

        var $container = $("#response");

        var toResolve = $(this).find('input[name=ip_or_domain]').val();

        $container.removeClass('text-danger');
        $container.text('');

        $.get(
            '/' + toResolve
        ).done(function (api_response) {
            if (api_response.hasOwnProperty('error')) {
                $container.addClass('text-danger');
                $container.text(api_response.error);
            } else {
                $container.JSONView(api_response.data);
                $("#map").css({opacity: 1, zoom: 1});

                var latLng = {lat: api_response.data.location.latitude, lng: api_response.data.location.longitude};

                if (currentMarker != null) {
                    currentMarker.setMap(null);
                }

                currentMarker = new google.maps.Marker({
                    position: latLng,
                    map: map,
                    title: 'Hello World!'
                });

                map.setZoom(5);
                map.panTo(currentMarker.position);
            }
        }).fail(function () {
            console.log('error')
        });

        return false;
    })
})(jQuery);
