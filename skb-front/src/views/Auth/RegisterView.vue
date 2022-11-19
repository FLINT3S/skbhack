<template>
  <section>
    <span class="auth-screen-header">Регистрация</span>

    <n-space vertical class="mt-5">
      <n-input placeholder="Логин" v-model:value="registerData.email" />
      <n-input
        v-model:value="registerData.password"
        placeholder="Пароль"
        type="password"
      />
      <n-input
        v-model:value="registerData.passwordConfirmation"
        placeholder="Ещё раз пароль"
        type="password"
      />
    </n-space>

    <n-button
      block
      type="primary"
      round
      size="large"
      class="button-enter"
      :disabled="
        !(
          registerData.email &&
          registerData.password &&
          registerData.passwordConfirmation
        )
      "
      @click="onClickSubmitRegister"
    >
      Зарегистрироваться
    </n-button>

    <router-link to="/auth/login" class="sub-action-auth mt-4 d-block">
      Войти
    </router-link>
  </section>
</template>

<script setup lang="ts">
import { storeToRefs } from "pinia";
import { useAuthStore } from "../../stores/auth";

const { registerData } = storeToRefs(useAuthStore());
const { submitRegister } = useAuthStore();

const onClickSubmitRegister = () => {
  submitRegister();
};
</script>

<style scoped></style>
