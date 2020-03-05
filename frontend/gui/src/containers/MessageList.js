import React from 'react';

import Message from '../components/Message';
import TypingIndicator from '../components/TypingIndicator';

function MessageList(props) {
    const messages = props.messages.map((msg) =>
        <Message key={props.messages.indexOf(msg)} content={msg.content} sender={msg.sender} />);

    let indicator = props.showTypingIndicator ? <TypingIndicator /> : null;

    return (
        <div className="msg-container">
            {messages}
            {indicator}
        </div>
    )
}

export default MessageList;