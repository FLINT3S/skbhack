export const currenciesColors = {
  "RUB": 'rgb(61,191,191)',
  "USD": "rgb(252,188,91)",
  "EUR": "rgb(64,135,201)"
}

export class Currency {
  id: number
  title: string
  symbol: string
  value: number
  growth?: boolean
  color?: string

  constructor(id: number, title: string, symbol: string, value: number, growth?: boolean, color?: string) {
    this.id = id
    this.title = title
    this.symbol = symbol
    this.value = value
    this.growth = growth
    this.color = color || currenciesColors[this.title as keyof typeof currenciesColors]
  }

  static fromJSON(json: any): Currency {
    return new Currency(json.id, json.title, json.symbol, json.value, json.growth, json.color || currenciesColors[json.title as keyof typeof currenciesColors])
  }
}
