import React from 'react';
import Card from 'react-bootstrap/Card'

import ContactData from '../Data/ContactInfo.js'

class Contact extends React.Component{
    render()
    {
        var data = ContactData.contact.map(function (d) {
            return(
                <div>
                    <b> { d[0] } </b>
                    <ul>
                        <li> { d[1] } {d[2]} </li>
                        <li> { d[3] } {d[4]} </li>
                    </ul>
                <br />
                </div>
            )
        })

        return(
            <Card style={{ width: '10' }}>
                <div className="my-2 rounded" style={{ background: '#D2691E' }}> 
                    <Card.Header> Contact Information</Card.Header>
                </div>
                <Card.Body style={{ background:"#FFDEAD" }}>
                    <Card.Text>  
                        { data }
                    </Card.Text>
                </Card.Body>
            </Card>
        )
        
    }
}

export default Contact;