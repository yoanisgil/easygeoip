/**
 * Created by Yoanis Gil on 15-05-09.
 */
"use strict";

(function () {
    $('form').on('submit', function (evt) {
        evt.preventDefault();

        var $container = $("#response");

        var toResolve = $(this).find('input[name=ip_or_domain]').val();

        $container.removeClass('text-danger');
        $container.text('');

        $.get(
            '/' + toResolve
        ).done(function (api_resposne) {
                if (api_resposne.hasOwnProperty('error')) {
                    $container.addClass('text-danger');
                    $container.text(api_resposne.error);
                } else {
                    $container.JSONView(api_resposne.data);
                }
            }).fail(function () {
                console.log('error')
            });

        return false;
    })
})(jQuery);
