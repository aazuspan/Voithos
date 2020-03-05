import axios from 'axios';
import React from 'react';

import { InputGroup, FormControl, Button } from 'react-bootstrap';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faReply } from '@fortawesome/free-solid-svg-icons';

const USER = 'user';
const VOITHOS = 'voithos';


class InputForm extends React.Component {
    state = {
        formContent: '',
        userMessageHistory: [],
        currentMessageHistoryIndex: -1,
    }

    handleFormUpdate = (event) => {
        this.setState({
            formContent: event.target.value,
        })
    }

    handleKeyPress = (event) => {
        if (event.key === 'ArrowUp') {
            this.messageHistoryUp();
        }
        else if (event.key === 'ArrowDown') {
            this.messageHistoryDown();
        }
    }

    // Allow access to previous message in history
    messageHistoryUp = () => {
        let newMessageHistoryIndex;

        // Prevent indexes outside of history range
        if (this.state.currentMessageHistoryIndex + 1 < this.state.userMessageHistory.length) {
            newMessageHistoryIndex = this.state.currentMessageHistoryIndex + 1;
        }
        else {
            newMessageHistoryIndex = this.state.userMessageHistory.length - 1;
        }

        this.setState({
            currentMessageHistoryIndex: newMessageHistoryIndex,
        }, this.loadMessageFromHistory)
    }

    // Allow access to next message in history
    messageHistoryDown = () => {
        let newMessageHistoryIndex;

        // Prevent indexes outside of history range
        if (this.state.currentMessageHistoryIndex - 1 >= 0) {
            newMessageHistoryIndex = this.state.currentMessageHistoryIndex - 1;
        }
        else {
            newMessageHistoryIndex = 0;
        }

        this.setState({
            currentMessageHistoryIndex: newMessageHistoryIndex,
        }, this.loadMessageFromHistory)
    }

    // Store user message history to allow navigating through them
    addMessageToHistory = (message) => {
        let updatedUserMessageHistory = this.state.userMessageHistory.slice();
        updatedUserMessageHistory.unshift(message);

        this.setState({
            userMessageHistory: updatedUserMessageHistory,
        })
    }

    // Set the form content to a previous user message based on position in message history
    loadMessageFromHistory = () => {
        if (this.state.currentMessageHistoryIndex !== -1) {
            this.setState({
                formContent: this.state.userMessageHistory[this.state.currentMessageHistoryIndex],
            })
        }
    }

    handleSubmit = (event) => {
        event.preventDefault();

        let newMessage = {
            content: this.state.formContent,
            sender: USER,
        }

        this.props.addMessage(newMessage);
        this.addMessageToHistory(newMessage.content);

        this.setState({
            formContent: '',
            currentMessageHistoryIndex: -1,
        });

        this.props.waitForResponse();

        axios.get('http://127.0.0.1:8000/api/', { params: { input_text: newMessage.content } })
            .then(res => {
                let responseMessage = {
                    content: res.data.content,
                    sender: VOITHOS,
                }
                this.props.addMessage(responseMessage);
                this.props.stopWaitingForResponse();
            })
            .catch((err) => {
                let errorMessage = {
                    content: "An error occured connecting to Voithos. Please try again later!",
                    sender: VOITHOS,
                }
                this.props.addMessage(errorMessage);
                this.props.stopWaitingForResponse();
            })
    }

    render() {
        return (
            <>
                <form onSubmit={this.handleSubmit}>
                    <InputGroup className="fixed-bottom p-4">
                        <FormControl
                            placeholder="Hello Voithos..."
                            autoComplete="off"
                            aria-label="Input form"
                            value={this.state.formContent}
                            onChange={this.handleFormUpdate}
                            onKeyDown={this.handleKeyPress}
                            maxLength="80"
                        >
                        </FormControl>
                        <InputGroup.Append>
                            <Button type="submit" className="btn-outline-secondary btn-light">
                                <FontAwesomeIcon icon={faReply} />
                            </Button>
                        </InputGroup.Append>
                    </InputGroup>
                </form>
            </>
        )
    }
}

export default InputForm;