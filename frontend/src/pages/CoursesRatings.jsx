import React from 'react';
import PropTypes from 'prop-types';
import {withRouter} from 'react-router';
import {Link} from 'react-router-dom';
import InputValidator from '../components/validation/InputValidator.jsx';
import ValidatedComponent from '../components/validation/ValidatedComponent.jsx';
import * as Actions from '../redux/actions/FieldofstudyActions';
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
      on_semester: '',
      canSubmit:true, 
      currentfieldsofstudy:[],
      compulsory:[],
      elective:[],
    }
    this.changeRatingComp = this.changeRatingComp.bind(this);
    this.changeRatingElect = this.changeRatingElect.bind(this);
    this.setDatasFieldofstudy = this.setDatasFieldofstudy.bind(this);
    this.updateC = this.updateC.bind(this);

  }
  

  changeRatingComp(val, index) {
    // 1. Make a shallow copy of the items
    let compulsory = [...this.state.compulsory];
    // 2. Make a shallow copy of the item you want to mutate
    let item = {...compulsory[index]};
    // 3. Replace the property you're intested in
    item.rating = val;
    // 4. Put it back into our array. N.B. we *are* mutating the array here, but that's why we made a copy first
    compulsory[index] = item;
    // 5. Set the state to our new copy
    this.setState({compulsory});
    var faculty = this.state.recfaculty;
    var fieldofstudy = this.state.recfieldofstudy;
    var startyears = this.state.recstartyears;
    var onsemester = this.state.recon_semester;
    var currentfieldsofstudy = this.state.currentfieldsofstudy;
    var elective = this.state.compulsory;
    this.props.updateCourses({currentfieldsofstudy, faculty, fieldofstudy, startyears, onsemester, elective, compulsory})
    this.props.getCourses({currentfieldsofstudy, faculty, fieldofstudy, startyears})
  }

  changeRatingElect(val, index) {
    // 1. Make a shallow copy of the items
    let elective = [...this.state.elective];
    // 2. Make a shallow copy of the item you want to mutate
    let item = {...elective[index]};
    // 3. Replace the property you're intested in
    item.rating = val;
    // 4. Put it back into our array. N.B. we *are* mutating the array here, but that's why we made a copy first
    elective[index] = item;
    // 5. Set the state to our new copy
    this.setState({elective});
  }

  componentDidMount() {
    const {apiBaseURL} = settings;
    if(UserSession.getToken()===null){this.props.history.push('/login');}
    else{this.props.getUserFieldsOfStudy();}

  }

  setDatasFieldofstudy(event){
    this.props.getUserFieldsOfStudy();
    var fields = event.target.value.split('/');
    var faculty = fields[3]
    var fieldofstudy = fields[0]
    var startyears = fields[2]
    var on_semester = fields[1]
      this.setState({
      recfaculty: faculty,
      recfieldofstudy: fieldofstudy,
      recstartyears:startyears,
      recon_semester: on_semester,
      canSubmit: faculty && fieldofstudy && startyears && on_semester
      })
  }
  updateC(e){
    this.props.getUserFieldsOfStudy();
    if(this.state.recfaculty && this.state.recfieldofstudy && this.state.recstartyears && this.state.recon_semester && this.state.currentfieldsofstudy){
      var faculty = this.state.recfaculty;
      var fieldofstudy = this.state.recfieldofstudy;
    var startyears = this.state.recstartyears;
    var on_semester = this.state.recon_semester;
    var currentfieldsofstudy = this.state.currentfieldsofstudy;
    this.props.getCourses({currentfieldsofstudy, faculty, fieldofstudy, startyears})
    var {compulsory, elective} = this.props.fieldofstudy.courses;
    this.setState({
      compulsory: compulsory,
      elective:elective
      })
    }
  }


  render() {
    var currentfieldsofstudy = null;
    var {errors, possiblefaculties, possiblefieldsofstudies,currentfieldsofstudy, isFetching} = this.props.fieldofstudy;
    if(Array.isArray(currentfieldsofstudy)){
      var current_fields = Array.from(currentfieldsofstudy).map((anObjectMapped, index) => {
        return (
        <option key={anObjectMapped.fieldofstudyname +'/'+anObjectMapped.onSemester+'/'+anObjectMapped.startYears+'/'+anObjectMapped.faculty} value={anObjectMapped.fieldofstudyname +'/'+anObjectMapped.onSemester+'/'+anObjectMapped.startYears+'/'+anObjectMapped.faculty}>{anObjectMapped.fieldofstudyname +'/'+anObjectMapped.onSemester+'/'+anObjectMapped.startYears+'/'+anObjectMapped.faculty}</option>  
        );})
    }
    var compulsory = this.state.compulsory;
    var elective  = this.state.elective;
    if(Array.isArray(compulsory) ){
      var compulsory_stars = Array.from(this.state.compulsory).map((anObjectMapped, index) => {
        return (
          <p>{compulsory[index].name} &nbsp;
          <StarRatings
            rating={compulsory[index].rating}
            starRatedColor="#0078a0"
            starHoverColor="#3498db"
            changeRating={this.changeRatingComp}
            numberOfStars={5}
            starDimension="40px"
            starSpacing="15px"
            name={index}
          />
          </p>
        );})
    }

    else{var compulsory_stars = null;}
    if(Array.isArray(elective)){
      var elective_stars = Array.from(this.state.elective).map((anObjectMapped, index) => {
        return (
          <p>{elective[index].name}&nbsp;
          <StarRatings
            rating={elective[index].rating}
            starRatedColor="#0078a0"
            starHoverColor="#3498db"
            changeRating={this.changeRatingElect}
            numberOfStars={5}
            starDimension="40px"
            starSpacing="15px"
            name={index}
          />
          </p>
        );})
    }

    else{var compulsory_stars = null;}
    return (
      <div>
<div className="row">
          <div className="small-12 columns">
            <div className="nt-box">
              <div className="nt-box-title">
              Oceny kursów
              </div>
              <select name="delete" id="delete-select" onClick={this.setDatasFieldofstudy}>
    {current_fields}
			</select>
      <div>
              <div className="row text-center">
              <button className="btn"
                      type="submit"
                      name="submit-login"
                      onClick={this.updateC}
                      disabled={!this.state.canSubmit}>
                Aktualizuj
              </button>
            </div>
              </div>
              <div className="nt-box">
              <div className="nt-box-title">
                Obowiązkowe:
                </div>
                {compulsory_stars}
              </div>
              <p></p>
              <div className="nt-box">
              <div className="nt-box-title">
                Obieralne:
                </div>
                {elective_stars}
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
    fieldofstudy: _.get(state, 'fieldofstudy'),
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(ValidatedComponent(withRouter(CoursesRatings)));
