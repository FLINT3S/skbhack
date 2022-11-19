<template>
  <section>
    <span class="auth-screen-header">Вход</span>

    <n-space vertical class="mt-5">
      <n-input placeholder="Логин" v-model:value="loginData.email" />
      <n-input
        v-model:value="loginData.password"
        placeholder="Пароль"
        type="password"
      />
    </n-space>

    <n-button
      block
      type="primary"
      round
      size="large"
      class="button-enter"
      :disabled="!(loginData.email && loginData.password)"
      @click="onClickSubmitLogin"
    >
      Войти
    </n-button>

    <router-link to="/auth/register" class="sub-action-auth mt-4 d-block">
      Зарегистрироваться
    </router-link>
  </section>
</template>

<script setup lang="ts">
import { storeToRefs } from "pinia";
import { useAuthStore } from "../../stores/auth";

const { loginData } = storeToRefs(useAuthStore());
const { submitLogin } = useAuthStore();

const onClickSubmitLogin = () => {
  submitLogin();
};
</script>

<style scoped></style>
