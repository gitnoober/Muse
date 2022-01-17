import React, { Component } from 'react';
import { render } from 'react-dom';


export default class Dummy extends Component{
    constructor(props){
        super(props);  //calling the constructor of the parent(Component)
    }

    render(){
        return (<p>This is the Dummy Home page</p>);
    }
}
