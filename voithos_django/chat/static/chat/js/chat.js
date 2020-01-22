const USER = 'user';
const VOITHOS = 'voithos';
const MESSAGE_BOX = document.getElementById('message-container')

// Handle chat input by making a GET request with the data and receiving and displaying the response
function handleChatInput() {
    const input_form = document.getElementById('input-text')
    const input_text = input_form.value;

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
            addMessage(input_text, USER);
            addMessage(data['output'], VOITHOS);
        }
    })
}

// Add a message to the message box. Message class based on whether it's sent by user or voithos
function addMessage(message, sender) {
    MESSAGE_BOX.innerHTML += `<div class='msg msg-${sender}'>${message}</div>`;
    scrollToBottom();
}

// When chat is submitted, handle it
document.getElementById('submit-button').addEventListener('click', handleChatInput)


// Automatically scroll to bottom of message box
function scrollToBottom() {
    MESSAGE_BOX.scrollTop = MESSAGE_BOX.scrollHeight - MESSAGE_BOX.clientHeight;
}
