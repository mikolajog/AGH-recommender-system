import { takeEvery, put } from 'redux-saga/effects';
import * as NotificationActions from '../actions/NotificationActions';
import _ from 'lodash';

export default function* watchErrors(getState) {
  yield takeEvery('*', function* logger(action) {
    if(action.error) {
      var errorAction = createErrorNotification(action.error);
      yield put(errorAction);
    }
  });
}

function createErrorNotification(err) {
    return NotificationActions.createError("Złe dane logowania!");
}

