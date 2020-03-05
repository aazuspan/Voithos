import React from 'react';

import { InputGroup, FormControl, Button, FormGroup } from 'react-bootstrap';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faReply } from '@fortawesome/free-solid-svg-icons';


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
        console.log(this.state.formContent)

        this.setState({
            formContent: '',
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
                            onChange={this.handleFormUpdate}>
                        </FormControl>
                        <InputGroup.Append>
                            <Button variant="outline-secondary" type="submit">
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