import * as Types from './AuthActionTypes';

export function login(index_number, password) {
  return {type: Types.LOGIN, index_number, password};
}

export function loginSuccess(token) {
  return {type: Types.LOGIN_SUCCESS, token};
}

export function loginFailure(error) {
  return {type: Types.LOGIN_FAILURE, error};
}

export function logout() {
  return {type: Types.LOGOUT};
}
