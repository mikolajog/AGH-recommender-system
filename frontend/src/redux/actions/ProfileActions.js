import * as Types from './ProfileActionTypes';

export function getProfile() {
  return {type: Types.PROFILE_GET};
}

export function getProfileSuccess(payload) {
  return {type: Types.PROFILE_GET_SUCCESS, payload};
}

export function getProfileFailure(error) {
  return {type: Types.PROFILE_GET_FAILURE, error};
}

export function createProfile(payload) {
  return {type: Types.PROFILE_CREATE, payload};
}

export function createProfileSuccess(payload) {
  return {type: Types.PROFILE_CREATE_SUCCESS, payload};
}

export function createProfileFailure(error) {
  return {type: Types.PROFILE_CREATE_FAILURE, error};
}

export function createProfileInit() {
  return {type: Types.PROFILE_CREATE_INIT};
}
