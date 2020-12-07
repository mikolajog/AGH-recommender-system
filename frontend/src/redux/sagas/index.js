import {all, fork} from 'redux-saga/effects';
import errorFlow from './errorFlow';
import authFlow from './authFlow';
import profileFlow from './profileFlow';
import signupFlow from './signupFlow';
import keywordsFlow from './keywordsFlow';
import fieldofstudyFlow from './fieldofstudyFlow';

export default function* root() {
  yield all([
    fork(errorFlow),
    fork(authFlow),
    fork(profileFlow),
    fork(signupFlow),
    fork(keywordsFlow),
    fork(fieldofstudyFlow)
  ]);
}
