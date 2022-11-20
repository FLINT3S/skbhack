<template>
  <section>
    <n-card title="Исторические данные">
      <div class="d-flex flex-wrap justify-content-center">
        <n-button
            v-for="c in currencies.filter(c => c.ticker !== 'RUB')"
            :secondary="selectedCurrency?.ticker !== c.ticker"
            class="mx-auto my-2"
            size="large"
            type="primary"
            @click="selectCurrency(c)"
        >
          {{ c.ticker }}
        </n-button>
      </div>
    </n-card>

    <n-card class="mt-4">
      <div v-if="loadingData">
        <n-skeleton :repeat="10" :height="32" class="mb-3"></n-skeleton>
      </div>
      <n-table v-else>
        <n-table :bordered="false" :single-line="false">
          <thead>
          <tr>
            <th>Дата</th>
            <th>Цена</th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="d in historyData">
            <td>{{ new Date(d.day * 1000).toLocaleDateString() }}</td>
            <td>{{ d.rate }}</td>
          </tr>
          </tbody>
        </n-table>
      </n-table>
    </n-card>
  </section>
</template>

<script lang="ts" setup>
import axios from "axios";
import {API} from "../utils/constants";
import {storeToRefs} from "pinia";
import {useMoneyStore} from "../stores/money";
import type {Ref} from "vue";
import {Currency} from "../data/Currency";

type hd = {
  day: number,
  rate: number
}

const {currencies} = storeToRefs(useMoneyStore()) as { currencies: Ref<Currency[]> };

const selectedCurrency = ref<Currency>(new Currency("0", "USD", "$", 1))
const loadingData = ref(false)
const historyData = ref<hd[]>([])

const selectCurrency = (c: Currency) => {
  selectedCurrency.value = c

  loadHistoryData(c.ticker)
}

const loadHistoryData = (ticker: string) => {
  loadingData.value = true
  axios.get(`${API}/trading/currencyHistory/${ticker}`)
      .then(res => {
        historyData.value = res.data as hd[]
      })
      .finally(() => {
        loadingData.value = false
      })
}

loadHistoryData('USD')
</script>

<style scoped>

</style>
