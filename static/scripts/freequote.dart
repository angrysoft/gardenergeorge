import "dart:html";
import 'dart:js';

bool checkCaptcha() {
  var response = context['grecaptcha'].callMethod('getResponse');
  if (response.length == 0) {
    return false;
  } else {
    return true;
  }
}

void showModal(id) {
	querySelector(id).classes.add('modal-show');
}
void hideModal(id) {
    querySelector(id).classes.remove('modal-show');
}


void checkForm(var ev) {
  var recaptchaErrorMsg = querySelector('#recaptchaErrorMsg');
  if (checkCaptcha()) {
    recaptchaErrorMsg.setInnerHtml('');
    showModal('#info');
  } else {
    recaptchaErrorMsg.setInnerHtml('check "I am not a robot:" checkbox');
    recaptchaErrorMsg.focus();
    ev.preventDefault();
  }
}

void main() {
  querySelector('#mailForm').onSubmit.listen((Event ev) => checkForm(ev));
}
