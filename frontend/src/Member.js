import React, { Component } from 'react'
import {Container, Row, Col, Button, Table,Alert,InputGroup, FormControl} from 'react-bootstrap';
import TableWrite from './TableWrite.js';
import axios from 'axios';
class Member extends Component {

    constructor(props){
        console.log("========constructor=============");
        super(props);
        this.state = { //react는 state를 통해 해당 클래스 변수 관리를 한다고 보면 됨
            tableColumns : ["Id", "Password","Salt","Status","AddTime"],
            tableData : []
        }
        this.getAccountData();
    }

    getAccountData = async() => {
        let url = 'http://localhost:5000/auth/info';
        //axios
        axios.get(url,
        {
            id:"tallmang123",
            status:"N",
        },
        {
            headers:{
                'Content-type' : 'application/json'
            }
        }).then((response) => { // success
            this.setState({tableData: response.data.data});
            this.tableData = response.data.data;
            console.log(this.tableData);
            console.log("======================");
        })
        .catch((response) => { // fail
            console.log('ERROR');
        });
    }

    searchClick = async() => {
        let url = 'http://localhost:5000/auth/info';
    }
    //view를 구성하는 메인 render함수
    // 임의의 html 구성을 함수로 변경하여 해당 함수로 대체가 가능하다 - TableWrite.js-->
    render(){
        console.log("*******************************");
        console.log(this.state.tableData);
        return (
            <Container>
                <br/><br/>
                <Alert key='primary' variant='primary'>This is Test Page</Alert>
                <Row>
                    <Col></Col>
                    <Col></Col>
                    <Col>
                        <InputGroup className="mb-3">
                            <FormControl aria-describedby="basic-addon1" />
                            <InputGroup.Prepend>
                                <Button variant="primary">Search</Button>
                            </InputGroup.Prepend>
                        </InputGroup>
                    </Col>
                </Row>
                <br/>
                <Row>
                    <TableWrite columns={this.state.tableColumns} datas={this.state.tableData}/>
                </Row>
            </Container>
        );
    }
}
export default Member;