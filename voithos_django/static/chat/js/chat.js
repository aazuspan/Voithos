const USER = 'user';
const VOITHOS = 'voithos';
const MESSAGE_BOX = document.getElementById('message-container');
const RESPONSE_DELAY_MS = 750;


// When chat is submitted, handle it
document.getElementById('submit-button').addEventListener('click', handleChatInput)

addMessage('Hello! I am Voithos. What can I do for you?', VOITHOS, undefined, true);


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
            addMessage(data['output'], VOITHOS, delay_time, null, data['input']);
        }
    })
}

// When a response feedback button is clicked, hide the input text that triggered the response in the feedback modal
$(document).on('click', '.button-review', function (e) {
    addHiddenInputToModal(e);
});

// Enable feedback submit button when a choice is made
$('#command-choices').on('change', function () {
    $('#feedback-submit').prop('disabled', false);
})

// When response feedback is submitted, handle it
$('#feedback-submit').on('click', function (e) {
    handleResponseFeedback(e);
});

// TODO: Fix issue with jquery returning n.fn.init, forcing me to select by index 0
// When a response is reviewed, pass the input that triggered it to the modal
function addHiddenInputToModal(event) {
    responseInput = $(event.target).closest('.msg-voithos').find('.response-input')[0].innerText;
    $('#response-input').text(responseInput);
}

// TODO: send submitted choice and associated user input via Ajax, handle them in Python
function handleResponseFeedback(e) {
    const submitted_choice = $('#command-choices option:selected').text();
}


// Add a message to the message box. Message class based on whether it's sent by user or voithos
function addMessage(message, sender, delay = 0, first = false, input = null) {
    let btn_template = "<button class='btn btn-sm float-right button-review' data-toggle='modal' data-target='#feedback-modal' title='Mark incorrect response'><i class='fa fa-times'></i></button>"

    // Input that prompted the response, if any
    let input_template = '';
    if (input) {
        // Hide it in the message so it can be retrieved for NLU training
        input_template = `<div class="response-input" hidden>${input}</div>`;
    }

    // User messages and first message don't need button to report incorrect response
    if (sender == USER || first == true) {
        btn_template = '';
    }
    setTimeout(function () {
        MESSAGE_BOX.innerHTML += `<div class='msg msg-${sender}'>${message}${btn_template}${input_template}</div>`;
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
