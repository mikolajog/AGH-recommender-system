import React from 'react';
import PropTypes from 'prop-types';
import {withRouter} from 'react-router';
import {Link} from 'react-router-dom';
import InputValidator from '../components/validation/InputValidator.jsx';
import ValidatedComponent from '../components/validation/ValidatedComponent.jsx';
import * as Actions from '../redux/actions/KeywordsActions';
import {bindActionCreators} from 'redux';
import {connect} from 'react-redux';
import settings from '../config/settings';
import axios from '../api/axios';
import UserSession from '../UserSession';
import _ from 'lodash';


class Keywords extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      errors:{},
      keywords:{},
      canDelete:false,
      canAdd: false,
      wordDel:null,
      wordAdd:null
    }
    this.checkifCanDeleteKeyword = this.checkifCanDeleteKeyword.bind(this);
    this.changeDeleteKeywordSelection = this.changeDeleteKeywordSelection.bind(this);
    this.deleteKeyword = this.deleteKeyword.bind(this);
    this.addKeyword = this.addKeyword.bind(this);
    this.changeWord = this.changeWord.bind(this);
  }

  componentDidMount() {
    const {apiBaseURL} = settings;
    if(UserSession.getToken()===null){this.props.history.push('/login');}
    else{
    this.props.getKeywords();}
  }

  checkifCanDeleteKeyword(){
    var {errors, keywords, isFetching} = this.props.keywords;
    if(Array.from(keywords).length > 0){this.setState({canDelete:true})}
    else{this.setState({canDelete:false})}
  }

  changeDeleteKeywordSelection(event) {
    var canDelete = this.state.wordDel && event.target.value;
    this.setState({
      wordDel: event.target.value,
      canDelete: canDelete
    });
  }

  deleteKeyword(e) {
    e.preventDefault();
    var word = this.state.wordDel;
    this.props.deleteKeyword({word});
    this.setState({canDelete:false, wordDel:null});
  }

  addKeyword(e) {
    e.preventDefault();
    var wordAdd = this.state.wordAdd;
    var {errors, keywords, isFetching} = this.props.keywords;
    if( wordAdd !=="") {
      var word = wordAdd;
      this.props.addKeyword({word});this.inputword.value = '';this.setState({
        wordAdd: '',
        canAdd: false
      });} 
  }

  changeWord(event) {
    var canAdd = this.state.wordAdd && event.target.value;
    this.setState({
      wordAdd: event.target.value,
      canAdd: canAdd
    });
  }
  

  render() {

    var {errors, keywords, isFetching} = this.props.keywords;
    var current_keywords = Array.from(keywords).map((anObjectMapped, index) => {
      return (
      <option key={anObjectMapped.word} value={anObjectMapped.word}>{anObjectMapped.word}</option>  
      );
  })
    return (<div>
      <div>
<div className="row">
        <div className="small-12 columns">
          <div className="nt-box">
            <div className="nt-box-title">
            Obecne słowa kluczowe 
            </div>
            <div className="small-12 medium-10 large-10 columns">
            <select onClick={this.changeDeleteKeywordSelection}>
            {current_keywords}
    </select>
    </div>
    <div className="row text-center">
            <button className="btn"
                    type="submit"
                    name="submit-login"
                    onClick={this.deleteKeyword}
                    disabled={!this.state.canDelete}>
              Usuń słowo kluczowe
            </button>
          </div>
            </div>
          </div>
        </div>
      </div>
      <p></p>
<div className="row">
        <div className="small-12 columns">
          <div className="nt-box">
            <div className="nt-box-title">
              Dodaj słowo kluczowe
              <p>Dodaj pojedyncze słowa kluczowe związane z Twoimi zainteresowaniami, umiejętnościami lub planowaną karierą.</p>
            </div>
            <div className="nt-box-row">
            <div >

            <div className="small-12 medium-10 large-10 columns">
              <InputValidator fieldName="Słowo"
                              errors={null}
                              shouldValidateOnBlur={true}>
                <input ref={(ref) => this.inputword= ref} 
                type="text"
                       name="wordinput"
                       placeholder="Wpisz słowo"
                       onChange={this.changeWord}/>
              </InputValidator>
              </div> 

            <div className="row text-center">
            <button className="btn"
                    type="submit"
                    name="submit-login"
                    onClick={this.addKeyword}
                    disabled={!this.state.canAdd}>
              Dodaj słowo kluczowe
            </button>
          </div>
  
   </div>

            </div>
          </div>
        </div>
      </div>
      </div>

      );
  }
} 



Keywords.displayName = 'Keywords';

Keywords.propTypes = {
  keywords: PropTypes.object
};

function mapDispatchToProps(dispatch) {
  return bindActionCreators(Actions, dispatch);
}

function mapStateToProps(state) {
  return {
    keywords: _.get(state, 'keywords'),
    fieldofstudy: _.get(state, 'fieldofstudy'),
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(ValidatedComponent(withRouter(Keywords)));
