import React from 'react';
import filterReducer from '../Reducers/reducer.js'
import { createStore } from 'redux';
import { BrowserRouter ,Redirect, Route, Link } from "react-router-dom";

import Testing from './TestComponent.js'
import Col from 'react-bootstrap/Col';

const store = createStore(filterReducer);

class Decide extends React.Component{

    constructor(props)
    {
        super(props);
    }
    render(){
        // console.log("Props : " + this.props.filterBy +" : " )
        const store = createStore(filterReducer);
        var state = store.getState()
        console.log("Props : " + this.props.filterBy +" : " + state.filter_by)
        console.log(state.filter_by=="food")
        if(state.filter_by==="food"){
            alert("food")
            return(
                <BrowserRouter>
                    <Route path="/suggest/food" render={ props => <Testing filterBy="food" />} />
                    <Redirect push to='/suggest/food' /> 
                </BrowserRouter>          
            )
        }
        else if(state.filter_by==="stay"){
            return(
            <BrowserRouter>
                <Route path="/suggest/stay" render={ props => <Testing filterBy="stay" />} />
                <Redirect push to='/suggest/stay' /> 
            </BrowserRouter>
            )            
        }
        else if(state.filter_by==="service"){
            return(
            <BrowserRouter>
                <Route path="/suggest/service" render={ props => <Testing filterBy="service" />} />
                <Redirect push to='/suggest/service' /> 
            </BrowserRouter>
            )    
        }
        else if(state.filter_by==="room"){
            return(
            <BrowserRouter>
                <Route path="/suggest/room" render={ props => <Testing filterBy="room" />} />
                <Redirect push to='/suggest/room' /> 
            </BrowserRouter>
            )
        }
        else {
            return(
                <BrowserRouter>
                    <Route path="/suggest" render={ props => <Testing filterBy="default" />} />
                    <Redirect push to='/suggest' /> 
                </BrowserRouter>           
            )
        }
    }
}

export default Decide;