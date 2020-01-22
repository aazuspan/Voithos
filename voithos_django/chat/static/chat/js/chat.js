const USER = 'user';
const VOITHOS = 'voithos';
const MESSAGE_BOX = document.getElementById('message-container');


// When chat is submitted, handle it
document.getElementById('submit-button').addEventListener('click', handleChatInput)

addMessage('Hello! I am Voithos. What can I do for you?', VOITHOS);


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

        // If a server response is received, display the messages
        success: function (data) {
            addMessage(input_text, USER);
            addMessage(data['output'], VOITHOS)
        }
    })
}

// Add a message to the message box. Message class based on whether it's sent by user or voithos
function addMessage(message, sender) {
    if (sender == VOITHOS) {
        // Voithos responses should be slightly delayed for readability
        setTimeout(function () { MESSAGE_BOX.innerHTML += `<div class='msg msg-${sender}'>${message}</div>` }, 750);
    }
    else {
        MESSAGE_BOX.innerHTML += `<div class='msg msg-${sender}'>${message}</div>`;
    }
    scrollToBottom();
}



// Automatically scroll to bottom of message box
function scrollToBottom() {
    MESSAGE_BOX.scrollTop = MESSAGE_BOX.scrollHeight - MESSAGE_BOX.clientHeight;
}
