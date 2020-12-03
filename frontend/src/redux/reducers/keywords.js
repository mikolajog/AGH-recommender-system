import * as Types from '../actions/KeywordsActionTypes';
import ErrorUtils from '../../utils/ErrorUtils';

function getInitialState() {
  return {
    isFetching: false,
    errors: {},
    keywords:{}
  };
}

export default function addFieldOfStudy(state = getInitialState(), action) {
  switch (action.type) {
    case Types.KEYWORDS_GET_KEYWORDS_GET_INIT:
    case Types.KEYWORDS_ADD_KEYWORD_POST_INIT:
    case Types.KEYWORDS_DELETE_KEYWORD_DELETE_INIT:
      return getInitialState();
    case Types.KEYWORDS_GET_KEYWORDS_GET:
    case Types.KEYWORDS_ADD_KEYWORD_POST:
    case Types.KEYWORDS_DELETE_KEYWORD_DELETE:
      return {
        ...state,
        isFetching: true,
      };
    case Types.KEYWORDS_GET_KEYWORDS_GET_SUCCESS:
    case Types.KEYWORDS_ADD_KEYWORD_POST_SUCCESS:
    case Types.KEYWORDS_DELETE_KEYWORD_DELETE_SUCCESS:
      return {
        ...state,
        isFetching: false,
        keywords: action.payload
      };
    case Types.KEYWORDS_GET_KEYWORDS_GET_FAILURE:
    case Types.KEYWORDS_ADD_KEYWORD_POST_FAILURE:
    case Types.KEYWORDS_DELETE_KEYWORD_DELETE_FAILURE:
      return {
        isFetching: false,
        errors: ErrorUtils.getApiErrors(action.error),
        keywords: action.state.keywords
      };
    default:
      return state;
  }
}

// KEYWORDS_GET_KEYWORDS_GET
// KEYWORDS_ADD_KEYWORD_POST
// KEYWORDS_DELETE_KEYWORD_DELETE
