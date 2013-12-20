(function($){
    $('#new-post-btn').on('click', function(){
        var data = {};
        data['name'] = $('#new-post-name').val();
        data['content'] = $('#new-post-content').val();
        data['topic_type'] = $(this).attr('data-type');
        data['group'] = $(this).attr('data-id');
        $.ajax({
            type: 'POST',
            contentType: 'application/json',
            url: '/api/topic/create/',
            data: JSON.stringify(data),
            success: function(res) {
                location.reload();
            },
            error: function(res) {
            }
        });
    });

    $('.new-comment-btn').on('click', function(){
        var data = {};
        var topic = $(this).attr('data-id')
        data['topic'] = topic
        data['content'] = $('#new-comment-'+topic).val();
        $.ajax({
            type: 'POST',
            contentType: 'application/json',
            url: '/api/topic/comment/create/',
            data: JSON.stringify(data),
            success: function(res) {
                location.reload();
            },
            error: function(res) {
            }
        });
    });

    $('#new-act-post-btn').on('click', function(){
        var data = {};
        data['name'] = $('#new-post-name').val();
        data['content'] = $('#new-post-content').val();
        data['group'] = $(this).attr('data-id');
        data['start_time'] = $('#new-post-start-time').val();
        data['end_time'] = $('#new-post-end-time').val();
        data['capacity'] = $('#new-post-capacity').val();
        data['place'] = $('#new-post-place').val();
        $.ajax({
            type: 'POST',
            contentType: 'application/json',
            url: '/api/activity/create/',
            data: JSON.stringify(data),
            success: function(res) {
                location.reload();
            },
            error: function(res) {
            }
        });
    });

    $('.new-act-comment-btn').on('click', function(){
        var data = {};
        var activity = $(this).attr('data-id')
        data['activity'] = activity
        data['content'] = $('#new-comment-'+activity).val();
        $.ajax({
            type: 'POST',
            contentType: 'application/json',
            url: '/api/activity/comment/create/',
            data: JSON.stringify(data),
            success: function(res) {
                location.reload();
            },
            error: function(res) {
            }
        });
    });

    $('.participate-act-btn').on('click', function(){
        var data = {};
        var activity = $(this).attr('data-id')
        data['activity'] = activity
        $.ajax({
            type: 'POST',
            contentType: 'application/json',
            url: '/api/activity/participate/',
            data: JSON.stringify(data),
            success: function(res) {
                location.reload();
            },
            error: function(res) {
            }
        });
    });
})(jQuery);
