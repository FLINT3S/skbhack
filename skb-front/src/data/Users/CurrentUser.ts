import {User} from "../Users/User";
import {API} from "../../utils/constants";
import axios from "axios";

import type {TransactionsData} from "../../data/Transaction";
import {Transaction} from "../../data/Transaction";
import {Currency} from "../../data/Currency";

export class CurrentUser extends User {
  userHistory: TransactionsData[] = []
  loadingHistory: boolean = false

  createAccount(currency: string): Promise<boolean> {
    return new Promise((resolve, reject) => {
      axios.post(`${API}/balance/createAccount`, {user_id: this.id, currency_id: currency})
        .then(() => {
          resolve(true)
        })
        .catch((error) => {
          reject(error)
        })
    })
  }

  loadHistory(): Promise<TransactionsData[]> {
    this.loadingHistory = true

    return new Promise((resolve, reject) => {
      axios.get(`${API}/balance/userHistory/${this.id}`)
        .then((response) => {
          const data = response.data as TransactionsData[]
          const res = data.map(d => ({
            ...d,
            transactions: d.transactions.map(t => new Transaction(t.description, t.datetime, t.amount, Currency.fromJSON(t.currency)))
          }))
          this.userHistory = res

          resolve(res)
        })
        .catch((error) => {
          reject(error)
        })
        .finally(() => {
          this.loadingHistory = false
        })
    })
  }
}
