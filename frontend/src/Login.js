import React, { Component } from 'react';
import {Link} from 'react-router-dom';
import {Container, Form, Button, Card, Row, Col, Image} from 'react-bootstrap';
import TableWrite from './TableWrite.js';
import axios from 'axios';
import {withTranslation} from "react-i18next";
import i18n from "./lang/i18n";


class Login extends Component
{
    constructor(props){
        super(props);
        this.state = {
            account : '',
            password : '',
            show:false,
            errorMsg : ''
        }
    }

    handleChange = e => {
        this.setState({
            [e.target.name]: e.target.value
        })
    }

    googleLogin = async() =>{
        window.location.href = "/googleLogin";
    }

    accountLogin = async() => {
        let {account,password} = this.state
        let md5 = require("md5");

        let url = '/auth/login';
        //axios get
        axios.post(url,{
            id:account,
            password:md5(password)
        },
        {
            headers:
            {
                'Content-type' : 'application/json'
            }
        }).then((response) => { // success
            console.log(response)
            window.location.href = "/member";
        })
        .catch((error) => { // fail
            console.log(error.response.data)
            console.log(error.response.data.message)
            this.setState({show: true, errorMsg: error.response.data.message});
        });
    }

    render(){
        const { t , i18n } = this.props;

        return (
        <Container fluid>
            <br/><br/><br/>
            <Row>
                <Col></Col>
                <Col>
                    <Card className="">
                        <Card.Header>{t('login')}</Card.Header>
                            <Card.Body>
                                <Form>
                                    <Form.Group as={Row}>
                                        <Form.Label column sm="4">{t('account')}</Form.Label>
                                        <Col sm="8">
                                            <Form.Control type="text" placeholder={t('account_input')} name="account" onChange={this.handleChange}/>
                                        </Col>
                                    </Form.Group>
                                    <Form.Group as={Row}>
                                        <Form.Label column sm="4">{t('password')}</Form.Label>
                                        <Col sm="8">
                                            <Form.Control type="password" placeholder={t('password_input')} name="password" onChange={this.handleChange}/>
                                        </Col>
                                    </Form.Group>
                                    {this.state.show == true &&
                                        <p style={{color:'red'}}>* {this.state.errorMsg}</p>
                                    }
                                </Form>
                                <Button variant="primary" className="w-100" onClick={this.accountLogin}>{t('login')}</Button>
                                <br/><br/>
                                <Button variant="default" onClick={this.googleLogin}><Image src="./static/btn_google_signin1.png"/></Button>
                            </Card.Body>
                        </Card>
                    </Col>
                <Col></Col>
            </Row>
        </Container>
        );
    }
}

export default withTranslation()(Login);