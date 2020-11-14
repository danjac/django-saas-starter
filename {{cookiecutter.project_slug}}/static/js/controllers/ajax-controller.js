import axios from "axios";
import Turbolinks from "turbolinks";
import { Controller } from "stimulus";

export default class extends Controller {
  // Generic AJAX actions
  // Actions:
  //
  // data-action="ajax#post" : sends a POST
  // data-action="ajax#get" etc
  //
  // Attributes:
  //
  // data-ajax-url: URL endpoint
  // data-ajax-confirm: confirmation dialog message. No confirm dialog will be shown if absent.
  //
  // data-ajax-replace: replaces inner HTML of controller element with HTML returned from server.
  // to replace inner HTML of child element, add data-target="ajax.replace"
  //
  // data-ajax-remove: removes the controller element after successful request.
  // to remove a child element, add data-target="ajax.remove"
  //
  // data-ajax-redirect:
  //
  // If server sends a Turbolinks redirect in the response header, this will be automatically applied if
  // data-ajax-replace or data-ajax-remove attributes are not present. To override this use data-ajax-redirect.
  //
  // For example, if the server sends the redirect "/profile" and data-ajax-redirect="/" then redirect
  // will be sent to "/" not "/profile". If data-ajax-redirect is not present then will automatically
  // redirect to "/profile".
  //
  // If data-ajax-redirect is set to "none" then server redirect is ignored and nothing else happens.

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
