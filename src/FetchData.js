
export default function filterByDefault() {
    // alert("Gafdf")
    var res;
    fetch('/suggest').then(response =>
        response.json().then(data => {
            console.log(data);
            // return data;
            // console.log(data);
        })
    );
}

export function filterByFood(){
    fetch('/suggest/food').then(response =>
        response.json().then(data => {
            console.log(data);
            return {
                type : 'SUGGEST',
                hotelName : data[0],
                reviews : data[1],
                scores : data[2]
            }
            // this.setState({ hotelName: data[0] });
            // this.setState({ reviews: data[1] })
            // this.setState({ scores: data[2] })
        })
    );
}

export function filterByStay() {
    fetch('/suggest/stay').then(response =>
        response.json().then(data => {
            console.log(data);
            return {
                type : 'SUGGEST',
                hotelName : data[0],
                reviews : data[1],
                scores : data[2]
            }
            
        })
    );
}

export function filterByService(){
    fetch('/suggest/service').then(response =>
        response.json().then(data => {
            console.log(data);
            return {
                type : 'SUGGEST',
                hotelName : data[0],
                reviews : data[1],
                scores : data[2]
            }
        })
    );
}

export function filterByRoom() {
    fetch('/suggest/room').then(response =>
        response.json().then(data => {
            console.log(data);
            return {
                type : 'SUGGEST',
                hotelName : data[0],
                reviews : data[1],
                scores : data[2]
            }
        })
    );
}