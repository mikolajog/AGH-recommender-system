import * as Types from '../actions/UserActionTypes';
import ErrorUtils from '../../utils/ErrorUtils';

function getInitialState() {
  return {
    isFetching: false,
    field: {},
    errors: {}
  };
}

export default function addFieldOfStudy(state = getInitialState(), action) {
  switch (action.type) {
    case Types.USER_ADD_FIELDOFSTUDY_POST_INIT:
    case Types.USER_GET_FIELDSOFSTUDY_GET_INIT:
      return getInitialState();
    case Types.USER_ADD_FIELDOFSTUDY_POST:
    case Types.USER_GET_FIELDSOFSTUDY_GET:
      return {
        ...state,
        isFetching: true,
      };
    case Types.USER_ADD_FIELDOFSTUDY_POST_SUCCESS:
    case Types.USER_GET_FIELDSOFSTUDY_GET_SUCCESS:
      return {
        ...state,
        isFetching: false,
        field: action.payload
      };
    case Types.USER_ADD_FIELDOFSTUDY_POST_FAILURE:
    case Types.USER_GET_FIELDSOFSTUDY_GET_FAILURE:
      return {
        isFetching: false,
        errors: ErrorUtils.getApiErrors(action.error)
      };
    default:
      return state;
  }
}
