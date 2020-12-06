import {all, call, put, takeEvery} from 'redux-saga/effects';
import FieldofstudyApi from '../../api/FieldofstudyApi';
import * as Actions from '../actions/FieldofstudyActions';
import * as Types from '../actions/FieldofstudyActionTypes';
import { push } from 'connected-react-router'

export default function* fieldofstudyFlow() {
  yield all([
    takeEvery(Types.FIELDOFSTUDY_GET_GETPOSSIBLEFACULTIES_GET, getPossibleFaculties),
    takeEvery(Types.FIELDOFSTUDY_GET_GETPOSSIBLEFIELDSOFSTUDY_GET, getPossibleFieldsofstudy),
    takeEvery(Types.FIELDOFSTUDY_GET_GETPOSSIBLESTARTYEARSFORFIELDSOFSTUDY_GET, getPossibleStartYearsForFieldsofstudy),
    takeEvery(Types.FIELDOFSTUDY_GET_GETUSERFIELDSOFSTUDY_GET, getUserFieldsOfStudy),
    takeEvery(Types.FIELDOFSTUDY_POST_CONNECTUSERWITHFIELDOFSTUDY_POST, connectUserWithFieldofstudy),
    takeEvery(Types.FIELDOFSTUDY_POST_DISCONNECTUSERWITHFIELDOFSTUDY_POST, disconnectUserWithFieldofstudy),
    takeEvery(Types.FIELDOFSTUDY_GET_GETPROFILE_GET, getProfile),
    takeEvery(Types.FIELDOFSTUDY_GET_GETCOURSES_GET, getCourses),
    takeEvery(Types.FIELDOFSTUDY_POST_UPDATECOURSES_POST, updateCourses),
  ]);
}

function* getPossibleFaculties() {
  try {
    const response = yield call(FieldofstudyApi.getPossibleFaculties);
    yield put(Actions.getPossibleFacultiesSuccess(response));
  }
  catch (error) {
    yield put(Actions.getPossibleFacultiesFailure(error));
  }
}

function* getPossibleFieldsofstudy(payload) {
  try {
    const response = yield call(FieldofstudyApi.getPossibleFieldsofstudy, payload);
    yield put(Actions.getPossibleFieldsofstudySuccess(response));
  }
  catch (error) {
    yield put(Actions.getPossibleFieldsofstudyFailure(error));
  }
}

function* getPossibleStartYearsForFieldsofstudy(payload) {
  try {
    const response = yield call(FieldofstudyApi.getPossibleStartYearsForFieldsofstudy, payload);
    yield put(Actions.getPossibleStartYearsForFieldsofstudySuccess(response));
  }
  catch (error) {
    yield put(Actions.getPossibleStartYearsForFieldsofstudyFailure(error));
  }
}

function* getUserFieldsOfStudy() {
  try {
    const response = yield call(FieldofstudyApi.getUserFieldsOfStudy);
    yield put(Actions.getUserFieldsOfStudySuccess(response));
  }
  catch (error) {
    yield put(Actions.getUserFieldsOfStudyFailure(error));
  }
}

function* connectUserWithFieldofstudy(payload) {
  try {
    const response = yield call(FieldofstudyApi.connectUserWithFieldofstudy, payload);
    yield put(Actions.connectUserWithFieldofstudySuccess(response));
  }
  catch (error) {
    yield put(Actions.connectUserWithFieldofstudyFailure(error));
  }
}

function* disconnectUserWithFieldofstudy(payload) {
  try {
    const response = yield call(FieldofstudyApi.disconnectUserWithFieldofstudy, payload);
    yield put(Actions.disconnectUserWithFieldofstudySuccess(response));
  }
  catch (error) {
    yield put(Actions.disconnectUserWithFieldofstudyFailure(error));
  }
}

function* getProfile() {
  try {
    const response = yield call(FieldofstudyApi.getProfile);
    yield put(Actions.getProfileSuccess(response));
  }
  catch (error) {
    yield put(Actions.getProfileFailure(error));
  }
}

function* getCourses(payload) {
  try {
    const response = yield call(FieldofstudyApi.getCourses, payload);
    yield put(Actions.getCoursesSuccess(response));
  }
  catch (error) {
    yield put(Actions.getCoursesFailure(error));
  }
}

function* updateCourses(payload) {
  try {
    const response = yield call(FieldofstudyApi.updateCourses, payload);
    yield put(Actions.updateCoursesSuccess(response));
  }
  catch (error) {
    yield put(Actions.updateCoursesFailure(error));
  }
}


// FIELDOFSTUDY_GET_GETPOSSIBLEFACULTIES
// FIELDOFSTUDY_GET_GETPOSSIBLEFIELDSOFSTUDY
// FIELDOFSTUDY_GET_GETPOSSIBLESTARTYEARSFORFIELDSOFSTUDY
// FIELDOFSTUDY_GET_GETUSERFIELDSOFSTUDY
// FIELDOFSTUDY_POST_CONNECTUSERWITHFIELDOFSTUDY
// FIELDOFSTUDY_POST_DISCONNECTUSERWITHFIELDOFSTUDY