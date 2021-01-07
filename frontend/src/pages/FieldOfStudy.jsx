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

class FieldOfStudy extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      addfaculty: '',
      addfieldofstudy: '',
      addstartyears:'',
      addon_semester: '',
      canAdd:false,
      deletefaculty: '',
      deletefieldofstudy: '',
      deletestartyears:'',
      deleteon_semester: '',
      canDelete:false,
      possible_faculties:<div></div>,
      possible_fieldsofstudy:<div></div>,
      possible_startyears:<div></div>,
    };

    // this.addFieldOfStudy = this.addFieldOfStudy.bind(this);
    this.onChange = this.onChange.bind(this);
    this.changeFaculty = this.changeFaculty.bind(this);
    this.changeField = this.changeField.bind(this);
    this.changeStartYear = this.changeStartYear.bind(this);
    this.changeSemesterNumber = this.changeSemesterNumber.bind(this);
    this.addFieldOfStudy = this.addFieldOfStudy.bind(this);
    this.deleteFieldofstudy = this.deleteFieldofstudy.bind(this);
    this.deleteSelect = this.deleteSelect.bind(this);
  }

  onChange(fieldName, e) {
    this.setState({[fieldName]: e.target.value});

  }

  componentDidMount() {
    const {apiBaseURL} = settings;
    if(UserSession.getToken()===null){this.props.history.push('/login');}
    else{
    this.props.getUserFieldsOfStudy();}
  }


  render() {
    const {apiBaseURL} = settings;
    if(UserSession.getToken()===null){this.props.history.push('/login');}
  //   let fieldOfStudy;
    var {errors, possiblefaculties, possiblefieldsofstudies,currentfieldsofstudy, isFetching} = this.props.fieldofstudy;
    if(Array.from(currentfieldsofstudy).length >0){
      var current_fields = Array.from(currentfieldsofstudy).map((anObjectMapped, index) => {
        return (
        <option key={anObjectMapped.fieldofstudyname +'/'+anObjectMapped.onSemester+'/'+anObjectMapped.startYears+'/'+anObjectMapped.faculty} value={anObjectMapped.fieldofstudyname +'/'+anObjectMapped.onSemester+'/'+anObjectMapped.startYears+'/'+anObjectMapped.faculty}>{anObjectMapped.fieldofstudyname +'/'+anObjectMapped.onSemester+'/'+anObjectMapped.startYears+'/'+anObjectMapped.faculty}</option>  
        );})
    }
    else{var current_fields = null;}
    // if(this.state.addfaculty!=='' || possiblefieldsofstudies){
    //   var possible_fieldsofstudy = Array.from(possiblefieldsofstudies).map((anObjectMapped, index) => {
    //     return (
    //     <option key={anObjectMapped.faculty} value={anObjectMapped.faculty}>{anObjectMapped.faculty}</option>  
    //     );})
    // }
    // else{var possible_fieldsofstudy=null;}

  //   if(this.state.faculty==='Wydział Elektrotechniki, Automatyki, Informatyki i Inżynierii Biomedycznej'){
  //     fieldOfStudy = <div>
  //    <label for="fieldofstudy-select">Wybierz kierunek:</label>
  //     <select name="fieldofstudy" id="fieldofstudy-select" onChange={this.onChange.bind(this, 'fieldofstudy')}>
  // <option value="Informatyka">Informatyka</option>
  // <option value="Automatyka i Robotyka">Automatyka i Robotyka</option>
  // <option value="Inżynieria Biomedyczna">Inżynieria Biomedyczna</option>
  //   </select>
  //   </div>
  //   }

    return (
      <div>
         <div>
<div className="row">
          <div className="small-12 columns">
            <div className="nt-box">
              <div className="nt-box-title">
              Obecne kierunki studiów
              <p>Usuń dodany kierunek studiów.</p>
              </div>
              <select name="delete" id="delete-select" onClick={this.deleteSelect}>
    {current_fields}
			</select>
      <div className="row text-center">
              <button className="btn"
                      type="submit"
                      name="submit-login"
                      onClick={this.deleteFieldofstudy}
                      disabled={!this.state.canDelete}>
                Usuń kierunek studiów
              </button>
            </div>
              </div>
            </div>
          </div>
        </div>
        <p></p>
<div className="row">
          <div className="small-12 columns">
            <div className="nt-box">
              <div className="nt-box-title">
                Dodaj nowy kierunek
                <p>Dodaj kierunek studiów wybierając wydział, nazwę kierunku, rok akademicki rozpoczęcia oraz numer semestru, na którym jesteś.</p>
              </div>
              <div className="nt-box-row">

              <div>
      <div>
      <label for="faculty-select">Wybierz wydział:</label>
      <select name="faculty" id="faculty-select" onClick={this.changeFaculty}>
      {this.state.possible_faculties}
    </select>
    </div>
    <div>
      <label for="fieldofstudy-select">Wybierz kierunek:</label>
       <select name="fieldofstudy" id="fieldofstudy-select" onClick={this.changeField}>
   {this.state.possible_fieldsofstudy}
     </select>
     </div>

     <div>
      <label for="fieldofstudy-select">Wybierz rok akademicki rozpoczęcia:</label>
       <select name="startyear" id="fieldofstudy-select" onClick={this.changeStartYear}>
   {this.state.possible_startyears}
     </select>
     </div>
     <div>
     <label for="on_semester-select">Wybierz numer semesteru, na którym jesteś:</label>
      <select name="on_semester" id="on_semester-select" onClick={this.changeSemesterNumber}>
      <option value="1">1</option> <option value="2">2</option> <option value="3">3</option> <option value="4">4</option><option value="5">5</option><option value="6">6</option><option value="7">7</option>
    </select>
    </div>
    <div>Nowy kierunek: {this.state.addfieldofstudy}/{this.state.addon_semester}/{this.state.addstartyears}/{this.state.addfaculty}</div>
    <div className="row text-center">
              <button className="btn"
                      type="submit"
                      name="submit-login"
                      onClick={this.addFieldOfStudy}
                      disabled={!this.state.canAdd}>
                Dodaj kierunek studiów
              </button>
            </div>
    
     </div>

              </div>
            </div>
          </div>
        </div> 
        </div>
    
    );
  }

  changeFaculty(event){
    event.preventDefault();
    this.props.getPossibleFaculties();
    var {errors, possiblefaculties, possiblefieldsofstudies, isFetching} = this.props.fieldofstudy;
    var possible_faculties = Array.from(possiblefaculties).map((anObjectMapped, index) => {
      return (
      <option key={anObjectMapped.faculty} value={anObjectMapped.faculty}>{anObjectMapped.faculty}</option>  
      );})
    this.setState({
      addfaculty: event.target.value,
      addfieldofstudy:'',
      addstartyears:'',
      addon_semester:'',
      canAdd:false,
      possible_faculties:possible_faculties,
      possible_fieldsofstudy:null,
      possible_startyears:null,
    });
  }

  changeField(event){
    event.preventDefault();
    if(event.target.name === "fieldofstudy" && this.state.addfaculty){
    var faculty = this.state.addfaculty;
    this.props.getPossibleFieldsofstudy({faculty})
    var {errors, possiblefaculties, possiblefieldsofstudies, isFetching} = this.props.fieldofstudy;
    var possible_fieldsofstudy = Array.from(possiblefieldsofstudies).map((anObjectMapped, index) => {
      return (
      <option key={anObjectMapped.fieldofstudy} value={anObjectMapped.fieldofstudy}>{anObjectMapped.fieldofstudy}</option>  
      );})
    this.setState({
      addfieldofstudy:event.target.value,
      addstartyears:'',
      addon_semester:'',
      canAdd:false,
      possible_fieldsofstudy:possible_fieldsofstudy,
      possible_startyears:null,
    })
  }
  }

  changeStartYear(event){
    event.preventDefault();
    if( this.state.addfaculty && this.state.addfieldofstudy ){
    var faculty = this.state.addfaculty;
    var fieldofstudyname = this.state.addfieldofstudy;
    this.props.getPossibleStartYearsForFieldsofstudy({faculty, fieldofstudyname})
    var {errors, possiblefaculties, possiblefieldsofstudies, possiblestartyears, isFetching} = this.props.fieldofstudy;
    var possible_startyears = Array.from(possiblestartyears).map((anObjectMapped, index) => {
      return (
      <option key={anObjectMapped.years} value={anObjectMapped.years}>{anObjectMapped.years}</option>  
      );})
    this.setState({
      addstartyears:event.target.value,
      addon_semester:'',
      canAdd:false,
      possible_startyears:possible_startyears
    })
  }
  }

  changeSemesterNumber(event){
    event.preventDefault();
    if(this.state.addfaculty && this.state.addfieldofstudy && this.state.addstartyears){
    var canAdd =  this.state.addon_semester && this.state.addstartyears && this.state.addfieldofstudy && this.state.addfaculty
    this.setState({
      addon_semester:event.target.value,
      canAdd:canAdd
    })
  }
  }

  addFieldOfStudy(event){
    event.preventDefault();
    var faculty = this.state.addfaculty;
    var fieldofstudyname = this.state.addfieldofstudy;
    var startyears = this.state.addstartyears;
    var on_semester = this.state.addon_semester;
    this.props.connectUserWithFieldofstudy({faculty, fieldofstudyname, startyears, on_semester})
    this.props.getUserFieldsOfStudy();
  }

  deleteFieldofstudy(event){
    event.preventDefault();
    var faculty = this.state.deletefaculty
    var fieldofstudyname = this.state.deletefieldofstudy
    var startyears = this.state.deletestartyears
    var on_semester = this.state.deleteon_semester
    this.props.disconnectUserWithFieldofstudy({faculty, fieldofstudyname, startyears, on_semester})
    this.props.getUserFieldsOfStudy();
  }

  deleteSelect(event){
    event.preventDefault();
    this.props.getUserFieldsOfStudy();
    if(event.target.value !== ''){
    var fields = event.target.value.split('/');
    var faculty = fields[3]
    var fieldofstudyname = fields[0]
    var startyears = fields[2]
    var on_semester = fields[1]
      this.setState({
      deletefaculty: faculty,
      deletefieldofstudy: fieldofstudyname,
      deletestartyears:startyears,
      deleteon_semester: on_semester,
        canDelete: faculty && fieldofstudyname && startyears && on_semester
      })
    }
  }
  
}


FieldOfStudy.displayName = 'FieldOfStudy';

FieldOfStudy.propTypes = {
  possiblefaculties: PropTypes.object
};

function mapDispatchToProps(dispatch) {
  return bindActionCreators(Actions, dispatch);
}

function mapStateToProps(state) {
  return {
    fieldofstudy: _.get(state, 'fieldofstudy'),
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(ValidatedComponent(withRouter(FieldOfStudy)));
