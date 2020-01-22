// Handle chat input by making a GET request with the data and receiving and displaying the response
function handleChatInput() {
    var input_form = document.getElementById('input-text')
    var input_text = input_form.value;

    var output_ul = document.getElementById('output-text')

    // Clear the form
    input_form.value = '';

    // Send the form data in a GET request
    $.ajax({
        url: '/',
        data: {
            'input_text': input_text
        },
        dataType: 'json',
        // If a response is received, add it to the page
        success: function (data) {
                output_ul.innerHTML += `<li>${data['output']}</li>`;
            }
        })
}

// When chat is submitted, handle it
document.getElementById('submit-button').addEventListener('click', handleChatInput)
