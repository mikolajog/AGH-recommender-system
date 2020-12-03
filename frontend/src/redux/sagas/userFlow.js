import {all, call, put, takeEvery} from 'redux-saga/effects';
import UserApi from '../../api/UserApi';
import * as Actions from '../actions/UserActions';
import * as Types from '../actions/UserActionTypes';
import * as UserActions from '../actions/UserActions';
import { push } from 'connected-react-router'

export default function* userFlow() {
  yield all([
    takeEvery(Types.USER_ADD_FIELDOFSTUDY_POST, addFieldOfStudy),
    takeEvery(Types.USER_GET_FIELDSOFSTUDY_GET, getFieldsOfStudy),
  ]);
}

function* addFieldOfStudy(action) {
  var {payload} = action;

  try {
    const response = yield call(UserApi.addFieldOfStudy, payload);
    yield put(Actions.addFieldOfStudySuccess(response));
    // yield put(UserActions.addFieldOfStudy(payload.faculty, payload.fieldofstudy, payload.on_semester));
  }
  catch (error) {
    yield put(Actions.addFieldOfStudyFailure(error));
  }
}

function* getFieldsOfStudy() {
  try {
    const response = yield call(UserApi.getFieldsOfStudy);
    yield put(Actions.getFieldsOfStudySuccess(response));
  }
  catch (error) {
    yield put(Actions.addFieldOfStudyFailure(error));
  }
}

