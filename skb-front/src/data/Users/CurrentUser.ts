import {User} from "../Users/User";
import {API} from "../../utils/constants";
import type {Currency} from "../../data/Currency";
import axios from "axios";

export class CurrentUser extends User {
  createAccount(currency: Currency): Promise<boolean> {
    return new Promise((resolve, reject) => {
      axios.post(`${API}/balance/createAccount`, {user_id: this.id, currency_id: currency.id})
        .then(() => {
          resolve(true)
        })
        .catch((error) => {
          reject(error)
        })
    })
  }
}
