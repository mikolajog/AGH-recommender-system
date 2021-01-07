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

class ProfessorsRatings extends React.Component {
  constructor() {
    super();
    this.state = {
      errors:{},
      faculty: '',
      fieldofstudy: '',
      startyears:'',
      on_semester: '',
      canSubmit:true, 
      currentfieldsofstudy:[],
      professors:[],
    }

    this.changeRatingProf = this.changeRatingProf.bind(this);
    this.setDatasFieldofstudy = this.setDatasFieldofstudy.bind(this);
    this.updateC = this.updateC.bind(this);

  }

  componentDidMount() {
    const {apiBaseURL} = settings;
    if(UserSession.getToken()===null){this.props.history.push('/login');}
    
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

  changeRatingProf(val, index) {
    // 1. Make a shallow copy of the items
    let professors = [...this.state.professors];
    // 2. Make a shallow copy of the item you want to mutate
    let item = {...professors[index]};
    // 3. Replace the property you're intested in
    item.rating = val;
    // 4. Put it back into our array. N.B. we *are* mutating the array here, but that's why we made a copy first
    professors[index] = item;
    // 5. Set the state to our new copy
    this.setState({professors});
    var faculty = this.state.recfaculty;
    var fieldofstudy = this.state.recfieldofstudy;
    var startyears = this.state.recstartyears;
    var onsemester = this.state.recon_semester;
    var currentfieldsofstudy = this.state.currentfieldsofstudy;
    this.props.updateProfessors({currentfieldsofstudy, faculty, fieldofstudy, startyears, onsemester, professors})
    this.props.getProfessors({currentfieldsofstudy, faculty, fieldofstudy, startyears})
  }

  updateC(e){
    this.props.getUserFieldsOfStudy();
    if(this.state.recfaculty && this.state.recfieldofstudy && this.state.recstartyears && this.state.recon_semester && this.state.currentfieldsofstudy){
      var faculty = this.state.recfaculty;
      var fieldofstudy = this.state.recfieldofstudy;
    var startyears = this.state.recstartyears;
    var on_semester = this.state.recon_semester;
    var currentfieldsofstudy = this.state.currentfieldsofstudy;
    this.props.getProfessors({currentfieldsofstudy, faculty, fieldofstudy, startyears})
    var {professors} = this.props.fieldofstudy.professors;
    this.setState({
      professors:professors
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
    var professors  = this.state.professors;
    if(Array.isArray(professors) ){
      var professors_stars = Array.from(this.state.professors).map((anObjectMapped, index) => {
        return (
          <p>{professors[index].name} &nbsp;
          <StarRatings
            rating={professors[index].rating}
            starRatedColor="#0078a0"
            starHoverColor="#3498db"
            changeRating={this.changeRatingProf}
            numberOfStars={5}
            starDimension="40px"
            starSpacing="15px"
            name={index}
          />
          </p>
        );})
    }

    return (
    <div>
      <div className="row">
                <div className="small-12 columns">
                  <div className="nt-box">
                    <div className="nt-box-title">
                    Oceny Profesorów
                    <p>Wybierz kierunek studiów i wprowadź ocenę w skali 1-5 (5 to najlepsza ocena) dla każdej osoby.</p>
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
                   {professors_stars}
                  </div>
                </div>
              </div>
              </div>
              </div>

      );
  }
} 


ProfessorsRatings.displayName = 'Keywords';

ProfessorsRatings.propTypes = {
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

export default connect(mapStateToProps, mapDispatchToProps)(ValidatedComponent(withRouter(ProfessorsRatings)));
