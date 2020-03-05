import React from 'react';


function Message(props) {
    return (
        <>
            <h3>{props.sender}</h3>
            <p>{props.content}</p>
        </>
    )
}

export default Message;