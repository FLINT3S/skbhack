<template>
  <section>
    <span class="auth-screen-header">Регистрация</span>

    <n-space class="mt-5" vertical>
      <n-input v-model:value="registerData.login" placeholder="Логин"/>
      <n-input v-model:value="registerData.firstname" placeholder="Имя"/>
      <n-input v-model:value="registerData.surname" placeholder="Фамилия"/>
      <n-input
          v-model:value="registerData.password"
          placeholder="Пароль"
          type="password"
          show-password-on="click"
      />
      <n-input
          v-model:value="registerData.passwordConfirmation"
          placeholder="Ещё раз пароль"
          type="password"
          show-password-on="click"
      />
    </n-space>
    <div
        class="mt-3 text-danger"
        v-if="registerError"
    >
      {{ registerError }}
    </div>

    <n-button
        :disabled="
        !(
          registerData.login &&
          registerData.password &&
          registerData.passwordConfirmation &&
          registerData.firstname &&
          registerData.surname &&
          registerData.password === registerData.passwordConfirmation
        )
      "
        block
        class="button-enter"
        round
        size="large"
        type="primary"
        @click="onClickSubmitRegister"
    >
      Зарегистрироваться
    </n-button>

    <router-link class="sub-action-auth mt-4 d-block" to="/auth/login">
      Войти
    </router-link>
  </section>
</template>

<script lang="ts" setup>
import {storeToRefs} from "pinia";
import {useAuthStore} from "../../stores/auth";
import {useRouter} from "vue-router";

const {registerData} = storeToRefs(useAuthStore());
const {submitRegister} = useAuthStore();

const router = useRouter();

const registerError = ref("");

const onClickSubmitRegister = () => {
  submitRegister().then(() => {
    router.replace("/auth/verify");
  }).catch((e) => {
    registerError.value = e
  });
};
</script>

<style scoped></style>
