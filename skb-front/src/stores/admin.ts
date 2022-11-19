import {defineStore} from "pinia";

const useAdminStore = defineStore("admin", () => {
  const isCurrentUserAdmin = ref(false);

  const adminPanelUsers = ref([]);

  return {
    isCurrentUserAdmin,
  }
})
