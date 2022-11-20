import axios from "axios";

export class Credentials {
  static onLogin(token: string) {
    axios.defaults.headers.common['Authorization'] = token;
    localStorage.setItem("token", token);
  }

  static onLogout() {
    localStorage.removeItem("token");
  }
}
