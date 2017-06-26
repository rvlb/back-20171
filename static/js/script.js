$(document).ready(function() {
    $('#login-btn').click(function(e) {
        e.preventDefault();
        $('#auth-modal').modal('show');
    });

    $('#logout-btn').click(function(e) {
        e.preventDefault();
        $.ajax({
            url: '/contas/logout/',
            success: function(data) {
                location.reload();
            }
        });
    })

    $('#auth-form').submit(function(e) {
        e.preventDefault();
        $.ajax({
            url: '/contas/login/',
            method: 'POST',
            data: $('#auth-form').serialize(),
            dataType: 'json',
            success: function(data) {
                if(!data['result']) alert('Login incorreto!');
                else location.reload();
            }
        });
    });
});
