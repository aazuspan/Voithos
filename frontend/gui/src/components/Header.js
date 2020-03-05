import React from 'react';

import { Navbar, Nav } from 'react-bootstrap';


class Header extends React.Component {

    constructor() {
        super();
        this.state = {
            theme: this.loadTheme(),
        }
    }

    // Switch between dark and light themes in the component state
    switchTheme = (event) => {
        let currentTheme = 'light';
        if (this.state.theme === 'light') {
            currentTheme = 'dark';
        }

        this.setState({
            theme: currentTheme,
        })
    }

    // Update the display based on the theme
    setTheme() {
        let currentTheme = this.state.theme;
        document.documentElement.setAttribute('data-theme', currentTheme);
        localStorage.setItem('theme', currentTheme);
    }

    // Load if theme was previously saved. Return saved theme or default to light
    loadTheme() {
        const savedTheme = localStorage.getItem('theme') ? localStorage.getItem('theme') : 'light';
        return savedTheme;
    }


    render() {
        this.setTheme();

        return (
            <>
                <Navbar expand="lg">
                    <Navbar.Brand href="#home">VOITHOS</Navbar.Brand>
                    <Navbar.Toggle aria-controls="basic-navbar-nav" />
                    <Navbar.Collapse id="basic-navbar-nav">
                        <Nav className="mr-auto">
                            <Nav.Link href="https://github.com/aazuspan/Voithos/wiki">Documentation</Nav.Link>
                            <Nav.Link href="https://github.com/aazuspan/Voithos">Source Code</Nav.Link>
                        </Nav>

                        <Nav className="navbar-right">
                            <div className="theme-switch-wrapper">
                                <label id="theme-switch" htmlFor="theme-checkbox" title="Switch theme color">
                                    <input type="checkbox" id="theme-checkbox" onChange={this.switchTheme} checked={this.state.theme === 'dark'} />
                                    <div className="slider round"></div>
                                </label>
                            </div>
                        </Nav>
                    </Navbar.Collapse>
                </Navbar>
            </>
        )
    }
}

export default Header;