import React, { Component } from 'react'
import {Container, Row, Col, Button}from 'react-bootstrap';

export default class Second extends Component {
    render() {
        return (
            <div className="container">
                <button className="btn btn-danger">Click Me</button>
            </div>
        )
    }
}