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
    var token =  UserSession.getToken();
    return axios.get(`${apiBaseURL}/user/get/me/${token}`);
  }

  static getCourses({payload}) {
    var token =  UserSession.getToken();
    return axios.get(`${apiBaseURL}/courses/get/me/${token}/${payload.faculty}/${payload.fieldofstudy}/${payload.startyears}`);
  }

  static updateCourses({payload}) {
    var token =  UserSession.getToken();
    var {faculty, fieldofstudy, startyears, onsemester, elective, compulsory} = payload;
    return axios.post(`${apiBaseURL}/courses/updateratings/me`, {faculty, fieldofstudy, startyears, onsemester,elective,compulsory, token});
  }

  static getProfessors({payload}) {
    var token =  UserSession.getToken();
    return axios.get(`${apiBaseURL}/professors/get/me/${token}/${payload.faculty}/${payload.fieldofstudy}/${payload.startyears}`);
  }

  static updateProfessors({payload}) {
    var token =  UserSession.getToken();
    var {faculty, fieldofstudy, startyears, onsemester, professors} = payload;
    return axios.post(`${apiBaseURL}/professors/updateratings/me`, {faculty, fieldofstudy, startyears, onsemester,professors, token});
  }

  static getRecommendations({payload}) {
    var token =  UserSession.getToken();
    var {faculty, fieldofstudy, startyears, onsemester, mode} = payload;
    return axios.get(`${apiBaseURL}/recommendation/get/me/${token}/${payload.faculty}/${payload.fieldofstudy}/${payload.startyears}/${payload.onsemester}/${payload.mode}`);
  }

}
