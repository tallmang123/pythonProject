import React, { Component } from 'react'
import {Container, Row, Col, Button, Table} from 'react-bootstrap';
import TableWrite from './TableWrite.js';

class Member extends Component {
    constructor(props){
        super(props);
    }

    getAccountData = async() => {
        //axios.get
    }
    //view를 구성하는 메인 render함수
    render(){
        let columns = ["Seq", "Id", "Password","Salt","Status","AddTime"];
        let datas = [{
            Seq  : 1,
            Id : "tallmang123",
            Password : "1cdc2cdvdfa",
            Salt : "cd2",
            Status : "N",
            AddTime : "2021-05-03 00:00:00"
        }];
        return (
            <TableWrite columns={columns} data={datas}/>
        );
    }
}
export default Member;