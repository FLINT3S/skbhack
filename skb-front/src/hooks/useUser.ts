import {storeToRefs} from "pinia";
import {useUserStore} from "../stores/user";

export default function useUser() {
  const {token, user} = storeToRefs(useUserStore());

  return {
    token,
    user,
  }
}
