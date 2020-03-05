import React from 'react';

import Message from '../components/Message';

function MessageList(props) {
    const messages = props.messages.map((msg) =>
        <Message content={msg.content} sender={msg.sender} />);

    return (
        <>
            {messages}
        </>
    )
}

export default MessageList;