<template>
  <div class="account-cell d-flex">
    <div class="icon me-3"
         :style="{background: account.currency.color, borderColor: blendRGB(account.currency.color, -40), color: blendRGB(account.currency.color, -100)}">
      {{ account.currency.symbol }}
    </div>
    <div class="info d-flex flex-column">
      <n-h5 class="amount mb-2 fw-bold">{{ account.formatAmount }}</n-h5>
      <span class="title text-secondary">{{ account.title || 'Счёт в ' + account.currency.symbol }}</span>
    </div>
  </div>
</template>

<script setup lang="ts">
import type {Account} from "../data/Account";
import {blendRGB} from "../utils/colors";

const props = defineProps<{
  account: Account
}>()
</script>

<style scoped>
.icon {
  aspect-ratio: 1/1;
  width: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 100px;
  font-size: 26px;
  border-style: solid;
  border-width: 3px;
}
</style>
