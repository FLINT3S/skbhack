<template>
  <n-card class="mt-4" size="large">
    <template #header>
      <div class="d-flex align-items-center">
              <span class="material-icons-round me-2">
                history
              </span>

        <span class="m-0">Недавняя активность</span>
      </div>
    </template>


    <div v-if="loading">
      <n-skeleton class="mt-2" height="55px" repeat="5"></n-skeleton>
    </div>
    <div v-else-if="!loading && !td.length">
      <n-empty description="Нет недавней активности"></n-empty>
    </div>
    <n-list v-for="(transactionsDay, index) in td" v-else class="mt-3">
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
  </n-card>
</template>

<script lang="ts">
import ColorBalance from "../components/ColorBalance.vue";

import {getDayAndMonth} from "../utils/strings";
import type {TransactionsData} from "../data/Transaction";
import type {PropType} from "vue";

export default defineComponent({
  name: "HistoryList",
  components: {
    ColorBalance
  },
  props: {
    td: {
      type: Array as PropType<TransactionsData[]>,
      default: () => []
    },
    loading: {
      type: Boolean,
      default: false
    }
  },
  computed: {},
  methods: {
    getDayAndMonth
  }
});

</script>

<style scoped>

</style>
