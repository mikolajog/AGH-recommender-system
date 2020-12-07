import React from 'react';
import {Route} from 'react-router';
import App from '../pages/App.jsx';
import Home from '../pages/Home.jsx';
import Login from '../pages/Login.jsx';
import Signup from '../pages/Signup.jsx';
import SignupStatus from '../pages/SignupStatus.jsx';
import FieldOfStudy from '../pages/FieldOfStudy.jsx';
import Keywords from '../pages/Keywords.jsx';
import ProfessorsRatings from '../pages/ProfessorsRatings.jsx';
import CoursesRatings from '../pages/CoursesRatings.jsx';
export default class Routes extends React.Component {
  render() {
    return (
      <App>
        <Route exact path="/" component={Home}/>
        <Route path="/fieldofstudy" component={FieldOfStudy}/>
        <Route path="/keywords" component={Keywords}/>
        <Route path="/professorsratings" component={ProfessorsRatings}/>
        <Route path="/coursesratings" component={CoursesRatings}/>
        <Route path="/login" component={Login}/>
        <Route path="/signup" component={Signup}/>
        <Route path="/signup-status" component={SignupStatus}/>
      </App>
    );
  }
}

Routes.displayName = 'Routes';
