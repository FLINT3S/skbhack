<template>
  <section>
    <n-card>
      <div class="d-flex flex-wrap">
        <div>
          <div :style="{
        background: currentAccount.currency.color,
        borderColor: blendRGB(currentAccount.currency.color, -40),
        color: blendRGB(currentAccount.currency.color, -100)
      }"
               class="curr-icon me-3"
          >
            {{ currentAccount.currency.symbol }}
          </div>


          <n-h1 class="fw-bold mt-3">{{
              removeSigns(formatMoney(currentAccount.amount, currentAccount.currency.ticker))
            }}
          </n-h1>
        </div>

        <div class="ms-auto text-secondary d-flex small flex-column text-end">
          <span>Идентификатор счёта:<br>{{ currentAccount.id }}</span>
        </div>
      </div>
    </n-card>
    <currency-converter class="mt-4" @convert="loadHistory"/>

    <n-card class="mt-4" title="Курс валюты">
      <n-table :bordered="false" :single-line="false">
        <thead>
        <tr>
          <th>Валюта</th>
          <th>Покупка</th>
          <th>Продажа</th>
        </tr>
        </thead>
        <tbody>
        <tr>
          <td>{{ currentAccount.currency.symbol }}</td>
          <td>{{ currentCurrencyCost }}</td>
          <td>{{ currentCurrencyCost }}</td>
        </tr>
        </tbody>
      </n-table>
    </n-card>

    <history-list
        :td="historyListAccount"
    />
  </section>
</template>

<script lang="ts" setup>
import CurrencyConverter from "../components/CurrencyConverter.vue";
import {useRouter} from "vue-router";
import {useUserStore} from "../stores/user";
import {storeToRefs} from "pinia";
import {blendRGB} from "../utils/colors";
import {formatMoney, removeSigns} from "../utils/strings";
import {useMoneyStore} from "../stores/money";
import type {Ref} from "vue";
import type {Currency} from "../data/Currency";
import HistoryList from "@/components/HistoryList.vue";
import axios from "axios";
import {API} from "../utils/constants";

const router = useRouter();
const {currencies} = storeToRefs(useMoneyStore()) as { currencies: Ref<Currency[]> };
const {user: cUser} = storeToRefs(useUserStore())

const currentAccount = computed(() => cUser.value!.accounts.find(account => account.id === router.currentRoute.value.params.id)!)
const currentCurrencyCost = computed(() => currencies.value.find(currency => currency.ticker === currentAccount.value.currency.ticker)!.value?.toFixed(2))
const historyListAccount = ref([])

const loadHistory = () => {
  axios.get(`${API}/balance/accountHistory/${currentAccount.value.id}`)
      .then(res => {
        historyListAccount.value = res.data
      })
}

watchEffect(() => {
  console.log(router.currentRoute.value.params.id)
  loadHistory()
})

loadHistory()
</script>

<style scoped>
.curr-icon {
  width: 36px;
  height: 36px;
  font-size: 26px;
  text-align: center;
  border-radius: 100px;
  border-width: 2px;
  border-style: solid;
}

.small {
  font-size: 12px;
}
</style>
