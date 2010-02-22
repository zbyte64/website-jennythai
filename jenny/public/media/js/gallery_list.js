$(document).ready(function() {
    $('.gallery_listing a').mouseover(function() {
        $('#gallery_info > div').hide();
        $($(this).attr('href')).show();
    }).click(function() {
        //alert($($(this).attr('href')+' a:first').click().attr('href'));
        $($(this).attr('href')+' a:last').click();
        return false;
    });
});
