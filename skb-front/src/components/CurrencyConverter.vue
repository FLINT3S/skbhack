<template>
  <n-card title="Конвертация валют">
    <div class="mb-3 text-secondary text-center">
      Выберете справа две валюты (между которыми нужно сделать перевод) и введите сумму для конвертации
    </div>

    <div class="row align-items-center">
      <div class="col-1">
        <div>Из:</div>
      </div>
      <div class="col-8">
        <n-input
            v-model:value="fromValue"
            :disabled="!fromCurrency || !toCurrency"
            :suffix="fromCurrency"
            type="number"
        />
      </div>
      <div class="col-3">
        <n-select
            v-model:value="fromCurrency"
            :options="fromCurrencies"
            placeholder="Выберите валюту"
        />
      </div>
    </div>
    <div class="row align-items-center mt-3">
      <div class="col-1">
        <div>В:</div>
      </div>
      <div class="col-8">
        <n-input
            :disabled="!fromCurrency || !toCurrency"
            :suffix="fromCurrency"
            :value="toValue"
            readonly
            type="number"
        />
      </div>
      <div class="col-3">
        <n-select
            v-model:value="toCurrency"
            :options="toCurrencies"
            placeholder="Выберите валюту"
        />
      </div>
    </div>

    <n-h1 v-if="fromValue" class="text-center">
      {{ fromValue || 1 }} {{ from?.ticker }} = {{ ((fromValue || 1) * rate).toFixed(2) }} {{ to?.ticker }}
    </n-h1>

    <n-button
        :disabled="!fromCurrency || !toCurrency || !fromValue || (fromValue && fromAccount && fromAccountBalance < fromValue)"
        block
        class="button-enter mt-5"
        round
        size="large"
        type="primary"
        @click="onClickSubmitConvert"
    >
      Конвертировать
    </n-button>

    <div v-if="fromValue && fromAccount && fromAccountBalance < fromValue" class="text-danger text-center mt-2">
      Недостаточно средств на счете
    </div>
  </n-card>
</template>

<script lang="ts" setup>
import {storeToRefs} from "pinia";
import {useUserStore} from "../stores/user";
import {useMoneyStore} from "../stores/money";
import type {Ref} from "vue";
import type {Currency} from "../data/Currency";

const {user: cUser} = storeToRefs(useUserStore())

const {currencies} = storeToRefs(useMoneyStore()) as { currencies: Ref<Currency[]> };

const fromCurrency = ref<string | null>(null)
const toCurrency = ref<string | null>(null)
const fromValue = ref(0)

const toValue = computed(() => {
  if (!fromValue) return ""
  return (fromValue.value * rate.value).toFixed(2)
})

const fromCurrencies = computed(() => currencies.value
    .filter(c => cUser.value?.accounts
        .map(a => a.currency.ticker).includes(c.ticker) && c.id !== toCurrency.value).map(c => ({
      value: c.id,
      label: c.ticker
    })))
const toCurrencies = computed(() => currencies.value
    .filter(c => cUser.value?.accounts
        .map(a => a.currency.ticker).includes(c.ticker) && c.id !== fromCurrency.value).map(c => ({
      value: c.id,
      label: c.ticker
    })))


const from = computed(() => currencies.value.find(c => c.id === fromCurrency.value))
const to = computed(() => currencies.value.find(c => c.id === toCurrency.value))

const fromAccount = computed(() => cUser.value?.accounts?.find(a => a.currency.ticker === from.value!.ticker))
const fromAccountBalance = computed(() => fromAccount.value?.amount)


const rate = computed(() => {
  const from = currencies.value.find(c => c.id === fromCurrency.value)
  const to = currencies.value.find(c => c.id === toCurrency.value)

  if (from && to) {
    return from.value! / to.value!
  }
  return 0
})

const message = useMessage()

const onClickSubmitConvert = async () => {
  const fromAccount = cUser.value?.accounts.find(a => a.currency.ticker === from.value!.ticker)
  const toAccount = cUser.value?.accounts.find(a => a.currency.ticker === to.value!.ticker)

  if (fromAccount) {
    fromAccount.transferTo(toAccount!, fromValue.value).catch(() => {
      message.error("Не удалось конвертировать валюту")
    })
    cUser.value?.loadAccounts();
  }
}
</script>

<style scoped>

</style>
