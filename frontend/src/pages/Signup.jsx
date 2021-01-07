import React from 'react';
import { withRouter } from 'react-router';
import validatedComponent from '../components/validation/ValidatedComponent.jsx';
import InputValidator from '../components/validation/InputValidator.jsx';
import * as Actions from '../redux/actions/ProfileActions';
import {bindActionCreators} from 'redux';
import {connect} from 'react-redux';

class Signup extends React.Component {
  constructor() {
    super();

    this.state = {
      index_number: '',
      name: '',
      email: '',
      password: '',
      canSubmit:false
    };

    this.createUser = this.createUser.bind(this);
    this.validateConfirmPassword = this.validateConfirmPassword.bind(this);
  }

  componentDidMount() {
    this.redirectIfAuthed(this.props);
  }

  componentWillReceiveProps(nextProps) {
    this.redirectIfAuthed(nextProps);
  }

  redirectIfAuthed(props) {
    var {match, history, auth} = props;
    if (auth.token) {
      if (match.params.redirectTo) {
        history.push(match.params.redirectTo);
      }
      else {
        history.push('/');
      }
    }
  }

  createUser(event) {
    event.preventDefault();
    var {index_number, name, email, password} = this.state;

    if (this.props.isComponentValid()) {
      this.props.createProfile({index_number, name, email, password});
    }
  }

  onChange(fieldName, e) {
    this.setState({[fieldName]: e.target.value});
  }

  validateConfirmPassword() {
    var {password, confirmPassword} = this.state;
    if (password !== confirmPassword) {
      return 'Both passwords must be equal';
    }
      var canSubmit = this.state.password && this.state.name;
      this.setState({
      canSubmit: canSubmit
    });
  }

  render() {
    var {state} = this;
    var {errors} = this.props;
    return (
      <div className="ba-signup row">
        <form noValidate>
          <div className="panel small-12 small-centered columns">
            <div className="row panel-title">
              <h3>Utwórz konto</h3>
            </div>
            <div className="row">
              <InputValidator fieldName="Numer indeksu"
                              errors={errors.indexnumber}
                              shouldValidateOnBlur={true}>
              <input type="indexnumber"
                     name="indexnumber"
                     required
                     placeholder="Numer indeksu*"
                     value={state.index_number}
                     onChange={this.onChange.bind(this, 'index_number')}/>
              </InputValidator>
            </div>
            <div className="row">
              <InputValidator fieldName="Imię i nazwisko"
                              errors={errors.name}
                              shouldValidateOnBlur={true}>
              <input type="names"
                     name="name-surname"
                     required
                     placeholder="Imię i nazwisko*"
                     value={state.name}
                     onChange={this.onChange.bind(this, 'name')}/>
              </InputValidator>
            </div>
            <div className="row">
              <InputValidator fieldName="E-mail"
                              errors={errors.name}
                              shouldValidateOnBlur={true}>
              <input type="email"
                     name="email"
                     required
                     placeholder="Adres e-mail*"
                     value={state.email}
                     onChange={this.onChange.bind(this, 'email')}/>
              </InputValidator>
            </div>
            <div className="row">
              <input type="password"
                     name="password"
                     placeholder="Hasło*"
                     required
                     onChange={this.onChange.bind(this, 'password')}
                     value={state.password}/>
            </div>
            <div className="row">
              <InputValidator fieldName="Password"
                              errors={errors.password}
                              shouldValidateOnBlur={true}
                              customValidation={() => {return this.validateConfirmPassword();}}>
              <input type="password"
                     name="password-confirm"
                     placeholder="Potwierdź hasło*"
                     required
                     onChange={this.onChange.bind(this, 'confirmPassword')}
                     value={state.confirmPassword}/>
              </InputValidator>
            </div>
            <div className="row text-center">
              <button type="button"
                      name="btn-create"
                      className="ba-default-button"
                      onClick={this.createUser}
                      disabled={!this.state.canSubmit}>
                      
                Utwórz konto
              </button>
            </div>
          </div>
        </form>
        <div className="push"/>
      </div>
    );
  }
}

Signup.displayName = 'Signup';

function mapDispatchToProps(dispatch) {
  return bindActionCreators(Actions, dispatch);
}

function mapStateToProps(state) {
  return {...state.signup,  auth: {...state.auth}};
}

export default connect(mapStateToProps, mapDispatchToProps)(validatedComponent(withRouter(Signup)));
