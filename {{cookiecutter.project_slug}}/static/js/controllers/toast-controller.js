import { Controller } from 'stimulus';

import useTurbo from '~/turbo';

export default class extends Controller {
  static targets = ['container', 'message'];

  static values = {
    timeout: Number,
    type: String,
  };

  connect() {
    if (this.hasTimeoutValue && this.timeoutValue > 0) {
      // automatically toggle elements on page load after timeout
      setTimeout(() => this.remove(), this.timeoutValue);
    }
    useTurbo(this);
  }

  turboSubmitEnd(event) {
    // handle messages in HTTP header
    const { fetchResponse } = event.detail;
    const headers = fetchResponse.response ? fetchResponse.response.headers : null;
    if (!headers) {
      return;
    }

    const messages = headers.get('X-Messages');
    if (messages) {
      JSON.parse(messages).forEach((msg) => this.showMessage(msg.tags, msg.message));
    }

    const msg = headers.get('X-Message');
    const type = headers.get('X-Message-Type');
    if (msg && type) {
      this.showMessage(type, msg);
    }
  }

  showMessage(type, message) {
    this.messageTarget.innerText = message;
    // ensure any previous class is removed
    if (this.hasTypeValue) {
      this.containerTarget.classList.remove(this.typeValue);
    }
    this.containerTarget.classList.add(type);
    this.typeValue = type;

    this.element.classList.remove('hidden');

    this.timeout = setTimeout(() => {
      this.hide();
      clearTimeout(this.timeout);
    }, this.removeAfterValue || TIMEOUT);
  }

  hide() {
    this.element.classList.add('hidden');
  }

  remove() {
    this.element.remove();
  }
}
