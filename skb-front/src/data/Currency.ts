export const currenciesColors = {
  "RUB": 'rgb(61,191,191)',
  "USD": "rgb(252,188,91)",
  "EUR": "rgb(64,135,201)",
  "GBP": "rgb(201,64,126)",
  "CNY": "rgb(119,64,201)",
  "ISL": "rgb(201,105,64)",
  "KZT": "rgb(139,201,64)",
}

export class Currency {
  id: string
  ticker: string
  symbol: string
  value?: number
  growth?: boolean
  color?: string

  constructor(id: string, ticker: string, symbol: string, value?: number, growth?: boolean, color?: string) {
    this.id = id
    this.ticker = ticker
    this.symbol = symbol
    this.value = value
    this.growth = growth
    this.color = color || currenciesColors[this.ticker as keyof typeof currenciesColors]
  }

  static fromJSON(json: any): Currency {
    return new Currency(json.id, json.ticker, json.symbol, json.value, json.growth, json.color || currenciesColors[json.ticker as keyof typeof currenciesColors])
  }

  formatAmount(amount: number): string {
    return amount.toLocaleString('ru-RU', {style: 'currency', currency: this.ticker})
  }
}
