import {defineStore} from "pinia";
import type {CurrentUser} from "../data/Users/CurrentUser";

export const useUserStore = defineStore('user', () => {
  const token = ref<string | null>(null);
  const user = ref<CurrentUser | null>(null);

  return {
    token,
    user,
  }
})
