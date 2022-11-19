import {computed, ref} from "vue";
import {defineStore} from "pinia";

import {Account} from "../data/Account";
import {Currency} from "../data/Currency";
import type {TransactionsData} from "../data/Transaction";
import {Transaction} from "../data/Transaction";


const __mockData = {
  currencies: [
    {
      id: 123,
      ticker: "USD",
      value: 22.53,
      currencySymbol: "$",
      growth: true,
    },
    {
      id: 234,
      ticker: "EUR",
      value: 26.53,
      currencySymbol: "€",
      growth: false,
    },
    {
      id: 345,
      ticker: "GBP",
      value: 30.53,
      currencySymbol: "£",
      growth: true,
    },
    {
      id: 456,
      ticker: "CNY",
      value: 3.53,
      currencySymbol: "¥",
      growth: false,
    }
  ],
  accounts: [
    {
      id: "123",
      currency: {
        ticker: "USD",
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
        ticker: "EUR",
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
        ticker: "RUB",
        value: 0.3,
        symbol: "₽",
        growth: true,
      },
      amount: 100000,
      amountUSD: 300,
    }
  ],
  transactionsData: [
    {
      "day": 1668866694,
      "transactions": [
        {
          "description": "Перевод из USD в RUB",
          "datetime": 1668872303,
          "amount": -1.0,
          "currency": {
            "ticker": "USD",
            "symbol": "$"
          }
        },
        {
          "description": "Перевод из USD в RUB",
          "datetime": 1668872303,
          "amount": 60.37409999999999,
          "currency": {
            "ticker": "RUB",
            "symbol": "₽"
          }
        },
        {
          "description": "Перевод из USD в RUB",
          "datetime": 1668866694,
          "amount": -1.0,
          "currency": {
            "ticker": "USD",
            "symbol": "$"
          }
        },
        {
          "description": "Перевод из USD в RUB",
          "datetime": 1668866694,
          "amount": 60.37409999999999,
          "currency": {
            "ticker": "RUB",
            "symbol": "₽"
          }
        },
        {
          "description": "Перевод из USD в RUB",
          "datetime": 1668866693,
          "amount": 60.37409999999999,
          "currency": {
            "ticker": "RUB",
            "symbol": "₽"
          }
        },
        {
          "description": "Перевод из USD в RUB",
          "datetime": 1668866688,
          "amount": 60.37409999999999,
          "currency": {
            "ticker": "RUB",
            "symbol": "₽"
          }
        },
        {
          "description": "Перевод из RUB в USD",
          "datetime": 1668861145,
          "amount": 0.016563393905664848,
          "currency": {
            "ticker": "USD",
            "symbol": "$"
          }
        },
        {
          "description": "Перевод из RUB в USD",
          "datetime": 1668861145,
          "amount": -1.0,
          "currency": {
            "ticker": "RUB",
            "symbol": "₽"
          }
        }
      ]
    },
    {
      "day": 1660917888,
      "transactions": [
        {
          "description": "Перевод из USD в RUB",
          "datetime": 1660917893,
          "amount": -1.0,
          "currency": {
            "ticker": "USD",
            "symbol": "$"
          }
        },
        {
          "description": "Перевод из USD в RUB",
          "datetime": 1660917888,
          "amount": -1.0,
          "currency": {
            "ticker": "USD",
            "symbol": "$"
          }
        }
      ]
    }
  ]
}

export const useMoneyStore = defineStore('money', () => {
  const currencies = ref<Currency[]>(__mockData.currencies.map((currency, index) => new Currency(currency.id, currency.ticker, currency.currencySymbol, currency.value, currency.growth)))

  const accounts = ref<Account[]>(__mockData.accounts.map(account => new Account(account.id, Currency.fromJSON(account.currency), account.amount, account.amountUSD)))

  const totalUSD = computed(() => accounts.value.reduce((acc, account) => acc + account.amountUSD, 0))

  const transactionsData = ref<TransactionsData[]>(__mockData.transactionsData.map(d => ({
    ...d,
    transactions: d.transactions.map(t => new Transaction(t.description, t.datetime, t.amount, Currency.fromJSON(t.currency)))
  })))

  const groupedAccounts = computed(() => {
    const grouped = new Map<string, Account[]>()

    accounts.value.forEach(account => {
      const key = account.currency.ticker
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
    groupedAccounts,
    transactionsData
  }
});
