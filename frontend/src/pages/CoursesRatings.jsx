import React from 'react';
import PropTypes from 'prop-types';
import {withRouter} from 'react-router';
import {Link} from 'react-router-dom';
import InputValidator from '../components/validation/InputValidator.jsx';
import ValidatedComponent from '../components/validation/ValidatedComponent.jsx';
import * as Actions from '../redux/actions/UserActions';
import {bindActionCreators} from 'redux';
import {connect} from 'react-redux';
import settings from '../config/settings';
import axios from '../api/axios';
import UserSession from '../UserSession';
import _ from 'lodash';
import StarRatings from 'react-star-ratings';

class CoursesRatings extends React.Component {
  constructor() {
    super();
    this.state = {
      errors:{},
      rating:0,
      faculty: '',
      fieldofstudy: '',
      startyears:'',
      on_semester: ''
    }
    this.changeRating = this.changeRating.bind(this);

  }
  

  changeRating(newRating, name ) {
    this.setState({
      rating: newRating
    });
  }

  componentDidMount() {
    const {apiBaseURL} = settings;
    if(UserSession.getToken()===null){this.props.history.push('/login');}
  }


  render() {

    var courses_compulsory=  <p>Przedmiot 1 &nbsp;
    <StarRatings
      rating={this.state.rating}
      starRatedColor="#0078a0"
      starHoverColor="#3498db"
      changeRating={this.changeRating}
      numberOfStars={5}
      starDimension="40px"
      starSpacing="15px"
      name='rating'
    />
    </p>

    return (
      <div>
<div className="row">
          <div className="small-12 columns">
            <div className="nt-box">
              <div className="nt-box-title">
              Oceny kursów
              <div className="row text-center">
              <button className="btn"
                      type="submit"
                      name="submit-login"
                      onClick={this.addFieldOfStudy}
                      disabled={!this.state.canAdd}>
                Aktualizuj
              </button>
            </div>
              </div>
              <div className="nt-box">
              <div className="nt-box-title">
                Obowiązkowe:
                </div>
                {courses_compulsory}
              </div>
              <p></p>
              <div className="nt-box">
              <div className="nt-box-title">
                Obieralne:
                </div>
      </div>
              </div>
            </div>
          </div>
        </div>

      );
  }
} 


CoursesRatings.displayName = 'CoursesRatings';

CoursesRatings.propTypes = {
  field: PropTypes.object
};

function mapDispatchToProps(dispatch) {
  return bindActionCreators(Actions, dispatch);
}

function mapStateToProps(state) {
  return {
    user: _.get(state, 'user'),
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(ValidatedComponent(withRouter(CoursesRatings)));
