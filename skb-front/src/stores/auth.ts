import type {Ref} from "vue";
import {defineStore} from "pinia";

import axios from "axios";

import {API} from "../utils/constants";
import {LoginData} from "../data/LoginData";
import {RegisterData} from "../data/RegisterData";
import {Credentials} from "../data/Credentials";


export const useAuthStore = defineStore("auth", () => {
  const loginData: Ref<LoginData> = ref(new LoginData());
  const registerData: Ref<RegisterData> = ref(new RegisterData());

  function submitRegister() {
    return new Promise((resolve, reject) => {
      axios.post(`${API}/auth/register`, registerData.value)
        .then((response) => {
          Credentials.onLogin(response.data);
          resolve(response.data);
        })
        .catch((error) => {
          reject(error?.response?.data?.detail);
        });
    })
  }

  function submitLogin(): Promise<void | string> {
    return new Promise(async (resolve, reject) => {
      axios.post(`${API}/auth/login`, loginData.value)
        .then((response) => {
          console.log(response)
          Credentials.onLogin(response.data);
          resolve(response.data);
        })
        .catch((error) => {
          if (error?.response?.data?.detail) {
            reject(error?.response?.data?.detail);
            return
          }

          switch (error.code) {
            case 400:
              reject("Неверный логин или пароль")
              break
            case 401:
              reject("Неверный логин или пароль")
              break
            case 403:
              reject("Неверный логин или пароль")
              break
            case 404:
              reject("Неверный логин или пароль")
              break
            case 500:
              reject("Ошибка сервера")
              break
            default:
              reject("Неизвестная ошибка")
          }
        })
    })
  }

  return {
    loginData,
    submitLogin,
    registerData,
    submitRegister,
  };
});
