$(document).ready(function() {
    $('#projectForm').submit(function(e) {
        e.preventDefault();  // Prevent the default form submission behavior

        // Collect form data
        const formData = new FormData(this);

        // Send the data to the server using AJAX
        $.ajax({
            url: '/projects',  // Flask route to handle the data
            type: 'POST',
            data: formData,
            contentType: false,
            processData: false,
            success: function(response) {
                console.log('Data submitted successfully:', response);
                // You can handle the response from the server here if needed
            },
            error: function(error) {
                console.error('Error submitting data:', error);
            }
        });
    });

    // Show/hide GitHub link input based on checkbox
    $('#githubLinkCheckbox').change(function() {
        $('#githubLinkContainer').toggle(this.checked);
    });
});
