import React from 'react';
import PropTypes from 'prop-types';
import {withRouter} from 'react-router';
import {Link} from 'react-router-dom';
import InputValidator from '../components/validation/InputValidator.jsx';
import ValidatedComponent from '../components/validation/ValidatedComponent.jsx';
import * as Actions from '../redux/actions/AuthActions';
import {bindActionCreators} from 'redux';
import {connect} from 'react-redux';

class Login extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      index_number: '',
      password: '',
      canSubmit: false
    };

    this.popup = null;

    this.changeUser = this.changeUser.bind(this);
    this.changePassword = this.changePassword.bind(this);
    this.login = this.login.bind(this);
    this.redirectIfAuthed = this.redirectIfAuthed.bind(this);
  }

  login(e) {
    e.preventDefault();
    if (this.props.isComponentValid()) {
      this.props.login(this.state.index_number, this.state.password);
    }
  }

  componentDidMount() {
    this.redirectIfAuthed(this.props);
  }

  componentWillReceiveProps(nextProps) {
    this.redirectIfAuthed(nextProps);
  }

  redirectIfAuthed(props) {
    var {token, match, history} = props;
    if (token) {
      if (match.params.redirectTo) {
        history.push(match.params.redirectTo);
      }
      else {
        history.push('/');
      }
    }
  }

  render() {
    var {index_number, password, canSubmit} = this.state;
    var {errors} = this.props;

    return (
      <div className="ba-login row">
        <form noValidate>
          <div className="panel small-12 small-centered columns">
            <div className="row panel-title">
              <h3>Logowanie</h3>
            </div>
            <div className="row">
              <InputValidator fieldName="Numer indeksu"
                              errors={errors.username}
                              shouldValidateOnBlur={true}>
                <input type="indexnumber"
                       name="index_number"
                       placeholder="Numer indeksu*"
                       required
                       value={index_number}
                       onChange={this.changeUser}/>
              </InputValidator>
            </div>
            <div className="row">
              <InputValidator fieldName="Hasło"
                              errors={errors.data}
                              shouldValidateOnBlur={true}>
                <input type="password"
                       name="password"
                       placeholder="Hasło:*"
                       required
                       value={password}
                       onChange={this.changePassword}/>
              </InputValidator>
            </div>
            <div className="row text-center">
              <button className="btn"
                      type="submit"
                      name="submit-login"
                      onClick={this.login}
                      disabled={!canSubmit}>
                Zaloguj
              </button>
            </div>
            <div className="row text-center">
              <Link to="/signup">Utwórz konto</Link>
            </div>
          </div>
        </form>
      </div>
    );
  }

  changeUser(event) {
    var canSubmit = this.state.index_number && event.target.value;
    this.setState({
      index_number: event.target.value,
      canSubmit: canSubmit
    });
  }

  changePassword(event) {
    var canSubmit = this.state.password && event.target.value;
    this.setState({
      password: event.target.value,
      canSubmit: canSubmit
    });
  }
}

Login.displayName = 'Login';

Login.propTypes = {
  query: PropTypes.object
};

function mapDispatchToProps(dispatch) {
  return bindActionCreators(Actions, dispatch);
}

function mapStateToProps(state) {
  return {...state.auth};
}

export default connect(mapStateToProps, mapDispatchToProps)(ValidatedComponent(withRouter(Login)));
