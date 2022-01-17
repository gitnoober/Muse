import React, { Component } from 'react';
import { render } from 'react-dom';
import HomePage from './HomePage';

// setting up so that this App is the default export from this file
export default class App extends Component{
    constructor(props){
        super(props); 
    }

    render(){
        return (
            <div className="center">
                <HomePage />
            </div>
        );
    }
}

const appDiv = document.getElementById('app');

render(<App /> , appDiv);
