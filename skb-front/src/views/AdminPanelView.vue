<template>
  <n-card title="Панель администратора">
    <div>
      <n-tabs type="segment">
        <n-tab-pane name="admin" tab="Oasis">
          <div class="mt-3">
            <n-list>
              <n-list-item
                  v-for="user in commonUsers"
              >
                <user-cell
                    :blocked="user.blocked"
                    :fullName="user.fullName"
                    :role="user.roleTitle"
                    @block="onClickBlock(user)"
                    @change-balance="onClickChangeBalance(user)"
                />
              </n-list-item>
            </n-list>
          </div>
        </n-tab-pane>
        <n-tab-pane name="request" tab="Запросы на модерацию">
          <div class="mt-3">
            <n-list>
              <n-list-item
                  v-for="user in commonUsers"
              >
                <user-cell
                    :blocked="user.blocked"
                    :fullName="user.fullName"
                    :role="user.roleTitle"
                    @block="onClickBlock(user)"
                    @change-balance="onClickChangeBalance(user)"
                >

                </user-cell>
              </n-list-item>
            </n-list>
          </div>
        </n-tab-pane>
      </n-tabs>
    </div>

    <n-modal :show="showChangeBalanceModal" class="modal-medium" title="Изменение баланса"
             @close="showChangeBalanceModal = false">
      <n-card title="Изменить баланс">
        <template #header-extra>
          <div class="modal-close p-1 cursor-pointer" @click="showChangeBalanceModal = false">
            <span class="material-icons-round text-white">
              close
            </span>
          </div>
        </template>


        <div class="text-center w-75 mx-auto">
          <n-h4>Выберете счёт</n-h4>
          <div v-if="selectedUser?.loadingAccounts">
            <n-skeleton height="35px"></n-skeleton>
            <n-skeleton class="mt-2" height="35px"></n-skeleton>
            <n-skeleton class="mx-auto mt-2" height="75px" width="150px"></n-skeleton>
          </div>
          <div v-else>
            <n-select
                :options="selectedUserAccounts"
            />
            <n-input
                v-model:value="changeBalanceNewValue"
                class="mt-2"
                type="number"
            ></n-input>

            <n-button
                class="button-enter"
                round
                type="primary"
                @click="onClickSubmitChangeBalance"
            >
              Измениить баланс
            </n-button>
          </div>
        </div>
      </n-card>
    </n-modal>
  </n-card>
</template>

<script lang="ts" setup>
import UserCell from "../components/UserCell.vue";
import type {User} from "../data/Users/User";
import {storeToRefs} from "pinia";
import {useAdminStore} from "../stores/admin";

const dialog = useDialog()
const message = useMessage()

const {commonUsers} = storeToRefs(useAdminStore());

const showChangeBalanceModal = ref(false);
const selectedUser = ref<User | null>(null);

const changeBalanceNewValue = ref("0");

const selectedUserAccounts = computed(() => {
  if (selectedUser.value === null) {
    return [];
  }

  return selectedUser.value.accounts.map(account => {
    return {
      label: account.title,
      value: account.id,
    }
  });
});

const onClickChangeBalance = (user: User) => {
  selectedUser.value = user
  user?.loadAccounts()
  showChangeBalanceModal.value = true;
}

const onClickBlock = (user: User) => {
  selectedUser.value = user

  if (selectedUser.value.blocked) {
    dialog.success({
      title: 'Вы уверены?',
      content: 'Вы действительно хотите разблокировать пользователя?',
      positiveText: 'Заблокировать',
      negativeText: 'Отмена',
      onPositiveClick: () => {
        selectedUser.value?.unblock()
      },
      onNegativeClick: () => {
      }
    })
  } else {
    dialog.error({
      title: 'Вы уверены?',
      content: 'Вы действительно хотите заблокировать пользователя?',
      positiveText: 'Заблокировать',
      negativeText: 'Отмена',
      onPositiveClick: () => {
        selectedUser.value?.block()
      },
      onNegativeClick: () => {
      }
    })
  }
}

const onClickSubmitChangeBalance = () => {

}
</script>
<style scoped>

</style>
