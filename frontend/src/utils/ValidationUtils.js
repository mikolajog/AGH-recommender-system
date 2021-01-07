export default class ValidationUtils {
  static checkEmail(email, message) {
    var regex = /[A-Z0-9._%+-]+@student.agh.edu.pl/igm;
    if (email && !regex.test(email)) {
      return message || 'Proszę wprowadzić poprawny adres e-mail w domenie student.agh.edu.pl';
    }
  }

  static checkIndex(value, message) {
    var regex = /[0-9]{6}/igm;
    if (value && !regex.test(value)) {
      return message || 'Proszę wprowadzić poprawny numer indeksu.';
    }
  }

  static checkPass(value, message) {
    var regex = /.{8,}/igm;
    if (value && !regex.test(value)) {
      return message || 'Proszę wprowadzić hasło o długości minimum 8 znaków.';
    }
  }

  static checkName(value, message) {
    var regex = /^[A-Z-zóąśłżźćńÓĄŚŁŻŹĆŃ][a-z-zóąśłżźćńÓĄŚŁŻŹĆŃ]{2,20} [A-Z-zóąśłżźćńÓĄŚŁŻŹĆŃ][a-z-zóąśłżźćńÓĄŚŁŻŹĆŃ]{1,25}$/igm;
    if (value && !regex.test(value)) {
      return message || 'Proszę wprowadzić poprawne imię i nazwisko.';
    }
  }

  static checkKeyword(value, message) {
    var regex = /[^ ]+/igm;
    if (value && !regex.test(value)) {
      return message || 'Proszę wprowadzić poprawne pojedyncze słowo.';
    }
  }

  static checkUrl(url, message) {
    var regex = /^(http)s?(:\/\/)([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$/igm;  // eslint-disable-line no-useless-escape
    if (url && !regex.test(url)) {
      return message || 'Please enter a valid URL. (ex. http(s)://domain.com)';
    }
  }
}
