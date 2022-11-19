<template>
  <main class="container mt-4">
    <div class="row">
      <router-link class="col-12 col-lg-4 text-decoration-none" to="/profile" tag="div">
        <n-card size="large">
          <div class="d-flex justify-content-center flex-wrap">
            <n-avatar circle :size="60"></n-avatar>
            <div class="ms-4 my-auto">
              <n-h2 class="fw-bold mb-1">Иван</n-h2>
              <span class="mt-1 text-secondary">Перейти в профиль</span>
            </div>
            <div class="material-icons-round my-auto ms-auto goto-profile">
              chevron_right
            </div>
          </div>
        </n-card>
      </router-link>
      <div class="col-12 col-lg-8 mt-3 mt-lg-0">
        <n-card title="Всего на счетах" size="large">
          <div class="row">
            <div class="col-12 col-md-6">
              <span class="total-money">
                $ {{ totalUSD }}
              </span>

              <div class="mt-5">
                <n-button
                    type="primary"
                    round
                    block
                    size="large"
                    class="button-enter mt-0"
                >
                  Конвертация валют
                </n-button>
                <n-button
                    type="primary"
                    secondary
                    round
                    block
                    size="large"
                    class="button-enter mt-3"
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
      </div>
    </div>
  </main>
</template>

<script setup lang="ts">
import BalanceChart from "../components/BalanceChart.vue";
import {storeToRefs} from "pinia";
import {useMoneyStore} from "../stores/money";
import type {Account} from "../data/Account";
import type {Ref} from "vue";

const {
  accounts,
  totalUSD,
  groupedAccounts
} = storeToRefs(useMoneyStore()) as {
  accounts: Ref<Account[]>,
  totalUSD: Ref<number>,
  groupedAccounts: Ref<Map<string, Account[]>>
};

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
