import {defineStore} from "pinia";

export const useUserStore = defineStore('user', () => {
  const token = ref<null | string>(null);
  const user = ref(null);

  return {
    token,
    user,
  }
})
