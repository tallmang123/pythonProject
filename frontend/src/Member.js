import React, { Component } from 'react';
import {Link} from 'react-router-dom';
import {Container, Row, Col, Button, Table,Alert,InputGroup, FormControl, Dropdown} from 'react-bootstrap';
import TableWrite from './TableWrite.js';
import axios from 'axios';
import {withTranslation} from "react-i18next";
import i18n from "./lang/i18n";

class Member extends Component {

    constructor(props){
        super(props);
        this.state = { //react는 state를 통해 해당 클래스 변수 관리를 한다고 보면 됨
            tableColumns : ["Seq","Id", "Password","Salt","Status","AddTime"],
            tableData : [],
            inputId : '',
            languageTitle : '한국어'
        }
        this.getAccountData();
    }

    getAccountData = async() => {
        let url = 'http://localhost:5000/auth/info';
        //axios get
        axios.get(url,{},
        {
            headers:
            {
                'Content-type' : 'application/json'
            }
        }).then((response) => { // success
            this.setState({tableData: response.data.data});
        })
        .catch((response) => { // fail
            console.log('ERROR');
        });
    }

    searchClick = async() => {
        let url = 'http://localhost:5000/auth/info';
        let inputId = this.state.inputId
        //axios get
        axios.get(url,
        {
           params:{
                id:inputId
           }
        },
        {
            headers:{
                'Content-type' : 'application/json'
            }
        }).then((response) => { // success
            this.setState({tableData: response.data.data});
        })
        .catch((response) => { // fail
            console.log('ERROR');
        });
    }

    inputChange = e => {
        this.setState({
            [e.target.name]: e.target.value
        })
    }

    changeLanguage = e => {
        i18n.changeLanguage(e.split(',')[0]);
        this.setState({
            "languageTitle": e.split(',')[1]
        });
    }

    //view를 구성하는 메인 render함수
    render(){
        console.log("*******************************");
        console.log(this.state.tableData);
        const { t , i18n } = this.props;
        return (
            <Container>
                <br/><br/>
                <Alert key='primary' variant='primary'>{t('member_title')}</Alert>
                <Row>
                    <Col>
                        <Link to="/AddData"> {/*Link to Class(Page) -- Router에 정의된 url 및 클래스로 링크 처리함*/}
                            <Button variant="primary">{t('add')}</Button>
                        </Link>
                    </Col>
                    <Col></Col>
                    <Col>
                        <InputGroup className="mb-3">
                            <FormControl aria-describedby="basic-addon1" onChange={this.inputChange} name="inputId"/>
                            <InputGroup.Prepend>
                                <Button variant="primary" onClick={this.searchClick}>{t('search')}</Button>
                            </InputGroup.Prepend>
                        </InputGroup>
                    </Col>
                </Row>
                <br/>
                <Row>
                    {/*TableWrite 모듈 아래와 같이 호출*/}
                    <TableWrite columns={this.state.tableColumns} datas={this.state.tableData}/>
                </Row>
                <Row>
                    <Col>
                        <Dropdown onSelect={this.changeLanguage}>
                            <Dropdown.Toggle variant="success" id="dropdown-basic">{this.state.languageTitle}</Dropdown.Toggle>
                            <Dropdown.Menu>
                                <Dropdown.Item eventKey={["ko","한국어"]}>한국어</Dropdown.Item>
                                <Dropdown.Item eventKey={["en","English"]}>English</Dropdown.Item>
                            </Dropdown.Menu>
                        </Dropdown>
                    </Col>
                    <Col></Col>
                    <Col></Col>
                </Row>
            </Container>
        );
    }
}
//i18n , react-i18n
//useTranslation : function export 하는 방식인경우 사용
//withTranslation : class export 하는 방식이면 아래와 같이사용
export default withTranslation()(Member);
//export default Member;