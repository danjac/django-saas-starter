import { Controller } from 'stimulus';

export default class extends Controller {
  static values = {
    timeout: Number,
  };

  connect() {
    if (this.hasTimeoutValue && this.timeoutValue > 0) {
      // automatically toggle elements on page load after timeout
      setTimeout(() => this.remove(), this.timeoutValue);
    }
  }

  remove() {
    this.element.remove();
  }
}
