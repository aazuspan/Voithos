const USER = 'user';
const VOITHOS = 'voithos';
const MESSAGE_BOX = document.getElementById('message-container');
const RESPONSE_DELAY_MS = 750;


// When chat is submitted, handle it
document.getElementById('submit-button').addEventListener('click', handleChatInput)

addMessage('Hello! I am Voithos. What can I do for you?', VOITHOS);


// Handle chat input by making a GET request with the data and receiving and displaying the response
function handleChatInput() {
    const input_form = document.getElementById('input-text')
    const input_text = input_form.value;
    const date = new Date();
    // Record when the message is received to set response timeout
    const start_time = date.getTime();

    // Clear the form
    input_form.value = '';

    // Reject inputs without any letters
    if (!input_text.match(/[A-Za-z]+/)) {
        return;
    }


    addMessage(input_text, USER);

    // Send the form data in a GET request
    $.ajax({
        url: '/',
        data: {
            'input_text': input_text,
            'date': date,
        },
        dataType: 'json',

        // If a server response is received, display the response
        success: function (data) {
            const end_time = new Date().getTime();
            // Subtract time it took to get response from delay time
            const delay_time = Math.max(RESPONSE_DELAY_MS - (end_time - start_time), 0);
            addMessage(data['output'], VOITHOS, delay_time)
        }
    })
}

// Add a message to the message box. Message class based on whether it's sent by user or voithos
function addMessage(message, sender, delay = 0) {
    setTimeout(function () {
        MESSAGE_BOX.innerHTML += `<div class='msg msg-${sender}'>${message}</div>`;
        scrollToBottom();
    }, delay);
}

// Automatically scroll to bottom of message box
function scrollToBottom() {
    MESSAGE_BOX.scroll({
        top: MESSAGE_BOX.scrollHeight - MESSAGE_BOX.clientHeight,
        behavior: 'smooth'
    });
}
