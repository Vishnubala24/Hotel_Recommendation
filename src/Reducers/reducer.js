const initialState = {
    filter_by : "default",
    isRendered : false,
    hotelName : undefined,
    reviews : undefined,
    scores : undefined
}

function filterReducer(state= initialState, action) {
    switch(action.type){
        case 'FILTER_BY':
            alert("Hi")
            state.filter_by = action.category;
            state.isRendered = false;
            console.log('State changed to : '+ initialState.filter_by);
            return state;
        
        case 'ISRENDERED':
            state.isRendered = true;
            return state;
        
        case 'SUGGEST':
            state.hotelName = action.hotelName;
            state.reviews = action.reviews;
            state.scores = action.scores;
            return state;


        default:
            return state;
    }
}

export default filterReducer;