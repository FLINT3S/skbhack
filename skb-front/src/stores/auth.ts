import { defineStore } from "pinia";
import { LoginData } from "../data/LoginData";
import { RegisterData } from "../data/RegisterData";
import type { Ref } from "vue";

export const useAuthStore = defineStore("auth", () => {
  const loginData: Ref<LoginData> = ref(new LoginData());
  const registerData: Ref<RegisterData> = ref(new RegisterData());

  function submitRegister() {
    console.log(312);
  }

  function submitLogin() {
    console.log(123);
  }

  return {
    loginData,
    submitLogin,
    registerData,
    submitRegister,
  };
});
