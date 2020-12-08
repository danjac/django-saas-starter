import { Controller } from 'stimulus';

export default class extends Controller {
  static targets = ['item'];

  toggle(event) {
    this.itemTargets.forEach((item) => {
      item.classList.toggle('hidden');
    });
  }
}
