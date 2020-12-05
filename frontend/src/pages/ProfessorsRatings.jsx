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

class ProfessorsRatings extends React.Component {
  constructor() {
    super();
    this.state = {
      errors:{}
    }

  }

  componentDidMount() {
    const {apiBaseURL} = settings;
    if(UserSession.getToken()===null){this.props.history.push('/login');}
    
  }

  render() {
    return (
      <div>
<div className="row">
          <div className="small-12 columns">
            <div className="nt-box">
              <div className="nt-box-title">
              ProfessorsRatings
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
    user: _.get(state, 'user'),
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(ValidatedComponent(withRouter(ProfessorsRatings)));
