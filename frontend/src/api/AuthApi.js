import settings from '../config/settings';
import axios from './axios';

const {apiBaseURL} = settings;

export default class AuthApi {
  static login(index_number, password) {
    return axios.post(`${apiBaseURL}/login`, {index_number, password});
  }

  static register(profile) {
    return axios.post(`${apiBaseURL}/register`, profile);
  }
}
