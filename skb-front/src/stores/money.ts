import {computed, ref} from "vue";
import {defineStore, storeToRefs} from "pinia";
import axios from "axios";

import {useUserStore} from "../stores/user";

import {Currency} from "../data/Currency";
import type {TransactionsData} from "../data/Transaction";
import {API} from "../utils/constants";
import type {Account} from "../data/Account";


export const useMoneyStore = defineStore('money', () => {
  const {user: cUser} = storeToRefs(useUserStore())

  const currencies = ref<Currency[]>([])
  const accounts = computed(() => cUser.value?.accounts ?? [])

  const totalUSD = computed(() => accounts.value.reduce((acc, account) => acc + account.amountUSD, 0))

  const transactionsData = ref<TransactionsData[]>([])

  const groupedAccounts = computed(() => {
    const grouped = new Map<string, Account[]>()

    cUser.value?.accounts?.forEach(account => {
      const key = account.currency.ticker
      const group = grouped.get(key) || []
      group.push(account)
      grouped.set(key, group)
    })

    return grouped
  })

  function loadCurrencies(): Promise<Currency[]> {
    return new Promise(resolve => {
      axios.get(`${API}/balance/currencies`).then(({data}) => {
        // @ts-ignore
        currencies.value = data.map((currency: Currency) => Currency.fromJSON({...currency, value: currency.rate}))
        resolve(currencies.value)
      })
    })
  }

  function loadCurrentUserHistory(): Promise<TransactionsData[]> {
    return new Promise(resolve => {
      cUser.value!.loadHistory().then(data => {
        transactionsData.value = data
        resolve(transactionsData.value)
      })
    })
  }

  return {
    accounts,
    currencies,
    totalUSD,
    groupedAccounts,
    transactionsData,
    loadCurrencies,
    loadCurrentUserHistory
  }
});
