import * as Types from './FieldofstudyActionTypes';

export function getPossibleFaculties() {
  return {type: Types.FIELDOFSTUDY_GET_GETPOSSIBLEFACULTIES_GET};
}

export function getPossibleFacultiesSuccess(payload) {
  return {type: Types.FIELDOFSTUDY_GET_GETPOSSIBLEFACULTIES_SUCCESS, payload};
}

export function getPossibleFacultiesFailure(error) {
  return {type: Types.FIELDOFSTUDY_GET_GETPOSSIBLEFACULTIES_FAILURE, error};
}

export function getPossibleFacultiesInit() {
  return {type: Types.FIELDOFSTUDY_GET_GETPOSSIBLEFACULTIES_INIT};
}

///
export function getPossibleFieldsofstudy(payload) {
  return {type: Types.FIELDOFSTUDY_GET_GETPOSSIBLEFIELDSOFSTUDY_GET, payload};
}

export function getPossibleFieldsofstudySuccess(payload) {
  return {type: Types.FIELDOFSTUDY_GET_GETPOSSIBLEFIELDSOFSTUDY_SUCCESS, payload};
}

export function getPossibleFieldsofstudyFailure(error) {
  return {type: Types.FIELDOFSTUDY_GET_GETPOSSIBLEFIELDSOFSTUDY_FAILURE, error};
}

export function getPossibleFieldsofstudyInit() {
  return {type: Types.FIELDOFSTUDY_GET_GETPOSSIBLEFIELDSOFSTUDY_INIT};
}

//
export function getPossibleStartYearsForFieldsofstudy(payload) {
  return {type: Types.FIELDOFSTUDY_GET_GETPOSSIBLESTARTYEARSFORFIELDSOFSTUDY_GET, payload};
}

export function getPossibleStartYearsForFieldsofstudySuccess(payload) {
  return {type: Types.FIELDOFSTUDY_GET_GETPOSSIBLESTARTYEARSFORFIELDSOFSTUDY_SUCCESS, payload};
}

export function getPossibleStartYearsForFieldsofstudyFailure(error) {
  return {type: Types.FIELDOFSTUDY_GET_GETPOSSIBLESTARTYEARSFORFIELDSOFSTUDY_FAILURE, error};
}

export function getPossibleStartYearsForFieldsofstudyInit() {
  return {type: Types.FIELDOFSTUDY_GET_GETPOSSIBLESTARTYEARSFORFIELDSOFSTUDY_INIT};
}

///
export function getUserFieldsOfStudy() {
  return {type: Types.FIELDOFSTUDY_GET_GETUSERFIELDSOFSTUDY_GET};
}

export function getUserFieldsOfStudySuccess(payload) {
  return {type: Types.FIELDOFSTUDY_GET_GETUSERFIELDSOFSTUDY_SUCCESS, payload};
}

export function getUserFieldsOfStudyFailure(error) {
  return {type: Types.FIELDOFSTUDY_GET_GETUSERFIELDSOFSTUDY_FAILURE, error};
}

export function getUserFieldsOfStudyInit() {
  return {type: Types.FIELDOFSTUDY_GET_GETUSERFIELDSOFSTUDY_INIT};
}

//

export function connectUserWithFieldofstudy(payload) {
  return {type: Types.FIELDOFSTUDY_POST_CONNECTUSERWITHFIELDOFSTUDY_POST, payload};
}

export function connectUserWithFieldofstudySuccess(payload) {
  return {type: Types.FIELDOFSTUDY_POST_CONNECTUSERWITHFIELDOFSTUDY_SUCCESS, payload};
}

export function connectUserWithFieldofstudyFailure(error) {
  return {type: Types.FIELDOFSTUDY_POST_CONNECTUSERWITHFIELDOFSTUDY_FAILURE, error};
}

export function connectUserWithFieldofstudyInit() {
  return {type: Types.FIELDOFSTUDY_POST_CONNECTUSERWITHFIELDOFSTUDY_INIT};
}

//
export function disconnectUserWithFieldofstudy(payload) {
  return {type: Types.FIELDOFSTUDY_POST_DISCONNECTUSERWITHFIELDOFSTUDY_POST, payload};
}

export function disconnectUserWithFieldofstudySuccess(payload) {
  return {type: Types.FIELDOFSTUDY_POST_DISCONNECTUSERWITHFIELDOFSTUDY_SUCCESS, payload};
}

export function disconnectUserWithFieldofstudyFailure(error) {
  return {type: Types.FIELDOFSTUDY_POST_DISCONNECTUSERWITHFIELDOFSTUDY_FAILURE, error};
}

export function disconnectUserWithFieldofstudyInit() {
  return {type: Types.FIELDOFSTUDY_POST_DISCONNECTUSERWITHFIELDOFSTUDY_INIT};
}

//
export function getProfile() {
  return {type: Types.FIELDOFSTUDY_GET_GETPROFILE_GET};
}

export function getProfileSuccess(payload) {
  return {type: Types.FIELDOFSTUDY_GET_GETPROFILE_SUCCESS, payload};
}

export function getProfileFailure(error) {
  return {type: Types.FIELDOFSTUDY_GET_GETPROFILE_FAILURE, error};
}

export function getProfileInit() {
  return {type: Types.FIELDOFSTUDY_GET_GETPROFILE_INIT};
}

///
export function getCourses(payload) {
  return {type: Types.FIELDOFSTUDY_GET_GETCOURSES_GET, payload};
}

export function getCoursesSuccess(payload) {
  return {type: Types.FIELDOFSTUDY_GET_GETCOURSES_SUCCESS, payload};
}

export function getCoursesFailure(error) {
  return {type: Types.FIELDOFSTUDY_GET_GETCOURSES_FAILURE, error};
}

export function getCoursesInit() {
  return {type: Types.FIELDOFSTUDY_GET_GETCOURSES_INIT};
}

///
export function updateCourses(payload) {
  return {type: Types.FIELDOFSTUDY_POST_UPDATECOURSES_POST, payload};
}

export function updateCoursesSuccess(payload) {
  return {type: Types.FIELDOFSTUDY_POST_UPDATECOURSES_SUCCESS, payload};
}

export function updateCoursesFailure(error) {
  return {type: Types.FIELDOFSTUDY_POST_UPDATECOURSES_FAILURE, error};
}

export function updateCoursesInit() {
  return {type: Types.FIELDOFSTUDY_POST_UPDATECOURSES_INIT};
}

///
export function getProfessors(payload) {
  return {type: Types.FIELDOFSTUDY_GET_GETPROFESSORS_GET, payload};
}

export function getProfessorsSuccess(payload) {
  return {type: Types.FIELDOFSTUDY_GET_GETPROFESSORS_SUCCESS, payload};
}

export function getProfessorsFailure(error) {
  return {type: Types.FIELDOFSTUDY_GET_GETPROFESSORS_FAILURE, error};
}

export function getProfessorsInit() {
  return {type: Types.FIELDOFSTUDY_GET_GETPROFESSORS_INIT};
}

///
export function updateProfessors(payload) {
  return {type: Types.FIELDOFSTUDY_POST_UPDATEPROFESSORS_POST, payload};
}

export function updateProfessorsSuccess(payload) {
  return {type: Types.FIELDOFSTUDY_POST_UPDATEPROFESSORS_SUCCESS, payload};
}

export function updateProfessorsFailure(error) {
  return {type: Types.FIELDOFSTUDY_POST_UPDATEPROFESSORS_FAILURE, error};
}

export function updateProfessorsInit() {
  return {type: Types.FIELDOFSTUDY_POST_UPDATEPROFESSORS_INIT};
}

export function getRecommendations(payload) {
  return {type: Types.FIELDOFSTUDY_GET_GETRECOMMENDATIONS_GET, payload};
}

export function getRecommendationsSuccess(payload) {
  return {type: Types.FIELDOFSTUDY_GET_GETRECOMMENDATIONS_SUCCESS, payload};
}

export function getRecommendationsFailure(error) {
  return {type: Types.FIELDOFSTUDY_GET_GETRECOMMENDATIONS_FAILURE, error};
}

export function getRecommendationsInit() {
  return {type: Types.FIELDOFSTUDY_GET_GETRECOMMENDATIONS_INIT};
}
