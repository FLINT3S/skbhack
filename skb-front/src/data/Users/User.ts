import type {Account} from "../Account";
import {API} from "../../utils/constants";
import axios from "axios";

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
    return new Promise((resolve, reject) => {
      if (this.blocked) {
        reject("User is already blocked")
        return
      }

      axios.post(`${API}/admin/block_user`, {login: this.login})
        .then(() => {
          resolve(true)
        })
        .catch((error) => {
          reject(error)
        })
    })
  }

  unblock(): Promise<boolean> {
    return new Promise((resolve, reject) => {
      if (!this.blocked) {
        reject("User is already blocked")
        return
      }

      axios.post(`${API}/admin/unblock_user`, {login: this.login})
        .then(() => {
          resolve(true)
        })
        .catch((error) => {
          reject(error)
        })
    })
  }

  accept(): Promise<boolean> {
    return new Promise((resolve, reject) => {
      axios.post(`${API}/admin/verify_user`, {login: this.login})
        .then(() => {
          resolve(true)
        })
        .catch((error) => {
          reject(error)
        })
    })
  }

  dismiss(): Promise<boolean> {
    return new Promise((resolve, reject) => {
      axios.post(`${API}/admin/dismiss_user`, {login: this.login})
        .then(() => {
          resolve(true)
        })
        .catch((error) => {
          reject(error)
        })
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
