import type {Currency} from "../data/Currency";
import {formatMoney, removeSigns} from "../utils/strings";

export type TransactionsData = {
  day: number
  transactions: Transaction[]
}

export class Transaction {
  description: string
  datetime: number
  amount: number
  currency: Currency

  constructor(description: string, datetime: number, amount: number, currency: Currency) {
    this.description = description
    this.datetime = datetime
    this.amount = amount
    this.currency = currency
  }

  get time(): string {
    //return time without seconds
    return new Date(this.datetime).toLocaleTimeString('ru-RU', {hour: '2-digit', minute: '2-digit'})
  }

  get caption(): string {
    return `Перевод ${removeSigns(formatMoney(this.amount, this.currency.ticker))}`
  }
}
