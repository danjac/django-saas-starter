import axios from "axios";
import Turbolinks from "turbolinks";
import { Controller } from "stimulus";

export default class extends Controller {
  static targets = ["replace", "remove"];

  get() {
    this.dispatch("GET");
  }

  post() {
    this.dispatch("POST");
  }

  put() {
    this.dispatch("POST");
  }

  delete() {
    this.dispatch("DELETE");
  }

  async dispatch(method) {
    const confirmMsg = this.data.get("confirm");
    if (confirmMsg && !window.confirm(confirmMsg)) {
      return;
    }

    const url = this.data.get("url");
    const response = await axios({
      headers: {
        "Turbolinks-Referrer": location.href,
      },
      method,
      url,
    });

    const redirect = this.data.get("redirect");
    if (redirect) {
      if (redirect !== "none") Turbolinks.visit(redirect);
      return;
    }

    if (this.data.has("replace")) {
      if (this.hasReplaceTarget) {
        this.replaceTarget.innerHTML = response.data;
      } else {
        this.element.innerHTML = response.data;
      }
      return;
    }

    if (this.data.has("remove")) {
      if (this.hasRemoveTarget) {
        this.removeTarget.remove();
      } else {
        this.element.remove();
      }
      return;
    }
    //
    // default behaviour: redirect passed down in header
    if (!redirect && response.headers["content-type"].match(/javascript/)) {
      /* eslint-disable-next-line no-eval */
      eval(response.data);
    }
  }
}
