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
import {useRoute} from "vue-router";
import EmptyLayout from "./layout/EmptyLayout.vue";
import {computed} from "vue";
import themeOverrides from "./assets/styles/theme/naive-ui-theme-overrides.json";
import {parseJwt} from "./utils/other";

const token = localStorage.getItem("token") || "";
const user = parseJwt(token);

const route = useRoute();
const layout = computed(() => {
  return route.meta?.layout || EmptyLayout;
});
</script>

<style scoped></style>
