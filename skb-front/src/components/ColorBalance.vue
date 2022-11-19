<template>
  <div :class="transactionItem.amount > 0 ? 'green' : 'red'">
    {{ formatMoney(transactionItem.amount, transactionItem.currency.ticker) }}
  </div>
</template>

<script lang="ts">
import type {Transaction} from "../data/Transaction";
import {formatMoney} from "../utils/strings";

import {defineComponent} from "vue";

export default defineComponent({
  props: {
    transactionItem: {
      type: Object as () => Transaction,
      required: true
    }
  },
  methods: {
    formatMoney
  }
})
</script>

<style scoped>
.green {
  color: var(--amount-green)
}

.red {
  color: var(--amount-red)
}
</style>
