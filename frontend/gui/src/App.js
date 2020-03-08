import React from 'react';

import Header from './components/Header';
import InputForm from './components/InputForm';
import MessageList from './containers/MessageList';


class App extends React.Component {

  state = {
    messages: [],
    waitingForResponse: false,
  }

  componentDidMount = () => {
    if (!sessionStorage.getItem('introduced')) {
      this.scriptedIntro();
    }
  }

  // Add a new message object to the list of messages
  addMessage = (message) => {
    let currentMessages = this.state.messages.slice();
    currentMessages.push(message);

    this.setState({
      messages: currentMessages,
    });
  }

  // Start waiting for a response from Voithos (show typing indicator)
  waitForResponse = () => {
    this.setState({
      waitingForResponse: true,
    })
  }

  // Stop waiting for a response from Voithos (hide typing indicator)
  stopWaitingForResponse = () => {
    this.setState({
      waitingForResponse: false,
    })
  }

  scriptedIntro = () => {
    this.waitForResponse();

    let introMessage = {
      content: "Hello, I am Voithos! I am an automated personal assistant. Type 'help' to see a list of commands I recognize.",
      sender: "voithos",
    }

    setTimeout(() => {
      this.stopWaitingForResponse();
      this.addMessage(introMessage);
    }, 1500);

    sessionStorage.setItem('introduced', true);
  }

  render() {
    return (
      <>
        <Header />

        <MessageList
          messages={this.state.messages}
          showTypingIndicator={this.state.waitingForResponse} />

        <InputForm
          addMessage={this.addMessage}
          waitForResponse={this.waitForResponse}
          stopWaitingForResponse={this.stopWaitingForResponse} />
      </>
    );
  }
}

export default App;
