<template>
  <main>
    <n-card size="large" title="Всего на счетах">
      <div class="row">
        <div class="col-12 col-md-6">
              <span class="total-money">
                $ {{ totalUSD }}
              </span>

          <div class="mt-5">
            <n-button
                block
                class="button-enter mt-0"
                round
                size="large"
                type="primary"
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

    <n-card class="mt-4" size="large">
      <template #header>
        <div class="d-flex align-items-center">
              <span class="material-icons-round me-2">
                history
              </span>

          <span class="m-0">Недавняя активность</span>
        </div>
      </template>

      <n-list v-for="(transactionsDay, index) in td" v-if="td.length > 0 && !cUser?.loadingHistory" class="mt-3">
        <n-h2 class="mb-2">{{ getDayAndMonth(transactionsDay.day * 1000, true).toLowerCase() }}</n-h2>

        <n-list-item v-for="t in transactionsDay.transactions">
          <div class="d-flex justify-content-between">
            <div class="text-start">
              <n-h3 class="fw-bold">
                {{ t.description }}
              </n-h3>

              <div>
                {{ t.caption }}
              </div>
            </div>

            <div class="d-flex flex-column text-end">
              <color-balance :transaction-item="t"/>

              <span class="mt-3 text-secondary">
                    {{ t.time }}
              </span>
            </div>
          </div>
        </n-list-item>
      </n-list>
      <div v-else>
        <n-skeleton class="mt-2" height="55px" repeat="5"></n-skeleton>
      </div>
    </n-card>
  </main>
</template>

<script lang="ts" setup>
import {storeToRefs} from "pinia";
import type {Ref} from "vue";

import BalanceChart from "../components/BalanceChart.vue";
import ColorBalance from "../components/ColorBalance.vue";

import {getDayAndMonth} from "../utils/strings";

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

const {loadCurrentUserHistory} = useMoneyStore()
loadCurrentUserHistory()

const {user: cUser} = storeToRefs(useUserStore())


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
