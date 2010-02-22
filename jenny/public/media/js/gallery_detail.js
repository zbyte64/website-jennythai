$(document).ready(function() {
    $('#photo_list').hover(function() {
        $('#photo_list').fadeTo(500, 1);
    }, function() {
        $('#photo_list').fadeTo(500, 0.01);
    });
    $('#photo_list li a').click(function() {
        $('#current_photo').css('background-image', 'url('+$(this).attr('href')+')');
        return false;
    });
});
