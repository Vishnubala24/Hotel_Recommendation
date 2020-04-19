import { connect } from 'react-redux'
import { filterByFood, filterByStay, filterByService, filterByRoom } from '../FetchData.js'

const mapStateToProps = (state) => {
   return {
      hotelName: state.hotelName,
      reviews: state.reviews,
      scores : state.scores
   };
};
const mapDispatchToProps = (dispatch) => {
   return {
      filterByFood: () => dispatch(filterByFood()),
      filterByStay: () => dispatch(filterByStay()),
      filterByService: () => dispatch(filterByService()),
      filterByRoom: () => dispatch(filterByRoom()),
      filterByDefault: () => dispatch(filterByDefault())
   };
};
export default connect(mapStateToProps, mapDispatchToProps)(App);