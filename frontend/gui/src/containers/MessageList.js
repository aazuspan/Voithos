import React from 'react';

import Message from '../components/Message';

function MessageList(props) {
    const messages = props.messages.map((msg) =>
        <Message key={props.messages.indexOf(msg)} content={msg.content} sender={msg.sender} />);

    return (
        <div className="msg-container">
            {messages}
        </div>
    )
}

export default MessageList;