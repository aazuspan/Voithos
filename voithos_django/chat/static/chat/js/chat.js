// Handle chat input by making a GET request with the data and receiving and displaying the response
function handleChatInput() {
    const input_form = document.getElementById('input-text')
    const input_text = input_form.value;
    const output_div = document.getElementById('message-container')

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
            output_div.innerHTML += `<div class='msg msg-user'>${input_text}</div>`;
            output_div.innerHTML += `<div class='msg msg-voithos'>${data['output']}</div>`;
            scrollToBottom();
        }
    })
}

// When chat is submitted, handle it
document.getElementById('submit-button').addEventListener('click', handleChatInput)


// Automatically scroll to bottom of message box
function scrollToBottom() {
    const output_div = document.getElementById('message-container');
    output_div.scrollTop = output_div.scrollHeight - output_div.clientHeight;
}
