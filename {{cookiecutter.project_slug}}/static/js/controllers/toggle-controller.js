import { Controller } from "stimulus";

export default class extends Controller {
  static targets = ["item"];

  connect() {
    // automatically remove elements on page load
    const timeout = parseInt(this.data.get("timeout"));
    if (!isNaN(timeout) && timeout > 0) {
      setTimeout(() => this.remove(), timeout);
    }
  }

  remove() {
    this.itemTargets.forEach((item) => {
      item.setAttribute(
        "style",
        "transition: 1s; transform:translate(400px, 0);"
      );
      item.remove();
    });
  }
}
