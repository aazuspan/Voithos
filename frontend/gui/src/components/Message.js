import React from 'react';


function Message(props) {
    let messageContent = '';

    if (props.sender === 'voithos') {
        // Allow Voithos to respond with markdown
        messageContent = <div dangerouslySetInnerHTML={{ __html: props.content }} />;
    }
    else {
        messageContent = props.content;
    }

    return (
        <div className={`msg msg-${props.sender}`}>
            {messageContent}
        </div>
    )
}

export default Message;