import { Controller } from 'stimulus';

export default class extends Controller {
  static targets = ['item'];

  toggle() {
    // toggle DOM element
    if (this.hasItemTargets) {
      this.itemTargets.forEach((item) => {
        item.classList.toggle(this.toggleClass);
      });
    } else {
      this.element.classList.toggle(this.toggleClass);
    }
  }

  get toggleClass() {
    return this.data.get('class') || 'hidden';
  }
}
