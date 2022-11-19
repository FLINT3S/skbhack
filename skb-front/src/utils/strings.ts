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


export function getMonthName(month: number, gen: boolean = false): string {
  const months = [
    'Январь',
    'Февраль',
    'Март',
    'Апрель',
    'Май',
    'Июнь',
    'Июль',
    'Август',
    'Сентябрь',
    'Октябрь',
    'Ноябрь',
    'Декабрь'
  ]
  const monthsGen = [
    'Января',
    'Февраля',
    'Марта',
    'Апреля',
    'Мая',
    'Июня',
    'Июля',
    'Августа',
    'Сентября',
    'Октября',
    'Ноября',
    'Декабря'
  ]

  if (gen) {
    return monthsGen[month]
  }

  return months[month]
}

export function getDayAndMonth(datetime: number, gen: boolean = false): string {
  const date = new Date(datetime)
  return `${date.getDate()} ${getMonthName(date.getMonth(), gen)}`
}
