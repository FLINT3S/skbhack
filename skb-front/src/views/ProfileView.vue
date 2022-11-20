<template>
  <section>
    <n-card title="Профиль">
      <div class="d-flex align-items-center">
        <n-avatar :size="144" :src="`https://icotar.com/initials/${cUser.fullName}?fg=da5155&bg=f2f2f2`"
                  circle></n-avatar>
        <div class="ms-4">
          <n-h1 class="fw-bold m-0 mb-2">{{ cUser.fullName }}</n-h1>
          <span class="text-secondary">@{{ cUser.login }}</span>
        </div>
      </div>

      <div class="row mt-5 text-center fw-light">
        <div class="col-12 col-lg-4">Паспорт: 18 48 ****12</div>
        <div class="col-12 col-lg-4">ИНН: 456253263552</div>
        <div class="col-12 col-lg-4">СНИЛС: не указано</div>
      </div>
    </n-card>

    <history-list
        :loading="cUser?.loadingHistory"
        :td="td"
    ></history-list>
  </section>
</template>

<script lang="ts" setup>
import HistoryList from "../components/HistoryList.vue";

import {storeToRefs} from "pinia";
import {useUserStore} from "../stores/user";
import {useMoneyStore} from "../stores/money";

import type {Ref} from "vue";
import type {CurrentUser} from "../data/Users/CurrentUser";
import type {TransactionsData} from "../data/Transaction";

const {user: cUser} = storeToRefs(useUserStore()) as {
  user: Ref<CurrentUser>,
};

const {
  transactionsData: td
} = storeToRefs(useMoneyStore()) as {
  transactionsData: Ref<TransactionsData[]>
};
const {loadCurrentUserHistory, loadCurrencies} = useMoneyStore()

loadCurrentUserHistory()
</script>

<style scoped>

</style>
