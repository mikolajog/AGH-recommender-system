import React from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';

export default class Breadcrumbs extends React.Component {
  render() {
    var {movie, person} = this.props;

    return (
      <ul className="breadcrumbs">
        <li><Link to="/" >Główna</Link></li>
        <li><Link to="/fieldofstudy" >Kierunki studiów</Link></li>
        <li><Link to="/keywords" >Słowa kluczowe</Link></li>
        <li><Link to="/coursesratings" >Oceny przedmiotów</Link></li>
        <li><Link to="/professorsratings" >Oceny Profesorów</Link></li>
      </ul>
    );
  }
}

Breadcrumbs.displayName = 'Breadcrumbs';
Breadcrumbs.propTypes = {
  movie: PropTypes.object,
  person: PropTypes.object
};
