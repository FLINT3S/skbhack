import type {Currency} from "./Currency";

export class Account {
  currency: Currency
  amount: number
  amountUSD: number

  constructor(currency: Currency, amount: number, amountUSD: number) {
    this.currency = currency
    this.amount = amount
    this.amountUSD = amountUSD
  }
}
