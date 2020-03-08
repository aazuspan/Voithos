import React from 'react';
import Spinner from 'react-bootstrap/Spinner';


function TypingIndicator(props) {
    return (
        <div className={`msg msg-voithos msg-indicator`}>
            <Spinner animation="grow" role="status" >
                <span className="sr-only">Loading...</span>
            </Spinner>
            <Spinner animation="grow" role="status" style={{ animationDelay: "75ms" }}>
            </Spinner>
            <Spinner animation="grow" role="status" style={{ animationDelay: "150ms" }}>
            </Spinner>
        </div >
    )
}

export default TypingIndicator;