import React from 'react';

import Header from './components/Header';
import InputForm from './components/InputForm';
import MessageList from './containers/MessageList';


class App extends React.Component {

  state = {
    messages: [],
  }

  // Add a new message object to the list of messages
  addMessage = (message) => {
    let currentMessages = this.state.messages.slice();
    currentMessages.push(message);

    this.setState({
      messages: currentMessages,
    })
  }

  render() {
    return (
      <>
        <Header />
        <MessageList messages={this.state.messages} />
        <InputForm addMessage={this.addMessage} />
      </>
    );
  }
}

export default App;
