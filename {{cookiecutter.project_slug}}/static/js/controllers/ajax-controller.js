import axios from 'axios';
import Turbolinks from 'turbolinks';
import { Controller } from 'stimulus';

export default class extends Controller {
  static targets = ['fragment'];

  get(event) {
    event.preventDefault();
    this.dispatch('GET');
  }

  post(event) {
    event.preventDefault();
    this.dispatch('POST');
  }

  put(event) {
    event.preventDefault();
    this.dispatch('POST');
  }

  delete(event) {
    event.preventDefault();
    this.dispatch('DELETE');
  }

  async dispatch(method) {
    const confirmMsg = this.data.get('confirm');
    if (confirmMsg && !window.confirm(confirmMsg)) {
      return;
    }

    const url = this.data.get('url') || this.element.getAttribute('href');

    const headers = {
      'Turbolinks-Referrer': location.href,
    };

    const replace = this.data.has('replace');

    // request server return an HTML fragment to insert into DOM
    //
    if (replace) {
      headers['X-Request-Fragment'] = true;
    }

    const response = await axios({
      headers,
      method,
      url,
    });

    const redirect = this.data.get('redirect');

    if (redirect) {
      if (redirect !== 'none') Turbolinks.visit(redirect);
      return;
    }

    // remove target
    if (this.data.has('remove')) {
      if (this.hasFragmentTargets) {
        this.fragmentTargets.forEach((target) => target.remove());
      } else {
        this.element.remove();
      }
      return;
    }

    const contentType = response.headers['content-type'];

    if (replace && contentType.match(/html/)) {
      if (this.hasFragmentTargets) {
        this.fragmentTargets.forEach((target) => (target.innerHTML = response.data));
      } else {
        this.element.innerHTML = response.data;
      }
      return;
    }

    // default behaviour: redirect passed down in header
    if (!redirect && contentType.match(/javascript/)) {
      /* eslint-disable-next-line no-eval */
      eval(response.data);
    }
  }
}
