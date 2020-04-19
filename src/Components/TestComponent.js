import React from 'react';
import Hotels from './Hotels.js';

class Testing extends React.Component{

    constructor(props){
        super(props);
        this.state = { hotelName: [], reviews: [], scores: [] };
    }

    render(){


        if(this.props.filterBy == "default"){
            fetch('/suggest').then(response =>
                response.json().then(data => {
                    console.log(data);
                    this.setState({hotelName : data[0]})
                    this.setState({reviews : data[1]})
                    this.setState({scores : data[2]})
                })
            );
        }
        else if(this.props.filterBy == "food"){
            fetch('/suggest/food').then(response =>
                response.json().then(data => {
                    console.log(data);
                    this.setState({hotelName : data[0]})
                    this.setState({reviews : data[1]})
                    this.setState({scores : data[2]})
                })
            );
        }
        else if(this.props.filterBy == "stay"){
            fetch('/suggest/stay').then(response =>
                response.json().then(data => {
                    console.log(data);
                    this.setState({hotelName : data[0]})
                    this.setState({reviews : data[1]})
                    this.setState({scores : data[2]})
                })
            );
        }
        else if(this.props.filterBy == "service"){
            fetch('/suggest/service').then(response =>
                response.json().then(data => {
                    console.log(data);
                    this.setState({hotelName : data[0]})
                    this.setState({reviews : data[1]})
                    this.setState({scores : data[2]})
                })
            );
        }
        else if(this.props.filterBy == "room"){
            fetch('/suggest/room').then(response =>
                response.json().then(data => {
                    console.log(data);
                    this.setState({hotelName : data[0]})
                    this.setState({reviews : data[1]})
                    this.setState({scores : data[2]})
                })
            );
        }

        return(
            <div>
                <Hotels name={this.state.hotelName[0]} score={this.state.scores[0]} review={this.state.reviews[this.state.hotelName[0]]} /> <br />
                <Hotels name={this.state.hotelName[1]} score={this.state.scores[1]} review={this.state.reviews[this.state.hotelName[1]]} /> <br />
                <Hotels name={this.state.hotelName[2]} score={this.state.scores[2]} review={this.state.reviews[this.state.hotelName[2]]} /> <br />
                <Hotels name={this.state.hotelName[3]} score={this.state.scores[3]} review={this.state.reviews[this.state.hotelName[3]]} /> <br />
                <Hotels name={this.state.hotelName[4]} score={this.state.scores[4]} review={this.state.reviews[this.state.hotelName[4]]} />
            </div>
        );
    }
}

export default Testing;