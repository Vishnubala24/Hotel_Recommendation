
import React, { useEffect } from 'react';
import ReactDOM from 'react-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';


import { BrowserRouter ,Redirect, Route, Link } from "react-router-dom";

import './Styles/App.css';
import './Styles/index.css';
import App from './App.js'
import Contact from './Components/Contact.js'

import Filter from './Components/Filter.js'
import Hotels from './Components/Hotels.js'
import Title from './Components/Title.js'
import filterReducer from './Reducers/reducer.js'
import { createStore } from 'redux';
import { Provider } from 'react-redux';

const store = createStore(filterReducer);


class MainComponent extends React.Component {

    render(){
        return(
            <BrowserRouter>
				<div className="container-fluid" style={{
				backgroundColor: '#FFFACD',
				height : '100',
				width : '100'
              }}>
                    <br />
					<nav className="navbar navbar-expand-lg navbar-dark bg-dark">
						<div className="collpase navbar-collapse">
							<ul className="navbar-nav mr-auto">
								<li className="navbar-item">
									<Link to="/home" className="nav-link">Home</Link>
								</li>
								<li className="navbar-item">
									<Link to="/suggest" className="nav-link">Recommendations</Link>
								</li>
                                <li className="navbar-item">
									<Link to="/contact" className="nav-link">Contact</Link>
								</li>
							</ul>
						</div>
					</nav>
					<br />
					<br/>
					<Route path="/home" exact component={Contact} />
					<Route path="/suggest" component={App} />
                    <Route path="/contact" component={Contact} />
				</div>
            </BrowserRouter>
        );
    }
}

ReactDOM.render(<MainComponent />, document.getElementById('root'));

