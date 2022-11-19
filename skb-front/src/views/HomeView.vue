<template>
  <main class="container mt-4">
    <div class="row">
      <div class="col-12 col-lg-4">
        <router-link class="text-decoration-none" tag="div" to="/profile">
          <n-card size="small">
            <n-list hoverable>
              <n-list-item>
                <div class="d-flex justify-content-center flex-wrap">
                  <n-avatar :size="60" circle></n-avatar>
                  <div class="ms-4 my-auto">
                    <n-h2 class="fw-bold mb-1">Иван</n-h2>
                    <span class="mt-1 text-secondary">Перейти в профиль</span>
                  </div>
                  <div class="material-icons-round my-auto ms-auto goto-profile">
                    chevron_right
                  </div>
                </div>
              </n-list-item>
            </n-list>
          </n-card>
        </router-link>

        <n-card class="mt-3 mt-lg-4" size="large" title="Ваши счета">
          <n-list clickable hoverable>
            <n-list-item v-for="a in accounts" @click="$router.push('/account/' + a.id)">
              <account-cell :account="a"/>
            </n-list-item>
          </n-list>
          <n-button block class="mt-3" quaternary size="large" type="info" @click="showCreateAccountModal = true">
            <span class="material-icons-round">add</span>
            <span>Добавить счёт</span>
          </n-button>
        </n-card>
      </div>
      <div class="col-12 col-lg-8 mt-3 mt-lg-0">
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
      </div>
    </div>

    <n-modal :show="showCreateAccountModal" mask-closable @close="showCreateAccountModal = false">
      <n-card class="modal-medium" title="Создание нового счёта">
        <template #header-extra>
          <div class="modal-close p-1 cursor-pointer" @click="showCreateAccountModal = false">
            <span class="material-icons-round text-white">
              close
            </span>
          </div>
        </template>

        <div class="text-center w-75 mx-auto">
          <n-h4 class="fw-bold">Выберете валюту для нового счёта</n-h4>

          <n-select v-model:value="newSelectedCurrency"
                    :options="currencies.map(c => ({value: c.id, label: c.title}))"></n-select>

          <n-button block class="button-enter" round size="large" type="primary" @click="onClickSubmitCreateAccount">
            Создать счёт
          </n-button>
        </div>
      </n-card>
    </n-modal>
  </main>
</template>

<script lang="ts" setup>
import {storeToRefs} from "pinia";
import type {Ref} from "vue";

import BalanceChart from "../components/BalanceChart.vue";
import AccountCell from "../components/AccountCell.vue";

import {useMoneyStore} from "../stores/money";
import type {Account} from "../data/Account";
import type {Currency} from "../data/Currency";

const {
  accounts,
  totalUSD,
  groupedAccounts,
  currencies
} = storeToRefs(useMoneyStore()) as {
  accounts: Ref<Account[]>,
  totalUSD: Ref<number>,
  groupedAccounts: Ref<Map<string, Account[]>>,
  currencies: Ref<Currency[]>
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

const newSelectedCurrency = ref(null)
const showCreateAccountModal = ref(false)

const onClickSubmitCreateAccount = () => {
  console.log(newSelectedCurrency.value)
}
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
