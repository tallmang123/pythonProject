import React, { Component } from 'react'
import {Container, Row, Col, Button, Table} from 'react-bootstrap';

function TableWrite({ columns, data }) {
  return (
    <Container>
        <Table striped bordered hover>
            <thead>
                <tr>
                    {columns.map((column) => (
                        <th key={column} > {column} </th>
                    ))}
                </tr>
            </thead>
            <tbody>
                {data.map(({ Seq, Id, Password, Salt, Status, AddTime }) => (
                    <tr key={Id}>
                        <td>{Seq}</td>
                        <td>{Id}</td>
                        <td>{Password}</td>
                        <td>{Salt}</td>
                        <td>{Status}</td>
                        <td>{AddTime}</td>
                    </tr>
                ))}
            </tbody>
        </Table>
    </Container>
  )
}

export default TableWrite