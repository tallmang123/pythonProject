import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import reportWebVitals from './reportWebVitals';
import { BrowserRouter, Route } from 'react-router-dom';
import First from './First';
import Second from './Second';

ReactDOM.render(
    <BrowserRouter>
        <Route exact path='/first' component={ First } />
        <Route exact path='/second' component={ Second } />
    </BrowserRouter>
    , document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
