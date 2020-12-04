import settings from '../config/settings';
import axios from './axios';
import UserSession from '../UserSession';

const {apiBaseURL} = settings;
var token = UserSession.getToken();

export default class FieldofstudyApi {
  static getPossibleFaculties() {
    return axios.get(`${apiBaseURL}/fieldofstudy/get/faculty`);
  }

  static getPossibleFieldsofstudy({payload}) {
    return axios.get(`${apiBaseURL}/fieldofstudy/get/${payload.faculty}/fieldofstudynames`);
  }

  static getPossibleStartYearsForFieldsofstudy({payload}) {
    return axios.get(`${apiBaseURL}/fieldofstudy/get/startyears/${payload.faculty}/${payload.fieldofstudyname}`);
  }

  static getUserFieldsOfStudy() {
    return axios.get(`${apiBaseURL}/fieldofstudy/get/me/${token}`);
  }

  static connectUserWithFieldofstudy({payload}) {
    var fieldofstudy = payload;
    return axios.post(`${apiBaseURL}/fieldofstudy/connect/me`,{token, fieldofstudy});
  }

  static disconnectUserWithFieldofstudy(payload) {
    var fieldofstudy = payload.payload;
    return axios.post(`${apiBaseURL}/fieldofstudy/disconnect/me`,{token, fieldofstudy});
  }

  static getProfile() {
    var token =  UserSession.getToken()
    return axios.get(`${apiBaseURL}/user/get/me/${token}`);
  }
}
