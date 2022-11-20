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
import {parseJwt} from "../../utils/other";
import {CurrentUser} from "../../data/Users/CurrentUser";
import {useUserStore} from "../../stores/user";
import {useMoneyStore} from "../../stores/money";

const {loginData} = storeToRefs(useAuthStore());
const {submitLogin} = useAuthStore();

const router = useRouter();
const loginError = ref("");

const {user: cUser, token: globalToken} = storeToRefs(useUserStore())
const {loadCurrencies} = useMoneyStore()

const onClickSubmitLogin = () => {
  submitLogin()
      .then(() => {
        const token = localStorage.getItem("token") || "";
        if (token) {
          try {
            const user = parseJwt(token) as CurrentUser;

            cUser.value = new CurrentUser(user.id, user.login, user.firstname, user.surname, user.verify, user.blocked, user.role);
            cUser.value.loadAccounts();
            loadCurrencies();
          } catch (e) {
            localStorage.removeItem("token");
            router.push("/auth/login");
          }
        } else {
          router.replace("/auth/login");
        }

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
