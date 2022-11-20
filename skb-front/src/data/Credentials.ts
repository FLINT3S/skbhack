export class Credentials {
  static onLogin(token: string) {
    localStorage.setItem("token", token);
  }

  static onLogout() {
    localStorage.removeItem("token");
  }
}
