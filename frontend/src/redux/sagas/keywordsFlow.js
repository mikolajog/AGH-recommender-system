import {all, call, put, takeEvery} from 'redux-saga/effects';
import KeywordsApi from '../../api/KeywordsApi';
import * as Actions from '../actions/KeywordsActions';
import * as Types from '../actions/KeywordsActionTypes';
import * as KeywordsActions from '../actions/KeywordsActions';
import { push } from 'connected-react-router'

export default function* keywordsFlow() {
  yield all([
    takeEvery(Types.KEYWORDS_GET_KEYWORDS_GET, getKeywords),
    takeEvery(Types.KEYWORDS_ADD_KEYWORD_POST, addKeyword),
    takeEvery(Types.KEYWORDS_DELETE_KEYWORD_DELETE, deleteKeyword),
  ]);
}

function* getKeywords() {
  try {
    const response = yield call(KeywordsApi.getKeywords);
    yield put(Actions.getKeywordsSuccess(response));
  }
  catch (error) {
    yield put(Actions.getKeywordsFailure(error));
  }
}

function* addKeyword(action) {
  var {payload} = action;
  try {
    const response = yield call(KeywordsApi.addKeyword, payload);
    yield put(Actions.addKeywordSuccess(response));
  }
  catch (error) {
    yield put(Actions.addKeywordFailure(error));
  }
}

function* deleteKeyword(action) {
  var {payload} = action;
  try {
    const response = yield call(KeywordsApi.deleteKeyword, payload);
    yield put(Actions.deleteKeywordSuccess(response));
  }
  catch (error) {
    yield put(Actions.deleteKeywordFailure(error));
  }
}

// KEYWORDS_GET_KEYWORDS_GET
// KEYWORDS_ADD_KEYWORD_POST
// KEYWORDS_DELETE_KEYWORD_DELETE