import React from 'react';
import '../Styles/index.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import Container from 'react-bootstrap/Container';


class Hotels extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            opened: false,
        };
        this.toggleBox = this.toggleBox.bind(this);
    }

    toggleBox() {
        const { opened } = this.state;
        this.setState({
            opened: !opened,
        });
    }

    reviews() {
        return (
            <Card style={{ width: '40rem' }}>

                <Card.Body>
                    <Card.Text>
                        {this.state.data}
                    </Card.Text>
                </Card.Body>
            </Card>
        )
    }
    render() {

        // var { title, children } = this.props;
        const { opened } = this.state;
        var btn_status;
        if (opened) {
            btn_status = 'Hide Reviews';
        } else {
            btn_status = 'Show Reviews';
        }

        return (
            <div>
                <div className="container">

                    <Container>
                        <Card style={{ width: '50rem' }}>

                            <Card.Body>
                                <Card.Title> {this.props.name}</Card.Title>
                                <Card.Text>
                                    <b>Score : </b>{this.props.score}
                                </Card.Text>


                                <Button className="left" onClick={this.toggleBox} variant="primary"> {btn_status} </Button>
                                <br/><br/>
                                {opened && (
                                    <div class="boxContent">
                                        {this.props.review}
                                    </div>
                                )}
                                
                            </Card.Body>
                        </Card>
                    </Container>

                </div>
            </div>
        );
    }
}

export default Hotels;