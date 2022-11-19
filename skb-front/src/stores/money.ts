import {computed, ref} from "vue";
import {defineStore} from "pinia";
import {Account} from "../data/Account";
import {Currency} from "../data/Currency";

const __mockData = {
  currencies: [
    {
      id: 123,
      title: "USD",
      value: 22.53,
      currencySymbol: "$",
      growth: true,
    },
    {
      id: 234,
      title: "EUR",
      value: 26.53,
      currencySymbol: "€",
      growth: false,
    },
    {
      id: 345,
      title: "GBP",
      value: 30.53,
      currencySymbol: "£",
      growth: true,
    },
    {
      id: 456,
      title: "CNY",
      value: 3.53,
      currencySymbol: "¥",
      growth: false,
    }
  ],
  accounts: [
    {
      id: "123",
      currency: {
        title: "USD",
        value: 22.53,
        symbol: "$",
        growth: true,
      },
      amount: 1000,
      amountUSD: 1000,
    },
    {
      id: "123",
      currency: {
        title: "EUR",
        value: 26.53,
        symbol: "€",
        growth: false,
      },
      amount: 800,
      amountUSD: 1100,
    },
    {
      id: "123",
      currency: {
        title: "RUB",
        value: 0.3,
        symbol: "₽",
        growth: true,
      },
      amount: 100000,
      amountUSD: 300,
    }
  ]
}

export const useMoneyStore = defineStore('money', () => {
  const currencies = ref<Currency[]>(__mockData.currencies.map((currency, index) => new Currency(currency.id, currency.title, currency.currencySymbol, currency.value, currency.growth)))

  const accounts = ref<Account[]>(__mockData.accounts.map(account => new Account(account.id, Currency.fromJSON(account.currency), account.amount, account.amountUSD)))

  const totalUSD = computed(() => accounts.value.reduce((acc, account) => acc + account.amountUSD, 0))

  const groupedAccounts = computed(() => {
    const grouped = new Map<string, Account[]>()

    accounts.value.forEach(account => {
      const key = account.currency.title
      const group = grouped.get(key) || []
      group.push(account)
      grouped.set(key, group)
    })

    return grouped
  })

  return {
    accounts,
    currencies,
    totalUSD,
    groupedAccounts
  }
});
