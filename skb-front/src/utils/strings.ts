export function formatMoney(amount: number, currency: string): string {
  let res = amount.toLocaleString('ru-RU', {style: 'currency', currency: currency}).trim()

  if (amount >= 0) {
    res = '+' + res
  }

  return res
}

export function removeSigns(str: string): string {
  return str.replace(/[-+]/g, '')
}
