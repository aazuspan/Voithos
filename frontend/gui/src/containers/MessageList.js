import React from 'react';

import Message from '../components/Message';
import TypingIndicator from '../components/TypingIndicator';


class MessageList extends React.Component {
    constructor() {
        super();
        this.listEndRef = React.createRef();
    }

    componentDidMount() {
        this.scrollToBottom();
    }

    componentDidUpdate() {
        this.scrollToBottom();
    }

    scrollToBottom = () => {
        this.listEndRef.current.scrollIntoView({ behavior: 'smooth' });
    }

    render() {
        this.messages = this.props.messages.map((msg) =>
            <Message
                key={this.props.messages.indexOf(msg)}
                content={msg.content}
                sender={msg.sender} />);

        this.indicator = this.props.showTypingIndicator
            ?
            <TypingIndicator />
            :
            null;

        return (
            <div className="msg-container">
                {this.messages}
                {this.indicator}
                <div ref={this.listEndRef} />
            </div>
        )
    }
}

export default MessageList;