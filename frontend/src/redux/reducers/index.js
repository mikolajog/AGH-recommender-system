import {combineReducers} from 'redux';
import { connectRouter } from 'connected-react-router'
import notifications from './notifications';
import auth from './auth';
import signup from './signup';
import profile from './profile';
import genres from './genres';
import movies from './movies';
import person from './person';
import user from './user';
import keywords from './keywords';

const createRootReducer = (history) => combineReducers({
  router: connectRouter(history),
  notifications,
  auth,
  signup,
  profile,
  genres,
  movies,
  person,
  user,
  keywords
});

export default createRootReducer;
