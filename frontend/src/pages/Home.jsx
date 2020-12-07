import React from 'react';
import { Link} from 'react-router-dom';
import {BrowserRouter as Redirect} from 'react-router-dom';
import Loading from '../components/Loading.jsx';
import Carousel from '../components/Carousel.jsx';
import _ from 'lodash';
import AuthenticatedPage from './AuthenticatedPage.jsx';
import * as ProfileActions from '../redux/actions/ProfileActions';
import InputValidator from '../components/validation/InputValidator.jsx';
import {getProfile} from '../redux/actions/ProfileActions';

import * as Actions from '../redux/actions/FieldofstudyActions';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import UserSession from '../UserSession.js';
import settings from '../config/settings';



class Home extends React.Component {
  constructor() {
    super();
    this.state = {
      index_number: '',
      password: '',
      canSubmit: false,
      errors:{},
      recfaculty: '',
      recfieldofstudy: '',
      recstartyears:'',
      recon_semester: ''
    };
    this.changefieldofstudy = this.changefieldofstudy.bind(this);
  }

  componentDidMount(){ 
    if(UserSession.getToken()===null){this.props.history.push('/login');}
    else{this.props.getProfile();}
  }

  render() {
    const {apiBaseURL} = settings;
    if(UserSession.getToken()===null){this.props.history.push('/login');}
    var {name, indexNumber, email} = this.props.fieldofstudy.profile;
    var {index_number, password, canSubmit} = this.props;
    var {errors} = this.props;
    var {fieldofstudy} = this.state;
    var {errors, possiblefaculties, possiblefieldsofstudies,currentfieldsofstudy, isFetching} = this.props.fieldofstudy;
    if(Array.from(currentfieldsofstudy).length >0){
      var current_fields = Array.from(currentfieldsofstudy).map((anObjectMapped, index) => {
        return (
        <option key={anObjectMapped.fieldofstudyname +'/'+anObjectMapped.onSemester+'/'+anObjectMapped.startYears+'/'+anObjectMapped.faculty} value={anObjectMapped.fieldofstudyname +'/'+anObjectMapped.onSemester+'/'+anObjectMapped.startYears+'/'+anObjectMapped.faculty}>{anObjectMapped.fieldofstudyname +'/'+anObjectMapped.onSemester+'/'+anObjectMapped.startYears+'/'+anObjectMapped.faculty}</option>  
        );})
    }
    else{var current_fields = null;}
    return (
      <div>
<div className="row">
          <div className="small-12 columns">
            <div className="nt-box">
              <div className="nt-box-title">
                Mój profil
              </div>
              <div className="nt-box-row">
              <div className="row">
              <div className="small-12 medium-10 large-10 columns">
              <InputValidator fieldName="Numer indeksu"
                              
                              shouldValidateOnBlur={false}>
                Numer indeksu:
                <input type="text"
                       name="index_number"
                       placeholder={indexNumber}
                       
                       value={indexNumber}
                       onChange={this.changeUser}
                       disabled={true}/>
              </InputValidator>
              </div>
            </div>
            <div className="row">
              <div className="small-12 medium-10 large-10 columns">
              <InputValidator fieldName="Imie"
                              
                              shouldValidateOnBlur={false}>
                Imię i nazwisko:
                <input type="text"
                       name="index_number"
                       placeholder={name}
                       
                       value={name}
                       onChange={this.changeUser}
                       disabled={true}/>
              </InputValidator>
              </div>
            </div>
            <div className="row">
              <div className="small-12 medium-10 large-10 columns">
              <InputValidator fieldName="Mail"
                              
                              shouldValidateOnBlur={false}>
                E-mail:
                <input type="text"
                       name="index_number"
                       placeholder={email}
                  
                       value={email}
                       onChange={this.changeUser}
                       disabled={true}/>
              </InputValidator>
              </div>
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
      Rekomendacje
    </div>
    <div className="nt-box-row">
    <div className="row">
    <div className="small-12 medium-10 large-10 columns">
    <select name="field" id="fieldofstudy-select" onClick={this.changefieldofstudy}>
				{current_fields}
			</select>
    </div>
  </div>
  <div className="row">
    <div className="small-12 medium-10 large-10 columns">
    <div className="row text-center">
              <button className="btn"
                      type="submit"
                      name="submit-login"
                      onClick={this.login}
                      disabled={!canSubmit}>
                Indywidualny
              </button>
&nbsp;
              <button className="btn"
                      type="submit"
                      name="submit-login"
                      onClick={this.login}
                      disabled={!canSubmit}>
                Hybrydowy
              </button>
              &nbsp;
              <button className="btn"
                      type="submit"
                      name="submit-login"
                      onClick={this.login}
                      disabled={!canSubmit}>
                Zespołowy
              </button>
            </div>
    </div>
  </div>
    </div>
  </div>
</div>
</div>
</div>
      );
  }

  changefieldofstudy(event){
    this.props.getUserFieldsOfStudy();
    var fields = event.target.value.split('/');
    var faculty = fields[3]
    var fieldofstudyname = fields[0]
    var startyears = fields[2]
    var on_semester = fields[1]
      this.setState({
      recfaculty: faculty,
      recfieldofstudy: fieldofstudyname,
      recstartyears:startyears,
      recon_semester: on_semester,
        canSubmit: faculty && fieldofstudyname && startyears && on_semester
      })
  }
} 
Home.displayName = 'Home';

function mapStateToProps(state) {
  return {
    fieldofstudy: _.get(state, 'fieldofstudy'),
  };
}

function mapDispatchToProps(dispatch) {
  return bindActionCreators(Actions, dispatch);
}

// Wrap the component to inject dispatch and state into it
export default connect(mapStateToProps, mapDispatchToProps)(Home);
