$(document).ready(function(){
    $('#gallery_form .photo_ids > div').append('<div id="selected_photos">Added Photos:</div>');
    var href = '/gallery/select/?field=selected_photos';
    $('#selected_photos').after('<iframe frameborder="0" style="border:none; width:755px; height:210px;" src="' + href + '"></iframe>');
});
