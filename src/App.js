import React from 'react';
import './Styles/App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import ButtonGroup from 'react-bootstrap/ButtonGroup';
import ToggleButton from 'react-bootstrap/ToggleButton';
import { createStore } from 'redux';

import './Styles/App.css';
import './Styles/index.css';

import Decide from './Components/Decide.js'
import Title from './Components/Title.js'
import filterReducer from './Reducers/reducer.js'


const store = createStore(filterReducer);

class App extends React.Component{

  constructor(props) {
    super(props);
    this.state = { filterBy: "default" };
  }

  updateState(event) {
    if(event.target.value){
        console.log(event.target.name +" : "+ event.target.value)
        store.dispatch({type: 'FILTER_BY', category: event.target.value });
        this.setState({filterBy: event.target.value})
        console.log("State value : " + this.state.filterBy)
    }
}


  render() {

    return (
        <div>
            <Title />
            <br /><br />
            <Container>
                <Row>
                    <Col lg={2}>
                    <Container>
                <label>FILTER BY</label><br /><br />
                <div className="d-flex flex-column">

                    <ButtonGroup toggle vertical size="lg">
                        <ToggleButton type="radio" variant="outline-dark" name="generalbtn" value="default" onClick={ this.updateState.bind(this) }>
                            General
                        </ToggleButton><br /><br />
                        <ToggleButton type="radio" variant="outline-dark" name="foodbtn" value="food" onClick={ this.updateState.bind(this) }>
                            Food
                        </ToggleButton><br /><br />
                        <ToggleButton type="radio"  variant="outline-dark" name="staybtn" value="stay"  onClick={ this.updateState.bind(this) }>
                            Stay
                        </ToggleButton><br /><br />
                        <ToggleButton type="radio" variant="outline-dark" name="servicebtn" value="service"  onClick={ this.updateState.bind(this) }>
                            Staff & Service
                        </ToggleButton><br /><br />
                        <ToggleButton type="radio" variant="outline-dark" name="roombtn" value="room"  onClick={ this.updateState.bind(this) }>
                            Rooms
                        </ToggleButton>
                    </ButtonGroup>
                </div>
            </Container>
                    </Col>
                    <Col lg={10}>
                        <Decide filterBy={this.state.filterBy} />  
                    </Col>
                </Row>
            </Container>
        </div>
    )
}
}


export default App;




    // const { hotelName, reviews, scores } = this.props;
  
    // console.log("After getting current state : " + currentState.isRendered);
    // if (currentState.filter_by == "Food")// && !currentState.isRendered) 
    // {
    //     console.log("Food")
    //     fetch('/suggest/food').then(response =>
    //         response.json().then(data => {
    //             console.log(data);
    //             this.setState({ hotelName: data[0] });
    //             this.setState({ reviews: data[1] })
    //             this.setState({ scores: data[2] })
    //         })
    //     );
    //     store.dispatch({ type: 'ISRENDERED'});
    // }
    // else if(currentState.filter_by == "Stay")// && !currentState.isRendered) 
    // {
    //     fetch('/suggest/stay').then(response =>
    //         response.json().then(data => {
    //             console.log(data);
    //             this.setState({ hotelName: data[0] });
    //             this.setState({ reviews: data[1] })
    //             this.setState({ scores: data[2] })
    //         })
    //     );
    //     store.dispatch({ type: 'ISRENDERED'});
    // }
    // else if(currentState.filter_by == "Service")// && !currentState.isRendered) 
    // {
    //     fetch('/suggest/service').then(response =>
    //         response.json().then(data => {
    //             console.log(data);
    //             this.setState({ hotelName: data[0] });
    //             this.setState({ reviews: data[1] })
    //             this.setState({ scores: data[2] })
    //         })
    //     );
    //     store.dispatch({ type: 'ISRENDERED'});
    // }
    // else if(currentState.filter_by == "Room")// && !currentState.isRendered) 
    // {
    //     fetch('/suggest/room').then(response =>
    //         response.json().then(data => {
    //             console.log(data);
    //             this.setState({ hotelName: data[0] });
    //             this.setState({ reviews: data[1] })
    //             this.setState({ scores: data[2] })
    //         })
    //     );
    //     store.dispatch({ type: 'ISRENDERED'});
    // }
    // else if(currentState.filter_by == "default" && count==0)// && !currentState.isRendered)
    // {
    //     console.log("Current state is filtered by")
    //     fetch('/suggest').then(response =>
    //         response.json().then(data => {
    //             console.log(data);
    //             this.setState({ hotelName: data[0] });
    //             this.setState({ reviews: data[1] })
    //             this.setState({ scores: data[2] })
    //         })
    //     );
    //     store.dispatch({ type: 'ISRENDERED'});
    //     count++;
    // }
    