import React from 'react';
import { Link } from 'react-router-dom';
import Loading from '../components/Loading.jsx';
import Carousel from '../components/Carousel.jsx';
import _ from 'lodash';
import AuthenticatedPage from './AuthenticatedPage.jsx';
import UserRating from '../components/UserRating.jsx';
import * as ProfileActions from '../redux/actions/ProfileActions';
import InputValidator from '../components/validation/InputValidator.jsx';

import * as MovieActions from '../redux/actions/MovieActions';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';

class Home extends React.Component {
  constructor() {
    super();
    this.state = {
      index_number: '',
      password: '',
      canSubmit: false,
      errors:{},
      fieldofstudy: [{name: 'Informatyka'}, {name:'Automatyka'}]
    };

  }

  componentWillMount() {
  }

  render() {
    var {index_number, password, canSubmit} = this.props;
    var {errors} = this.props;
    var {fieldofstudy} = this.state;
    let fieldsofstudyList = fieldofstudy.length > 0
		&& fieldofstudy.map((item, i) => {
		return (
			<option key={i} value={item.name}>{item.name}</option>
		)
	}, this);
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
                              errors={errors}
                              shouldValidateOnBlur={true}>
                Numer indeksu:
                <input type="text"
                       name="index_number"
                       placeholder="Mkołaj Ogarek*"
                       required
                       value={index_number}
                       onChange={this.changeUser}
                       disabled={true}/>
              </InputValidator>
              </div>
            </div>
            <div className="row">
              <div className="small-12 medium-10 large-10 columns">
              <InputValidator fieldName="Numer indeksu"
                              errors={errors}
                              shouldValidateOnBlur={true}>
                Imię i nazwisko:
                <input type="text"
                       name="index_number"
                       placeholder="Mkołaj Ogarek*"
                       required
                       value={index_number}
                       onChange={this.changeUser}
                       disabled={true}/>
              </InputValidator>
              </div>
            </div>
            <div className="row">
              <div className="small-12 medium-10 large-10 columns">
              <InputValidator fieldName="Numer indeksu"
                              errors={errors}
                              shouldValidateOnBlur={true}>
                E-mail:
                <input type="text"
                       name="index_number"
                       placeholder="Mkołaj Ogarek*"
                       required
                       value={index_number}
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
    <select>
				{fieldsofstudyList}
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
} 
Home.displayName = 'Home';

function mapStateToProps(state) {
  return {
    // genres: state.genres.items,

    // movies: state.movies
  };
}

function mapDispatchToProps(dispatch) {
  return bindActionCreators(MovieActions, dispatch);
}

// Wrap the component to inject dispatch and state into it
export default connect(mapStateToProps, mapDispatchToProps)(Home);
