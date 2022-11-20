import {defineStore} from "pinia";
import {User} from "../data/Users/User";
import {__notVerifiedUsers} from "../stores/_mock/__admin";
import axios from "axios";
import {API} from "../utils/constants";

export const useAdminStore = defineStore("admin", () => {
  const isCurrentUserAdmin = ref(false);

  const commonUsers = ref<User[]>([]);
  const notVerifiedUsers = ref<User[]>([]);


  function loadCommonUsers(): Promise<User[]> {
    return new Promise((resolve, reject) => {
      axios.get(`${API}/admin/verified_users`)
        .then((response) => {
          commonUsers.value = response.data.map((user: any) => new User(user.id, user.login, user.firstname, user.surname, user.verify, user.blocked, user.role));
          resolve(commonUsers.value)
        })
        .catch((error) => {
          console.log(error);
        })
    })
  }

  function loadNotVerifiedUsers(): Promise<User[]> {
    return new Promise((resolve, reject) => {
      axios.get(`${API}/admin/not_verified_users`)
        .then((response) => {
          notVerifiedUsers.value = response.data.map((user: any) => new User(user.id, user.login, user.firstname, user.surname, user.verify, user.blocked, user.role));
          resolve(notVerifiedUsers.value)
        })
        .catch((error) => {
          console.log(error);
        })
    })
  }

  return {
    isCurrentUserAdmin,
    commonUsers,
    loadCommonUsers,
    loadNotVerifiedUsers,
    notVerifiedUsers
  }
})
