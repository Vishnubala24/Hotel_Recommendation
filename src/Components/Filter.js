import React from 'react';
import '../Styles/index.css';
import Container from 'react-bootstrap/Container';
import ButtonGroup from 'react-bootstrap/ButtonGroup';
import ToggleButton from 'react-bootstrap/ToggleButton'
import { BrowserRouter ,Redirect, Route } from "react-router-dom";

import Testing from './TestComponent.js'

import { createStore } from 'redux';
import filterReducer from '../Reducers/reducer.js';

const store = createStore(filterReducer);

class Filter extends React.Component {

    constructor(props)
    {
        super(props);
        this.updateState.bind(this);
    }

    updateState(event) {
        if(event.target.value){
            console.log(event.target.name +" : "+ event.target.value)
            store.dispatch({type: 'FILTER_BY', category: event.target.value });
        }
    }

    render() {

        const { filterByFood, filterByStay, filterByService, filterByRoom } = this.props;

        return (
            <Container>
                <label>FILTER BY</label><br /><br />
                <div className="d-flex flex-column">

                    <ButtonGroup toggle vertical size="lg">
                        <ToggleButton type="radio" variant="outline-dark" name="generalbtn" value="default" onClick={ this.updateState.bind(this) }>
                            General
                            {/* <BrowserRouter>
                                <Redirect push to="/suggest" />
                            </BrowserRouter> */}
                            
                        </ToggleButton><br /><br />
                        <ToggleButton type="radio" variant="outline-dark" name="foodbtn" value="food" onClick={ this.updateState.bind(this) }>
                            Food
                            {/* <BrowserRouter>
                                <Redirect push to="/suggest/food" />
                            </BrowserRouter> */}
                            
                        </ToggleButton><br /><br />
                        <ToggleButton type="radio"  variant="outline-dark" name="staybtn" value="stay"  onClick={ this.updateState.bind(this) }>
                            Stay
                            {/* <BrowserRouter>
                                <Redirect push to="/suggest/stay" />
                            </BrowserRouter> */}
                        </ToggleButton><br /><br />
                        <ToggleButton type="radio" variant="outline-dark" name="servicebtn" value="service"  onClick={ this.updateState.bind(this) }>
                            Staff & Service
                            {/* <BrowserRouter>
                                <Redirect push to="/suggest/service" />
                            </BrowserRouter> */}
                        </ToggleButton><br /><br />
                        <ToggleButton type="radio" variant="outline-dark" name="roombtn" value="room"  onClick={ this.updateState.bind(this) }>
                            Rooms
                            {/* <BrowserRouter>
                                {/* <Route path="/suggest/room" render={ props => <Testing filterBy="room" />} /> */}
                                {/* <Redirect push to="/suggest/room/" />
                            </BrowserRouter> */} 
                        </ToggleButton>
                    </ButtonGroup>
                </div>
            </Container>
        )
    }
}

export default Filter;