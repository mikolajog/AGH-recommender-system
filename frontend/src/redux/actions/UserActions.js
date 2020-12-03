import * as Types from './UserActionTypes';

export function addFieldOfStudy(payload) {
  return {type: Types.USER_ADD_FIELDOFSTUDY_POST, payload};
}

export function addFieldOfStudySuccess(payload) {
  return {type: Types.USER_ADD_FIELDOFSTUDY_POST_SUCCESS, payload};
}

export function addFieldOfStudyFailure(error) {
  return {type: Types.USER_ADD_FIELDOFSTUDY_POST_FAILURE, error};
}

export function addFieldOfStudyInit() {
  return {type: Types.USER_ADD_FIELDOFSTUDY_POST_INIT};
}

export function getFieldsOfStudy() {
  return {type: Types.USER_GET_FIELDSOFSTUDY_GET};
}

export function getFieldsOfStudySuccess(payload) {
  return {type: Types.USER_GET_FIELDSOFSTUDY_GET_SUCCESS, payload};
}

export function getFieldsOfStudyFailure(error) {
  return {type: Types.USER_GET_FIELDSOFSTUDY_GET_FAILURE, error};
}

export function getFieldsOfStudyInit() {
  return {type: Types.USER_GET_FIELDSOFSTUDY_GET_INIT};
}
