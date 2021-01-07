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
      recon_semester: '',
      mode:'',
    };
    this.changefieldofstudy = this.changefieldofstudy.bind(this);
    this.getIndividualRecom = this.getIndividualRecom.bind(this);
    this.getHybridRecom = this.getHybridRecom.bind(this);
    this.getTeamRecom = this.getTeamRecom.bind(this);
  }

  componentDidMount(){ 
    if(UserSession.getToken()===null){this.props.history.push('/login');}
    else{this.props.getProfile();}
    this.props.getProfile();
  }

  render() {
    var recommendations = null;
    var {recommendations} = this.props.fieldofstudy;
    if(Array.isArray(recommendations)){
      var current_rec = Array.from(recommendations).map((anObjectMapped, index) => {
        return (
        <li>{anObjectMapped.name} - {anObjectMapped.rating}%</li>
        );})
      }
    const {apiBaseURL} = settings;
    if(UserSession.getToken()===null){this.props.history.push('/login');}
    var {name, indexNumber, email} = this.props.fieldofstudy.profile;
    var {index_number, password, canSubmit} = this.props;
    var {errors} = this.props;
    var {fieldofstudy} = this.state;
    var currentfieldsofstudy=[];
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
      <p>W celu rekomendacji przedmiotów uzupełnij dane w zakładkach: 
      <ul>
        <li><Link to="/fieldofstudy" >Kierunki studiów</Link></li>
        <li><Link to="/keywords" >Słowa kluczowe</Link></li>
        <li><Link to="/coursesratings" >Oceny przedmiotów</Link></li>
        <li><Link to="/professorsratings" >Oceny Profesorów</Link></li>
      </ul>
      Wybierz kierunek studiów oraz sposób rekomendacji!
      <ul>
        <li>Indywidualny - rekomendacja tylko na podstawie własnego profilu</li>
        <li>Zespołowy - rekomendacja z wykorzystaniem danych innych użytkowników</li>
        <li>Mieszany - rekomendacja z użyciem danych własnego profilu oraz danych innych użytkowników</li>
        </ul> </p>
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
                      onClick={this.getIndividualRecom}
                      disabled={!this.state.canSubmit}>
                Indywidualny
              </button>
&nbsp;
              <button className="btn"
                      type="submit"
                      name="submit-login"
                      onClick={this.getHybridRecom}
                      disabled={!this.state.canSubmit}>
                Mieszany
              </button>
              &nbsp;
              <button className="btn"
                      type="submit"
                      name="submit-login"
                      onClick={this.getTeamRecom}
                      disabled={!this.state.canSubmit}>
                Zespołowy
              </button>
            </div>
    <div><ol>{current_rec}</ol></div>
    </div>
  </div>
    </div>
  </div>
</div>
</div>
</div>
      );
  }
  getIndividualRecom(event){
    var {currentfieldsofstudy} = this.props.fieldofstudy;
    var mode = "individual";
    var faculty = this.state.recfaculty;
    var fieldofstudy = this.state.recfieldofstudy;
    var startyears = this.state.recstartyears;
    var onsemester = this.state.recon_semester;

    this.props.getRecommendations({currentfieldsofstudy, faculty, fieldofstudy, startyears, onsemester, mode})
  }
  getHybridRecom(event){
    var {currentfieldsofstudy} = this.props.fieldofstudy;
    var mode = "hybrid";
    var faculty = this.state.recfaculty;
    var fieldofstudy = this.state.recfieldofstudy;
    var startyears = this.state.recstartyears;
    var onsemester = this.state.recon_semester;
    this.props.getRecommendations({currentfieldsofstudy, faculty, fieldofstudy, startyears, onsemester, mode})
  }
  getTeamRecom(event){
    var {currentfieldsofstudy} = this.props.fieldofstudy;
    var mode = "team";
    var faculty = this.state.recfaculty;
    var fieldofstudy = this.state.recfieldofstudy;
    var startyears = this.state.recstartyears;
    var onsemester = this.state.recon_semester;
    this.setState({
      mode:"Proszę czekać..."
      })
    this.props.getRecommendations({currentfieldsofstudy, faculty, fieldofstudy, startyears, onsemester, mode})
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
      canSubmit: faculty!=='' && fieldofstudyname!=='' && startyears!=='' && on_semester!==''
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
