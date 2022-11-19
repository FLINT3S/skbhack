import type {Currency} from "./Currency";

export class Account {
  id: string
  currency: Currency
  amount: number
  amountUSD: number

  constructor(id: string, currency: Currency, amount: number, amountUSD: number) {
    this.id = id
    this.currency = currency
    this.amount = amount
    this.amountUSD = amountUSD
  }

  get formatAmount(): string {
    return this.currency.formatAmount(this.amount)
  }

  get title(): string {
    return "Счёт в " + this.currency.title
  }
}
