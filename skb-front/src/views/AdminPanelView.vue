<template>
  <n-card title="Панель администратора">
    <div class="ro">
      <n-tabs type="segment">
        <n-tab-pane name="admin" tab="Oasis">
          <div class="mt-3">
            <user-cell
                @change-balance="onClickChangeBalance"
                @block="onClickBlock"
            />
          </div>
        </n-tab-pane>
        <n-tab-pane name="request" tab="Запросы на модерацию">
          <div class="mt-3">
            Qilixiang
          </div>
        </n-tab-pane>
      </n-tabs>
    </div>
  </n-card>
</template>

<script lang="ts" setup>
import UserCell from "../components/UserCell.vue";

const onClickChangeBalance = () => {

}
const onClickBlock = () => {

}
</script>
<style scoped>

</style>
