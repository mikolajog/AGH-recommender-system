import settings from '../config/settings';
import axios from './axios';
import UserSession from '../UserSession';

const {apiBaseURL} = settings;
var token = UserSession.getToken();

export default class KeywordsApi {
  static getKeywords() {
    return axios.get(`${apiBaseURL}/keywords/get/me/${token}`);
  }

  static addKeyword({word}) {
    return axios.post(`${apiBaseURL}/keywords/add`,{token, word});
  }

  static deleteKeyword({word}) {
    return axios.delete(`${apiBaseURL}/keywords/delete/${token}/${word}`);
  }
}
