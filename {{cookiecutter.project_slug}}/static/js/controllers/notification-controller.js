import { Controller } from 'stimulus';

export default class extends Controller {
  // permanently or temporarily remove notifications e.g.
  // flash messages or cookie banners

  connect() {
    if (window.localStorage.getItem(this.storageKey)) {
      // automatically remove if storage key present
      this.remove();
    } else if (this.data.has('timeout')) {
      // automatically toggle elements on page load after timeout
      const timeout = parseInt(this.data.get('timeout'));
      if (!isNaN(timeout) && timeout > 0) {
        setTimeout(() => this.remove(), timeout);
      }
    }
  }

  remove() {
    if (this.storageKey) {
      window.localStorage.setItem(this.storageKey, true);
    }
    this.element.remove();
  }

  get storageKey() {
    return this.data.get('storage-key');
  }
}
