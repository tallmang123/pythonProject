import React, { Component } from 'react'
import {Link} from 'react-router-dom'
import {Container, Row, Col, Button, Table,Alert,InputGroup, FormControl} from 'react-bootstrap';
import TableWrite from './TableWrite.js';
import axios from 'axios';
class Member extends Component {

    constructor(props){
        console.log("========constructor=============");
        super(props);
        this.state = { //react는 state를 통해 해당 클래스 변수 관리를 한다고 보면 됨
            tableColumns : ["Seq","Id", "Password","Salt","Status","AddTime"],
            tableData : [],
            inputId : ''
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
        if(inputId == '')
        {
            alert('input data');
            return false;
        }
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

    //view를 구성하는 메인 render함수
    render(){
        console.log("*******************************");
        console.log(this.state.tableData);
        return (
            <Container>
                <br/><br/>
                <Alert key='primary' variant='primary'>This is Test Page</Alert>
                <Row>
                    <Col>
                        <Link to="/AddData"> {/*Link to Class(Page) -- Router에 정의된 url 및 클래스로 링크 처리함*/}
                            <Button variant="primary">Add</Button>
                        </Link>
                    </Col>
                    <Col></Col>
                    <Col>
                        <InputGroup className="mb-3">
                            <FormControl aria-describedby="basic-addon1" onChange={this.inputChange} name="inputId"/>
                            <InputGroup.Prepend>
                                <Button variant="primary" onClick={this.searchClick}>Search</Button>
                            </InputGroup.Prepend>
                        </InputGroup>
                    </Col>
                </Row>
                <br/>
                <Row>
                    {/*TableWrite 모듈 아래와 같이 호출*/}
                    <TableWrite columns={this.state.tableColumns} datas={this.state.tableData}/>
                </Row>
            </Container>
        );
    }
}
export default Member;