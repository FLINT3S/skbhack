<template>
  <n-config-provider :theme="lightTheme" :locale="ruRU" :date-locale="dateRuRU" :theme-overrides="themeOverrides">
    <component :is="layout">
      <n-message-provider>
        <router-view v-slot="{ Component }">
          <transition name="fade">
            <component :is="Component" />
          </transition>
        </router-view>
      </n-message-provider>
    </component>
  </n-config-provider>
</template>

<script setup lang="ts">
import {
  lightTheme,
  dateRuRU,
  NConfigProvider,
  NMessageProvider,
  ruRU,
} from "naive-ui";
import { useRoute } from "vue-router";
import EmptyLayout from "./layout/EmptyLayout.vue";
import { computed } from "vue";
import themeOverrides from "./assets/styles/theme/naive-ui-theme-overrides.json";

const route = useRoute();
const layout = computed(() => {
  return route.meta?.layout || EmptyLayout;
});
</script>

<style scoped></style>
