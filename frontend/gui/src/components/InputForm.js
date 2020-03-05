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
    }

    handleFormUpdate = (event) => {
        this.setState({
            formContent: event.target.value,
        })
    }

    handleSubmit = (event) => {
        event.preventDefault();

        let newMessage = {
            content: this.state.formContent,
            sender: USER,
        }

        this.props.addMessage(newMessage);

        this.setState({
            formContent: '',
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