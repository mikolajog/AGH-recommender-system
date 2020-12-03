import settings from '../config/settings';
import axios from './axios';
import UserSession from '../UserSession';

const {apiBaseURL} = settings;
var api_key = UserSession.getToken();

export default class UserApi {
  static addFieldOfStudy({faculty, fieldofstudy, on_semester}) {
    return axios.post(`${apiBaseURL}/users/me/add/fieldofstudy`, {api_key, faculty, fieldofstudy, on_semester});
  }

  static getFieldsOfStudy() {
    return axios.get(`${apiBaseURL}/users/'${api_key}'/get/fieldsofstudy`);
  }
}