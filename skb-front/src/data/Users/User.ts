import type {Account} from "../Account";

export class User {
  id: string;
  login: string;
  firstname: string;
  surname: string;
  createdAt?: number;
  verify?: boolean;
  blocked?: boolean;
  role?: string;
  accounts: Account[] = [];
  loadingAccounts: boolean = false;

  constructor(id: string, login: string, firstname: string, surname: string,
              verify: boolean = false, blocked: boolean = false, role: string = "User") {
    this.id = id;
    this.login = login;
    this.firstname = firstname;
    this.surname = surname;
    this.verify = verify;
    this.blocked = blocked;
    this.role = role;
  }

  get fullName(): string {
    return this.firstname + " " + this.surname
  }

  get roleTitle(): string {
    return this.role === "Admin" ? "Администратор" : "Пользователь"
  }

  block(): Promise<boolean> {
    console.log("block");

    return new Promise((resolve, reject) => {
      if (this.blocked) {
        reject("User is already blocked")
      }
      resolve(true)
    })
  }

  unblock(): Promise<boolean> {
    console.log("unblock");
    return new Promise((resolve, reject) => {
      if (!this.blocked) {
        reject("User is not blocked")
      }
      resolve(true)
    })
  }

  loadAccounts(): Promise<Account[]> {
    this.loadingAccounts = true;

    return new Promise((resolve, reject) => {
      resolve(this.accounts)
      console.log("loadAccounts");
      this.loadingAccounts = false;
    })
  }
}
