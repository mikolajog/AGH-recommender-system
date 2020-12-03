import settings from '../config/settings';
import axios from './axios';
import UserSession from '../UserSession';

const {apiBaseURL} = settings;

export default class ProfileApi {

  static getProfile() {
    var token =  UserSession.getToken()
    return axios.post(`${apiBaseURL}/users/me`, {token});
  }

  static getProfileRatings() {
    return axios.get(`${apiBaseURL}/movies/rated`);
  }

  static getProfileRecommendations() {
    return axios.get(`${apiBaseURL}/movies/recommended`);
  }
}
