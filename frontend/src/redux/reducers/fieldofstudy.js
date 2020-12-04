import * as Types from '../actions/FieldofstudyActionTypes';
import ErrorUtils from '../../utils/ErrorUtils';

function getInitialState() {
  return {
    isFetching: false,
    possiblefaculties: {},
    possiblefieldsofstudies: {},
    possiblestartyears:{},
    errors: {},
    currentfieldsofstudy:[],
    profile:{}
  };
}

export default function getPossibleFaculties(state = getInitialState(), action) {
  switch (action.type) {
    case Types.FIELDOFSTUDY_GET_GETPOSSIBLEFIELDSOFSTUDY_INIT:
    case Types.FIELDOFSTUDY_GET_GETPOSSIBLEFACULTIES_INIT:
    case Types.FIELDOFSTUDY_GET_GETPOSSIBLESTARTYEARSFORFIELDSOFSTUDY_INIT:
    case Types.FIELDOFSTUDY_POST_CONNECTUSERWITHFIELDOFSTUDY_INIT:
    case Types.FIELDOFSTUDY_POST_DISCONNECTUSERWITHFIELDOFSTUDY_INIT:
    case Types.FIELDOFSTUDY_GET_GETUSERFIELDSOFSTUDY_INIT:
    case Types.FIELDOFSTUDY_GET_GETPROFILE_INIT:
      return getInitialState();
      case Types.FIELDOFSTUDY_GET_GETPOSSIBLEFIELDSOFSTUDY_GET:
      return {
        ...state,
        isFetching: true,
        possiblefaculties: action.payload.faculty
      };
    case Types.FIELDOFSTUDY_GET_GETPOSSIBLEFACULTIES_GET:
      case Types.FIELDOFSTUDY_GET_GETPROFILE_GET:
        return {
          ...state,
          isFetching: true,
        };
    case Types.FIELDOFSTUDY_GET_GETPOSSIBLESTARTYEARSFORFIELDSOFSTUDY_GET:
      return {
        ...state,
        isFetching: true,
        possiblefaculties: action.payload.faculty,
        possiblefieldsofstudies: action.payload.fieldofstudyname
      };
    case Types.FIELDOFSTUDY_GET_GETPOSSIBLEFACULTIES_SUCCESS:
      return {
        ...state,
        isFetching: false,
        possiblefaculties: action.payload
      };
    case Types.FIELDOFSTUDY_GET_GETPROFILE_SUCCESS:
        return {
          ...state,
          isFetching: false,
          profile: action.payload
        };
    case Types.FIELDOFSTUDY_GET_GETPOSSIBLEFIELDSOFSTUDY_FAILURE:
    case Types.FIELDOFSTUDY_GET_GETPOSSIBLEFACULTIES_FAILURE:
    case Types.FIELDOFSTUDY_GET_GETPOSSIBLESTARTYEARSFORFIELDSOFSTUDY_FAILURE:
    case Types.FIELDOFSTUDY_POST_CONNECTUSERWITHFIELDOFSTUDY_FAILURE:
    case Types.FIELDOFSTUDY_POST_DISCONNECTUSERWITHFIELDOFSTUDY_FAILURE:
    case Types.FIELDOFSTUDY_GET_GETUSERFIELDSOFSTUDY_FAILURE:
      case Types.FIELDOFSTUDY_GET_GETPROFILE_FAILURE:
      return {
        isFetching: false,
        errors: ErrorUtils.getApiErrors(action.error)
      };
      case Types.FIELDOFSTUDY_GET_GETPOSSIBLEFIELDSOFSTUDY_SUCCESS:
      return {
        ...state,
        isFetching: false,
        // possiblefaculties: '',
        possiblefieldsofstudies: action.payload
      };
      case Types.FIELDOFSTUDY_POST_CONNECTUSERWITHFIELDOFSTUDY_POST:
      case Types.FIELDOFSTUDY_POST_DISCONNECTUSERWITHFIELDOFSTUDY_POST:
      case Types.FIELDOFSTUDY_GET_GETUSERFIELDSOFSTUDY_GET:
        return {
          ...state,
          isFetching: true
        };
      case Types.FIELDOFSTUDY_POST_CONNECTUSERWITHFIELDOFSTUDY_SUCCESS:
        case Types.FIELDOFSTUDY_POST_DISCONNECTUSERWITHFIELDOFSTUDY_SUCCESS:
        return {
          ...state,
          isFetching: false
        };
      case Types.FIELDOFSTUDY_GET_GETPOSSIBLESTARTYEARSFORFIELDSOFSTUDY_SUCCESS:
        return {
          ...state,
          isFetching: false,
          // possiblefaculties: '',
          possiblestartyears: action.payload
        };
        case Types.FIELDOFSTUDY_GET_GETUSERFIELDSOFSTUDY_SUCCESS:
        return {
          ...state,
          isFetching: false,
          // possiblefaculties: '',
          currentfieldsofstudy: action.payload
        };
    default:
      return state;
  }
}
