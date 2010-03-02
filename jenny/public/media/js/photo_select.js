$(document).ready(function() {
    $('#adminfiles a.insert').live('click', function() {
        var new_photo = '<a class="remove" href="#"><input type="hidden" name="photo_ids" value="'+$(this).attr('rel').split('/').pop()+'"/><img src="'+$(this).attr('href')+'"/></a>';
        $('#selected_photos').append(new_photo);
        return false;
    });
    $('#adminfiles .next, #adminfiles .prev').live('click', function() {
        $('#photo_selector').load($(this).attr('href')+' #adminfiles');
        return false;
    });
    $('#selected_photos .remove').live('click', function() {
        $(this).remove();
        return false;
    });
    $('#gallery_form .photo_ids > div').append('<div id="selected_photos">Added Photos:</div><div id="photo_selector"></div>');
    $('#photo_selector').load('/gallery/select/ #adminfiles');
});
