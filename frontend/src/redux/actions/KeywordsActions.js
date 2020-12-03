import * as Types from './KeywordsActionTypes';

export function getKeywords() {
  return {type: Types.KEYWORDS_GET_KEYWORDS_GET};
}

export function getKeywordsSuccess(payload) {
  return {type: Types.KEYWORDS_GET_KEYWORDS_GET_SUCCESS, payload};
}

export function getKeywordsFailure(error) {
  return {type: Types.KEYWORDS_GET_KEYWORDS_GET_FAILURE, error};
}

export function getKeywordsInit() {
  return {type: Types.KEYWORDS_GET_KEYWORDS_GET_INIT};
}

export function addKeyword(payload) {
  return {type: Types.KEYWORDS_ADD_KEYWORD_POST, payload};
}

export function addKeywordSuccess(payload) {
  return {type: Types.KEYWORDS_ADD_KEYWORD_POST_SUCCESS, payload};
}

export function addKeywordFailure(error) {
  return {type: Types.KEYWORDS_ADD_KEYWORD_POST_FAILURE, error};
}

export function addKeywordInit() {
  return {type: Types.KEYWORDS_ADD_KEYWORD_POST_INIT};
}

export function deleteKeyword(payload) {
  return {type: Types.KEYWORDS_DELETE_KEYWORD_DELETE, payload};
}

export function deleteKeywordSuccess(payload) {
  return {type: Types.KEYWORDS_DELETE_KEYWORD_DELETE_SUCCESS, payload};
}

export function deleteKeywordFailure(error) {
  return {type: Types.KEYWORDS_DELETE_KEYWORD_DELETE_FAILURE, error};
}

export function deleteKeywordInit() {
  return {type: Types.KEYWORDS_DELETE_KEYWORD_DELETE_INIT};
}