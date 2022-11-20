<template>
  <n-config-provider
      :date-locale="dateRuRU"
      :locale="ruRU"
      :theme="lightTheme"
      :theme-overrides="themeOverrides"
  >
    <transition mode="out-in" name="fade">
      <component :is="layout">
        <n-dialog-provider>
          <n-message-provider>
            <router-view v-slot="{ Component }">
              <transition mode="out-in" name="fade">
                <component :is="Component"/>
              </transition>
            </router-view>
          </n-message-provider>
        </n-dialog-provider>
      </component>
    </transition>
  </n-config-provider>
</template>

<script lang="ts" setup>
import {dateRuRU, lightTheme, NConfigProvider, NMessageProvider, ruRU,} from "naive-ui";
import {useRoute, useRouter} from "vue-router";
import EmptyLayout from "./layout/EmptyLayout.vue";
import {computed} from "vue";
import themeOverrides from "./assets/styles/theme/naive-ui-theme-overrides.json";
import {parseJwt} from "./utils/other";
import {storeToRefs} from "pinia";
import {useUserStore} from "./stores/user";
import {CurrentUser} from "./data/Users/CurrentUser";
import {useMoneyStore} from "./stores/money";

const router = useRouter();
const {user: globalUser, token: globalToken} = storeToRefs(useUserStore())
const {loadCurrencies} = useMoneyStore()

const token = localStorage.getItem("token") || "";
if (token) {
  try {
    const user = parseJwt(token) as CurrentUser;

    globalToken.value = token;
    globalUser.value = new CurrentUser(user.id, user.login, user.firstname, user.surname, user.verify, user.blocked, user.role);
    globalUser.value.loadAccounts();
    loadCurrencies();
  } catch (e) {
    localStorage.removeItem("token");
    router.push("/auth/login");
  }
} else {
  router.replace("/auth/login");
}

const route = useRoute();
const layout = computed(() => {
  return route.meta?.layout || EmptyLayout;
});
</script>

<style scoped></style>
