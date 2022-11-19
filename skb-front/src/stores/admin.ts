import {defineStore} from "pinia";
import {User} from "../data/Users/User";
import {__notVerifiedUsers} from "../stores/_mock/__admin";

export const useAdminStore = defineStore("admin", () => {
  const isCurrentUserAdmin = ref(false);

  const commonUsers = ref<User[]>(__notVerifiedUsers.map((user) => new User(user.id, user.login, user.firstname, user.surname, user.verify, user.blocked, user.role)));

  return {
    isCurrentUserAdmin,
    commonUsers
  }
})
