import settings from '../config/settings';
import axios from './axios';
import UserSession from '../UserSession';

const {apiBaseURL} = settings;

export default class ProfileApi {

  static getProfile() {
    var token =  UserSession.getToken()
    return axios.get(`${apiBaseURL}/user/get/me/${token}`);
  }
}
