<template>
  <main>
    <n-card size="large" title="Всего на счетах">
      <div class="row">
        <div class="col-12 col-md-6">
              <span class="total-money">
                $ {{ totalUSD.toFixed(2) }}
              </span>

          <div class="mt-5">
            <n-button
                block
                class="button-enter mt-0"
                round
                size="large"
                type="primary"
                @click="$router.push('/converter')"
            >
              Конвертация валют
            </n-button>
            <n-button
                block
                class="button-enter mt-3"
                round
                secondary
                size="large"
                type="primary"
                @click="$router.push('/currencyHistory')"
            >
              Курсы валют и прогнозы
            </n-button>
          </div>
        </div>
        <div class="col-12 col-md-6">
          <balance-chart :chart-data="chartData"/>
        </div>
      </div>
    </n-card>

    <history-list
        :td="td"
        :loading="cUser?.loadingHistory"
    />
  </main>
</template>

<script lang="ts" setup>
import {storeToRefs} from "pinia";
import type {Ref} from "vue";

import BalanceChart from "../components/BalanceChart.vue";
import HistoryList from "../components/HistoryList.vue";

import {useMoneyStore} from "../stores/money";
import type {Account} from "../data/Account";
import type {Currency} from "../data/Currency";
import {useUserStore} from "../stores/user";
import type {TransactionsData} from "../data/Transaction";


const {
  accounts,
  totalUSD,
  groupedAccounts,
  currencies,
  transactionsData: td
} = storeToRefs(useMoneyStore()) as {
  accounts: Ref<Account[]>,
  totalUSD: Ref<number>,
  groupedAccounts: Ref<Map<string, Account[]>>,
  currencies: Ref<Currency[]>,
  transactionsData: Ref<TransactionsData[]>
};

const {user: cUser} = storeToRefs(useUserStore())
const {loadCurrentUserHistory, loadCurrencies} = useMoneyStore()

loadCurrentUserHistory()
cUser.value?.loadAccounts();
loadCurrencies();


const chartData = ref({
  labels: Array.from(groupedAccounts.value.keys()),
  datasets: [
    {
      label: 'Data One',
      backgroundColor: accounts.value.map(a => a.currency.color),
      data: Array.from(groupedAccounts.value.values()).map(a => a.reduce((acc, cur) => acc + cur.amountUSD, 0))
    }
  ]
})
</script>

<style scoped>
.goto-profile {
  font-size: 2rem;
}

.total-money {
  font-size: 46px;
  font-weight: bold;
}
</style>
