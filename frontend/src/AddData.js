import React, { Component } from 'react'
import {Link} from 'react-router-dom'
import {Container, Form, Alert, Row, Col, Button, Modal} from 'react-bootstrap';
import TableWrite from './TableWrite.js';
import axios from 'axios';
import {withTranslation} from "react-i18next";

class AddData extends Component {

    constructor(props){
        console.log("========constructor=============");
        super(props);
        this.state = { //react는 state를 통해 해당 클래스 변수 관리를 한다고 보면 됨
            account : '',
            password : '',
            passwordConfirm : '',
            show : false
        }
    }
    handleClose = async() =>
    {
        this.setState({show: false});
        console.log(this.state)
    }

    handleShow = async() =>
    {
        this.setState({show: true});
        console.log(this.state)
    }

    handleChange = e => {
        this.setState({
            [e.target.name]: e.target.value
        })
    }

    submitData = async()=>
    {
        let {account,password,passwordConfirm} = this.state
        let md5 = require("md5");

        if(password != passwordConfirm)
        {
            alert('password mismatch')
            return false;
        }

        //axios get
        axios.post('/auth/info',{
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
            this.setState({show: true});
        })
        .catch((error) => { // fail
            console.log(error.response.data)
        });
    }

    //view를 구성하는 메인 render함수
    render(){
        console.log("*******************************");
        const { t , i18n } = this.props;
        return (
            <Container>
                <br/><br/>
                <Alert key='primary' variant='primary'>{t('member_add_title')}</Alert>
                <Form action="" method="post" onSubmit={this.formSubmit}>
                    <Form.Group as={Row} controlId="formHorizontalId">
                        <Form.Label column sm={2}>{t('account')}</Form.Label>
                        <Col sm={4}>
                            <Form.Control type="text" placeholder="Account" name="account" onChange={this.handleChange}/>
                        </Col>
                    </Form.Group>

                    <Form.Group as={Row} controlId="formHorizontalPassword">
                        <Form.Label column sm={2}>{t('password')}</Form.Label>
                        <Col sm={4}>
                            <Form.Control type="password" placeholder="Password" name="password" onChange={this.handleChange}/>
                        </Col>
                    </Form.Group>

                    <Form.Group as={Row} controlId="formHorizontalPasswordConfirm">
                        <Form.Label column sm={2}>{t('password_confirm')}</Form.Label>
                        <Col sm={4}>
                            <Form.Control type="password" placeholder="Password Confirm" name="passwordConfirm" onChange={this.handleChange}/>
                        </Col>
                    </Form.Group>
                </Form>
                <br/><br/><br/>
                <Row>
                    <Col></Col>
                    <Col></Col>
                    <Col sm={4}>
                        <Row>
                            <Col sm={6}>
                                <Button variant="primary" onClick={this.submitData}>{t('add')}</Button>
                            </Col>
                            <Col sm={6}>
                                <Link to="/Member">
                                    <Button variant="secondary">{t('cancel')}</Button>
                                </Link>
                            </Col>
                        </Row>
                    </Col>
                </Row>
                <Modal show={this.state.show} onHide={this.handleClose}>
                    <Modal.Body><p>Process Succeed</p></Modal.Body>
                    <Modal.Footer>
                        <Button variant="primary" onClick={this.handleClose}>Confirm</Button>
                    </Modal.Footer>
                </Modal>
            </Container>
        );
    }
}
//export default AddData;
//i18n , react-i18n
//useTranslation : function export 하는 방식인경우 사용
//withTranslation : class export 하는 방식이면 아래와 같이사용
export default withTranslation()(AddData);
