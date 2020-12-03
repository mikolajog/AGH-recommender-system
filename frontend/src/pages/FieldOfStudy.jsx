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

class FieldOfStudy extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      faculty: '',
      fieldofstudy: '',
      on_semester: '',
      fieldsofstudies:this.props,
      canSubmit: true
    };

    this.addFieldOfStudy = this.addFieldOfStudy.bind(this);
    this.onChange = this.onChange.bind(this);
    
  }

  onChange(fieldName, e) {
    this.setState({[fieldName]: e.target.value});

  }

  componentDidMount() {
    this.props.getFieldsOfStudy();
  }


  render() {

    let fieldOfStudy;
    var {errors, field, isFetching} = this.props.user;
    var{fieldofstudy, status} = field;

    if(this.state.faculty==='Wydział Elektrotechniki, Automatyki, Informatyki i Inżynierii Biomedycznej'){
      fieldOfStudy = <div>
     <label for="fieldofstudy-select">Wybierz kierunek:</label>
      <select name="fieldofstudy" id="fieldofstudy-select" onChange={this.onChange.bind(this, 'fieldofstudy')}>
  <option value="Informatyka">Informatyka</option>
  <option value="Automatyka i Robotyka">Automatyka i Robotyka</option>
  <option value="Inżynieria Biomedyczna">Inżynieria Biomedyczna</option>
    </select>
    </div>
    }

    return (
      <div>
        <div>
<div className="row">
          <div className="small-12 columns">
            <div className="nt-box">
              <div className="nt-box-title">
              Obecne kierunki studiów
              </div>
              <select>
              <option key='dsdf' value='val'>{fieldofstudy}</option>
			</select>
      <div className="row text-center">
              <button className="btn"
                      type="submit"
                      name="submit-login"
                      onClick={this.addFieldOfStudy}
                      disabled={this.canSubmit}>
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
              </div>
              <div className="nt-box-row">

              <div>
      <div>
     <label for="on_semester-select">Wybierz numer semesteru, na którym jesteś:</label>
      <select name="on_semester" id="on_semester-select" onChange={this.onChange.bind(this, 'on_semester')}>
  <option value="1">1</option>
  <option value="2">2</option>
  <option value="3">3</option>
  <option value="4">4</option>
  <option value="5">5</option>
  <option value="6">6</option>
  <option value="7">7</option>
  <option value="8">8</option>
  <option value="9">9</option>
  <option value="10">10</option>
    </select>
    </div>
      <div>
      <label for="faculty-select">Wybierz wydział:</label>
      <select name="faculty" id="faculty-select" onChange={this.onChange.bind(this, 'faculty')}>
      <option value="">--Wybierz wydział--</option>
  <option value="Wydział Elektrotechniki, Automatyki, Informatyki i Inżynierii Biomedycznej">Wydział Elektrotechniki, Automatyki, Informatyki i Inżynierii Biomedycznej</option>
  <option value="Wydział Wiertnictwa, Nafty i Gazu">Wydział Wiertnictwa, Nafty i Gazu</option>
  <option value="Wydział Zarządzania">Wydział Zarządzania</option>
    </select>
    </div>
    {fieldOfStudy}
    <div className="row text-center">
              <button className="btn"
                      type="submit"
                      name="submit-login"
                      onClick={this.addFieldOfStudy}
                      disabled={this.canSubmit}>
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
  addFieldOfStudy(event){
    event.preventDefault();
    var {faculty, fieldofstudy, on_semester} = this.state
    if (this.props.isComponentValid()) {
      this.props.addFieldOfStudy({faculty, fieldofstudy, on_semester});
      this.props.getFieldsOfStudy();
    }
  }
}


FieldOfStudy.displayName = 'FieldOfStudy';

FieldOfStudy.propTypes = {
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

export default connect(mapStateToProps, mapDispatchToProps)(ValidatedComponent(withRouter(FieldOfStudy)));
