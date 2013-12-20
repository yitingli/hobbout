(function($){

    $('#new-group-post-btn').on('click', function(){
        var data = {};
        data['name'] = $('#new-post-name').val();
        data['area'] = $('#new-post-area').val();
        data['brief_description'] = $('#new-post-bdes').val();
        data['description'] = $('#new-post-des').val();
        $.ajax({
            type: 'POST',
            contentType: 'application/json',
            url: '/api/group/create/',
            data: JSON.stringify(data),
            success: function(res) {
                location.reload();
            },
            error: function(res) {
            }
        });
    });

    $('.join-group-btn').on('click', function(){
        var data = {};
        var group = $(this).attr('data-id')
        data['group'] = group
        $.ajax({
            type: 'POST',
            contentType: 'application/json',
            url: '/api/group/join/',
            data: JSON.stringify(data),
            success: function(res) {
                location.reload();
            },
            error: function(res) {
            }
        });
    });
})(jQuery);
