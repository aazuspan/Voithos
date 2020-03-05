import React from 'react';
import axios from 'axios';


class Message extends React.Component {
    state = {
        response: null,
        input: '',
    }

    handleSubmit = (event) => {
        event.preventDefault();

        axios.get('http://127.0.0.1:8000/api/', { params: { input_text: this.state.input } })
            .then(res => {
                this.setState({
                    response: res.data.output,
                })
            })
            .catch((err) => {
                this.setState({
                    response: "There was an error connecting to Voithos's server. Try again later."
                });
            })
    }

    handleInputChange = (event) => {
        this.setState({
            input: event.target.value,
        })
    }

    render() {
        return (
            <>
                <form onSubmit={this.handleSubmit}>
                    <input type="text" onChange={this.handleInputChange} value={this.state.input} />
                    <button type="submit">Send</button>
                </form>
                {this.state.response}
            </>
        )
    }
}

export default Message;