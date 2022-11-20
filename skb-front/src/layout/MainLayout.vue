<template>
  <n-layout class="layout__main" native-scrollbar>
    <n-layout-header
        bordered
        class="layout__main__header"
        style="padding: 20px"
    >
      <div class="container h-100">
        <div class="row h-100">
          <router-link class="col-8 col-md-5 col-lg-3 d-flex" to="/">
            <img
                alt=""
                class="m-auto w-100 header-logo"
                src="../assets/img/skb-logo.svg"
            />
          </router-link>
          <div class="col-lg-8 d-none d-lg-flex justify-content-center">
            <currency-indicator
                v-for="c in currenciesTopList"
                :currency-symbol="c.symbol"
                :growth="c.growth"
                :title="c.ticker"
                :value="c.value || 0"
                class="mx-4"
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
    <n-layout class="layout__main__inner" position="absolute" style="top: 86px">
      <n-layout>
        <div class="container pb-3">
          <div class="row mt-4">
            <div class="col-12 col-lg-4">
              <router-link
                  :class="router.currentRoute.value.path === '/' ? 'collapsed' : ''"
                  class="text-decoration-none back-btn"
                  tag="div"
                  to="/"
              >
                <n-card class="mb-3" size="large">
                  <div class="d-flex align-items-center">
                    <div class="material-icons-round">
                      chevron_left
                    </div>
                    <n-h3 class="m-0">
                      Вернуться на главную
                    </n-h3>
                  </div>
                </n-card>
              </router-link>

              <router-link class="text-decoration-none" tag="div" to="/profile">
                <n-card size="small">
                  <n-list hoverable>
                    <n-list-item>
                      <div class="d-flex justify-content-center flex-wrap">
                        <n-avatar :size="60" :src="`https://icotar.com/initials/${cUser.fullName}?fg=da5155&bg=f2f2f2`"
                                  circle></n-avatar>
                        <div class="ms-4 my-auto">
                          <n-h2 class="fw-bold mb-1">{{ cUser.firstname }}</n-h2>
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
                <template #header-extra>
                  <n-button quaternary @click="updateData">
                    <div class="material-icons-round">
                      refresh
                    </div>
                  </n-button>
                </template>
                <div v-if="cUser && cUser.accounts">
                  <n-list clickable hoverable>
                    <n-list-item v-for="a in cUser.accounts" @click="$router.push('/account/' + a.id)">
                      <account-cell :account="a"/>
                    </n-list-item>
                  </n-list>
                  <n-button block class="mt-3" quaternary size="large" type="info"
                            @click="showCreateAccountModal = true">
                    <span class="material-icons-round">add</span>
                    <span>Добавить счёт</span>
                  </n-button>
                </div>
                <div v-else>
                  <n-skeleton class="mt-2" height="55px" repeat="3"></n-skeleton>
                </div>
              </n-card>

              <transition name="fade">
                <n-card v-if="isAdminPanelButtonShown" class="mt-4">
                  <n-button block type="primary" @click="$router.push('/admin')">
                    Панель админиистратора
                  </n-button>
                </n-card>
              </transition>
            </div>
            <div class="col-12 col-lg-8 mt-3 mt-lg-0">
              <slot></slot>
            </div>
          </div>
        </div>
      </n-layout>
    </n-layout>

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
          <div
              v-if="currencies.map(c => ({value: c.id, label: c.ticker})).filter(c => !cUser.accounts.map(a => a.currency.ticker).includes(c.label)).length">
            <n-h4 class="fw-bold">Выберете валюту для нового счёта</n-h4>

            <n-select v-model:value="newSelectedCurrency"
                      :options="currencies.map(c => ({value: c.id, label: c.ticker})).filter(c => !cUser.accounts.map(a => a.currency.ticker).includes(c.label))"></n-select>

            <n-button block class="button-enter" round size="large" type="primary" @click="onClickSubmitCreateAccount">
              Создать счёт
            </n-button>
          </div>
          <div v-else>
            <n-empty description="Все возможные счета созданы!">
            </n-empty>
            <n-button block class="button-enter" round size="large" type="primary"
                      @click="showCreateAccountModal = false">
              Закрыть
            </n-button>
          </div>
        </div>
      </n-card>
    </n-modal>
  </n-layout>
</template>

<script lang="ts" setup>
import type {Ref} from "vue";

import CurrencyIndicator from "../components/CurrencyIndicator.vue";
import AccountCell from "../components/AccountCell.vue";

import {storeToRefs} from "pinia";
import {useRouter} from "vue-router";

import {useUserStore} from "../stores/user";
import {useMoneyStore} from "../stores/money";
import type {CurrentUser} from "../data/Users/CurrentUser";

import type {Account} from "../data/Account";
import type {Currency} from "../data/Currency";


const router = useRouter();

const isAdminPanelButtonShown = computed(() => router.currentRoute.value.path !== '/admin' && cUser.value.role === "Admin");

const {
  accounts,
  totalUSD,
  currencies
} = storeToRefs(useMoneyStore()) as {
  accounts: Ref<Account[]>,
  totalUSD: Ref<number>,
  currencies: Ref<Currency[]>,
};

const {user: cUser} = storeToRefs(useUserStore()) as {
  user: Ref<CurrentUser>,
};


const newSelectedCurrency = ref<string | null>(null)
const showCreateAccountModal = ref(false)

const onClickSubmitCreateAccount = () => {
  if (newSelectedCurrency.value) {
    cUser.value.createAccount(newSelectedCurrency.value).then(() => {
      showCreateAccountModal.value = false
      cUser.value.loadAccounts()
    })
  }
}

const updateData = () => {
  cUser.value.loadAccounts()
}

setInterval(() => {
  updateData()
}, 10000)

const currenciesTopList = computed(() => {
  return currencies.value.slice(1, 5)
})
</script>

<style lang="scss" scoped>
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

.back-btn {
  height: 72px;
  overflow: hidden;
  transition: all .3s ease;
  display: block;
  margin-bottom: 24px;
}

.back-btn.collapsed {
  height: 0 !important;
  margin: 0;
}
</style>
