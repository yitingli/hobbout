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
})(jQuery);
