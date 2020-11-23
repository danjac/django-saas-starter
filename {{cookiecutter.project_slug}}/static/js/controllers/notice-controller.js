import { Controller } from 'stimulus';

export default class extends Controller {
  // show/hide static notifications such as a cookie banner.

  connect() {
    if (!window.localStorage.getItem(this.storageKey)) {
      this.element.classList.remove('hidden');
    }
  }

  dismiss() {
    window.localStorage.setItem(this.storageKey, true);
    this.element.classList.add('hidden');
  }

  get storageKey() {
    return this.data.get('key')
  }
}
