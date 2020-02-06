const USER = 'user';
const VOITHOS = 'voithos';
const MESSAGE_BOX = document.getElementById('message-container');
const RESPONSE_DELAY_MS = 750;


// When chat is submitted, handle it
document.getElementById('submit-button').addEventListener('click', handleChatInput)
intro();

// Voithos introduction for new user
function intro() {
    let inputGroupWrapper = document.getElementById('input-group-wrapper')
    addMessage('Hello! I am Voithos. I am a personal assistant that uses machine learning and artificial intelligence to perform tasks for you.', VOITHOS);
    setTimeout(function () { addMessage('You can give me commands or ask me questions by typing your input in the form at the bottom of the screen.', VOITHOS); }, 2500);

    // Add a blue highlight to the text box that disappears when clicked
    setTimeout(function () {
        inputGroupWrapper.classList.add('blue-highlight');
        inputGroupWrapper.addEventListener('click', function () {
            inputGroupWrapper.classList.remove('blue-highlight');
        }, { once: true });
    }, 3000);
    setTimeout(function () { addMessage('You can type "help" any time to get a list of possible commands.', VOITHOS); }, 6000);
}


// Handle chat input by making a GET request with the data and receiving and displaying the response
function handleChatInput() {
    const input_form = document.getElementById('input-text')
    const input_text = input_form.value;
    const date = new Date();
    // Record when the message is received to set response timeout
    const start_time = date.getTime();

    // Clear the form
    input_form.value = '';

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
