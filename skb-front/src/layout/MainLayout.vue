<template>
  <n-layout class="layout__main" native-scrollbar>
    <n-layout-header
        class="layout__main__header"
        style="padding: 20px"
        bordered
    >
      <div class="container h-100">
        <div class="row h-100">
          <router-link class="col-8 col-md-5 col-lg-3 d-flex" to="/">
            <img
                src="../assets/img/skb-logo.svg"
                class="m-auto w-100 header-logo"
                alt=""
            />
          </router-link>
          <div class="col-lg-8 d-none d-lg-flex justify-content-center">
            <currency-indicator
                class="mx-4"
                v-for="c in currencies"
                :title="c.ticker"
                :value="c.value || 0"
                :currency-symbol="c.symbol"
                :growth="c.growth"
            />
          </div>
          <div class="col ms-md-0 ms-lg-auto d-flex">
            <router-link
                class="mt-auto mb-auto ms-auto material-icons-round logout"
                to="/auth/logout"
            >
              logout
            </router-link>
          </div>
        </div>
      </div>
    </n-layout-header>
    <n-layout position="absolute" class="layout__main__inner" style="top: 86px">
      <n-layout>
        <div class="container pb-3">
          <slot></slot>
        </div>
      </n-layout>
    </n-layout>
  </n-layout>
</template>

<script setup lang="ts">
import {NLayout} from "naive-ui";
import CurrencyIndicator from "../components/CurrencyIndicator.vue";
import {storeToRefs} from "pinia";
import {useMoneyStore} from "../stores/money";
import type {Currency} from "../data/Currency";
import type {Ref} from "vue";

const {currencies}: { currencies: Ref<Currency[]> } = storeToRefs(useMoneyStore());
</script>

<style scoped lang="scss">
.layout__main {
  min-height: 100vh;
}

.header-logo {
  width: 100%;

  @media screen and (max-width: 576px) {
    max-width: 220px;
  }
}

.layout__main__header {
  height: 84px;
}

.layout__main__inner {
  top: 84px;
}

@media screen and (max-width: 576px) {
  .layout__main__header {
    height: 72px;
  }

  .layout__main__inner {
    top: 72px;
  }
}

.logout {
  text-decoration: none;
  cursor: pointer;
  color: var(--accent-blue);
  transition: color 0.2s ease-in-out, text-shadow 0.2s ease-in-out;

  &:hover {
    color: var(--accent-blue-hover);
    text-shadow: 0 0 1px rgba(15, 31, 75, 0.7);
  }
}
</style>
