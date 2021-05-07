import React, { Component } from 'react'
import {Container, Row, Col, Button, Table} from 'react-bootstrap';

function TableWrite({ columns, datas }) {
  console.log("===================tablewrite=================");
  console.log(columns);
  console.log(datas);
  return (
    <Table striped bordered hover>
        <thead>
            <tr>
                {columns.map((column) => (
                <th key={column} > {column} </th>
                ))}
            </tr>
        </thead>
        <tbody>
            {datas.map(data => (
                <tr key={data.Seq}>
                    <td>{data.Id}</td>
                    <td>{data.Password}</td>
                    <td>{data.Salt}</td>
                    <td>{data.Status}</td>
                    <td>{data.AddTime}</td>
                </tr>
            ))}
        </tbody>
    </Table>
  );
}

export default TableWrite