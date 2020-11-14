import { Controller } from 'stimulus';

export default class extends Controller {
  connect() {
    if (!window.localStorage.getItem('cookie-notice')) {
      this.element.classList.remove('hidden');
    }
  }

  dismiss() {
    window.localStorage.setItem('cookie-notice', true);
    this.element.classList.add('hidden');
  }
}
