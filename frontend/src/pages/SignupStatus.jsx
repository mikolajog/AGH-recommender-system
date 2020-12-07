import _ from 'lodash';
import React from 'react';
import PropTypes from 'prop-types';
import {Link} from 'react-router-dom';
import {createProfileInit} from '../redux/actions/ProfileActions';
import {connect} from 'react-redux';

class SignupStatus extends React.Component {
  componentWillMount() {
    
  }

  componentWillUnmount() {
  }

  render() {
    var {profile} = this.props;

    return (
      <div>
      <p>You have successfully created an account.</p>
                <div>
                  <Link to="/" className="button ba-default-btn">Homepage</Link>
                </div>
                </div>
    );
  }
}

SignupStatus.displayName = 'SignupStatus';
SignupStatus.contextTypes = {
  router: PropTypes.object.isRequired
};

function mapStateToProps(state) {
  return {
    profile: _.get(state.signup, 'savedProfile')
  };
}

export default connect(mapStateToProps)(SignupStatus);
