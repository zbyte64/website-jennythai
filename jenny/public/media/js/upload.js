// Add upload progress for multipart forms.
$(function() {
    var freq = 1000; // freqency of update in ms
    var progress_url = '/uploadmanager/upload-progress/'; // ajax view serving progress info
    var upload_url = '/uploadmanager/upload-temporary-file/';

    // Generate 32 char random uuid 
    function gen_uuid() {
        var uuid = ""
        for (var i=0; i < 32; i++) {
            uuid += Math.floor(Math.random() * 16).toString(16); 
        }
        return uuid
    }

    function bind_form(form) {
        var uuid = gen_uuid(); // id for this upload so we can fetch progress info.
        
        // Append X-Progress-ID uuid form action
        form.action += (form.action.indexOf('?') == -1 ? '?' : '&') + 'X-Progress-ID=' + uuid;
        
        var $progress = $('<div class="upload-progress"></div>').
            appendTo(form).append('<div class="progress-container"><span class="progress-info">uploading 0%</span><div class="progress-bar"></div></div>');
        $progress.hide();
        // Update progress bar
        function update_progress_info() {
            $.getJSON(progress_url, {'X-Progress-ID': uuid}, function(data, status){
                if (data) {
                    var progress = parseInt(data.uploaded) / parseInt(data.length);
                    var width = $progress.find('.progress-container').width()
                    var progress_width = width * progress;
                    $progress.find('.progress-bar').width(progress_width);
                    if (progress == 1) {
                        $progress.find('.progress-info').text('uploaded');
                    } else {
                        $progress.find('.progress-info').text('uploading ' + parseInt(progress*100) + '%');
                        window.setTimeout(update_progress_info, freq);
                    }
                    $progress.show();
                }
            });
        };

        $(form).submit(function() {
            window.setTimeout(update_progress_info, freq);
        });
    }

    $('form[enctype=multipart/form-data]').submit(function(){ 
        // Prevent multiple submits
        if ($.data(this, 'submitted')) return false;
        if ($(this).find('iframe').data('submitting')) {
            $(this).one("submit_ready", $(this).submit);
            return false;
        }

        $.data(this, 'submitted', true); // mark form as submitted.
    });

    $('form[enctype=multipart/form-data] input[type=file]').each(function(){ 
        var original_field = $(this);
        var parent_form = $(this).parents('form:first');
        var name_field = document.createElement('input');
        var key_field = document.createElement('input');
        $(name_field).attr({name: '_temporary_upload_file',
                            type: 'hidden'}).val($(this).attr('name'));
        $(key_field).attr({name: '_temporary_upload_file_key',
                           type: 'hidden'});
        $(this).after(name_field).after(key_field);
        var subform = document.createElement('form');
        $(subform).attr({action: upload_url,
                         method: 'post',
                         enctype: 'multipart/form-data'});
        $(this).wrap(subform);
        subform = $(this).parent();
        bind_form(subform[0]);
        subform.ajaxForm({dataType: 'json',
                          iframe: true,
                          success: function(data) {
                             $(key_field).val(data[original_field.attr('name')].key);
                             original_field.siblings('.upload-progress').show().find('.progress-info').text('uploaded');
                          }
        });
        $(this).change(function() {
            subform.submit();
        });
    });
});
