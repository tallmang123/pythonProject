import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import reportWebVitals from './reportWebVitals';
import { BrowserRouter, Route } from 'react-router-dom';
import First from './First';
import Second from './Second';
import Member from './Member';
import AddData from './AddData';
import Login from './Login';
import axios from 'axios'
import './lang/i18n';

import 'bootstrap/dist/css/bootstrap.css';

ReactDOM.render(
    <BrowserRouter>
        <Route path='/first'    component={ First } />
        <Route path='/second'   component={ Second } />
        <Route path='/member'   component={ Member } />
        <Route path='/addData'  component={ AddData } />
        <Route path='/login'    component={ Login } />
    </BrowserRouter>
    , document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
