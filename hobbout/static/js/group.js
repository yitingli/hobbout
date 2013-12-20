(function($){

    $('#new-group-post-btn').on('click', function(){
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
