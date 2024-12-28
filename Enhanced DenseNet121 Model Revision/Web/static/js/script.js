$(document).ready(function () {
    // Init
    $('.image-section').hide();
    $('#loading-text').hide();
    $('#result').hide();

    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $('#imagePreview').attr('src', e.target.result);
            }
            reader.readAsDataURL(input.files[0]);
        }
    }

    $("#imageUpload").change(function () {
        $('.image-section').show();
        $('#btn-predict').show();
        $('#result').text('');
        $('#result').hide();
        readURL(this);
    });

    // Predict
    $('#btn-predict').click(function () {
        var form_data = new FormData($('#upload-file')[0]);
        var selected_model = $('#model-select').val(); // Ambil model dari dropdown
        form_data.append('model', selected_model);    // Tambahkan model ke form data

        // Tampilkan tulisan Loading...
        $(this).hide();
        $('#loading-text').show();

        // Make prediction by calling API /predict
        $.ajax({
            type: 'POST',
            url: '/predict',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: true,
            success: function (data) {
                // Hasil prediksi
                $('#loading-text').hide();
                $('#btn-predict').show();
                $('#result').fadeIn(600);
                $('#result').text('Result: ' + data.result);
            },
            error: function (e) {
                // Error handling
                $('#loading-text').hide();
                $('#btn-predict').show();
                $('#result').fadeIn(600);
                $('#result').text('Error occurred');
            }
        });
    });
});
