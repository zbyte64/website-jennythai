$(document).ready(function(){
    $('#gallery_form .photo_ids > div').append('<div id="selected_photos">Added Photos:<textinput id="id_photo_ids" "name="photo_ids_text"/></div>');
    var href = '/gallery/select/?field=photo_ids_text';
    $('#selected_photos').after('<iframe frameborder="0" style="border:none; width:755px; height:210px;" src="' + href + '"></iframe>');
    $('#gallery_form').submit(function() {
        var value = $('#id_photo_ids').val().split();
        $.each(value, function() {
            $('#selected_photos').append('<input type="hidden" name="photo_ids" value="'+this.split('/').pop()+'"/>');
        });
    });
});
