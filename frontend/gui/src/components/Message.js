import React from 'react';


function Message(props) {
    return (
        <div className={`msg msg-${props.sender}`}>
            {props.content}
        </div>
    )
}

export default Message;