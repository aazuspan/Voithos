const USER = 'user';
const VOITHOS = 'voithos';
const MESSAGE_BOX = document.getElementById('message-container');

class MessageQueue {
    constructor() {
        // List of messages to post
        this.queue = [];
        // Currently waiting to poste
        this.active = false;
        this.waitingForResponse = false;
    }

    // Add a message to queue
    addMessage(message) {
        this.queue.push(message);
        this.checkStatus();
    }

    // Check if a message needs to be posted and isn't currently in progress
    checkStatus() {
        if (!this.active && this.queue.length > 0) {
            this.activate();
        }
    }

    // Add a typing indicator to show that a response from Voithos is loading
    waitForResponse() {
        this.waitingForResponse = true;
        this.addTypingIndicator();
    }

    // Start process of posting message
    activate() {
        this.active = true;
        let nextMessage = this.queue.shift();

        if (nextMessage.delay > 0) {
            if (!this.waitingForResponse && nextMessage.sender == VOITHOS) {
                this.addTypingIndicator();
            }
            else {
                this.waitingForResponse = false;
            }

            setTimeout(() => {
                this.postMessage(nextMessage);
            }, nextMessage.delay);
        }
        else {
            this.postMessage(nextMessage);
        }
    }

    // Add the message to the page and reset the process
    postMessage(message) {
        if (message.sender == VOITHOS) {
            this.removeTypingIndicator();
        }

        message.post();
        this.active = false;
        this.checkStatus();
    }

    addTypingIndicator() {
        MESSAGE_BOX.innerHTML += `<div class='msg msg-voithos msg-indicator' id='typing-indicator'></div>`;
        scrollToBottom();
    }

    removeTypingIndicator() {
        let indicator = document.getElementById('typing-indicator');
        if (indicator) {
            indicator.parentNode.removeChild(indicator);
        }
    }
}

class Message {
    constructor(message, sender, delay = 0) {
        this.message = message;
        this.sender = sender;
        this.delay = delay;
    }

    // Add the message to the page
    post() {
        MESSAGE_BOX.innerHTML += `<div class='msg msg-${this.sender}'>${this.message}</div>`;
        scrollToBottom();
    }
}

const queue = new MessageQueue();

// When chat is submitted, handle it
document.getElementById('submit-button').addEventListener('click', handleChatInput)

intro();

// Voithos introduction for new user
function intro() {
    let inputGroupWrapper = document.getElementById('input-group-wrapper')
    queue.addMessage(new Message('Hello! I am Voithos. I am a personal assistant that uses machine learning and artificial intelligence to perform tasks for you.', VOITHOS, 1000));
    queue.addMessage(new Message('You can give me commands or ask me questions by typing in the form at the bottom of the screen and pressing send. For example, you could say "Tell me a joke, Voithos!"', VOITHOS, 1500));

    // Add a blue highlight to the text box that disappears when clicked
    setTimeout(function () {
        inputGroupWrapper.classList.add('blue-highlight');
        inputGroupWrapper.addEventListener('click', function () {
            inputGroupWrapper.classList.remove('blue-highlight');
        }, { once: true });
    }, 3000);

    queue.addMessage(new Message('If you\'re not sure what to ask me, you can type "help" to get a list of commands I will recognize.', VOITHOS, 2000));
}

// Handle chat input by making a GET request with the data and receiving and displaying the response
function handleChatInput() {
    const input_form = document.getElementById('input-text')
    const input_text = input_form.value;
    const sanitized_text = sanitizeText(input_text);
    const date = new Date();
    // Record when the message is received to set response timeout
    const start_time = date.getTime();

    // Clear the form
    input_form.value = '';

    // Reject inputs without any letters
    if (!input_text.match(/[A-Za-z]+/)) {
        return;
    }

    queue.addMessage(new Message(input_text, USER));

    // Send the form data in a GET request
    $.ajax({
        url: '/',
        data: {
            'input_text': sanitized_text,
            'date': date,
        },
        dataType: 'json',

        beforeSend: function () {
            // Add typing indicator and wait for a response from Voithos
            queue.waitForResponse();
        },

        // If a server response is received, display the response
        success: function (data) {
            const end_time = new Date().getTime();
            const response_delay = data['delay'];
            // Subtract time it took to get response from delay time
            const actual_delay = Math.max(response_delay - (end_time - start_time), 0);
            queue.addMessage(new Message(data['output'], VOITHOS, actual_delay));
        }
    });
}

// Remove everything but alphnumeric and whitespace
function sanitizeText(inputText) {
    return inputText.replace(/[^a-zA-Z0-9 ]/g, "");
}


// Automatically scroll to bottom of message box
function scrollToBottom() {
    MESSAGE_BOX.scroll({
        top: MESSAGE_BOX.scrollHeight - MESSAGE_BOX.clientHeight,
        behavior: 'smooth'
    });
}

const themeToggle = document.getElementById('theme-switch');
themeToggle.addEventListener('change', switchTheme, false);
loadSavedTheme();

// Check if dark/light theme has been previously set and switch to that if so
function loadSavedTheme() {
    const savedTheme = localStorage.getItem('theme') ? localStorage.getItem('theme') : null;
    themeToggle.checked = true;
    if (savedTheme === 'dark') {
        themeToggle.click();
    }
}

// Switch between dark and light themes
function switchTheme(e) {
    let currentTheme = 'light';
    if (e.target.checked) {
        currentTheme = 'dark';
    }
    document.documentElement.setAttribute('data-theme', currentTheme);
    localStorage.setItem('theme', currentTheme);
}