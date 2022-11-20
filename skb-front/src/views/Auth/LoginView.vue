<template>
  <section>
    <span class="auth-screen-header">Вход</span>

    <n-space class="mt-5" vertical>
      <n-input v-model:value="loginData.login" placeholder="Логин"/>
      <n-input
          v-model:value="loginData.password"
          placeholder="Пароль"
          type="password"
      />
    </n-space>

    <div v-if="loginError" class="mt-3 text-danger">
      {{ loginError }}
    </div>

    <n-button
        :disabled="!(loginData.login && loginData.password)"
        block
        class="button-enter"
        round
        size="large"
        type="primary"
        @click="onClickSubmitLogin"
    >
      Войти
    </n-button>

    <router-link class="sub-action-auth mt-4 d-block" to="/auth/register">
      Зарегистрироваться
    </router-link>
  </section>
</template>

<script lang="ts" setup>
import {storeToRefs} from "pinia";
import {useAuthStore} from "../../stores/auth";
import {useRouter} from "vue-router";

const {loginData} = storeToRefs(useAuthStore());
const {submitLogin} = useAuthStore();

const router = useRouter();
const loginError = ref("");

const onClickSubmitLogin = () => {
  submitLogin()
      .then(() => {
        router.replace("/")
      })
      .catch((e) => {
        if (e === "VERIFY") {
          router.replace("/auth/verify");
        } else if (e === "BLOCK") {
          router.replace("/auth/block");
        } else {
          loginError.value = e;
        }
      });
};
</script>

<style scoped></style>
