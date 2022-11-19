<template>
  <div class="user-cell d-flex flex-wrap justify-content-md-between">
    <div>
      <n-h4 class="fw-bold mb-2">Андрей Андреевич И.</n-h4>
      <span class="text-secondary">Пользователь</span>
    </div>

    <div class="actions ms-auto mt-3 mt-md-0">
      <slot>
        <div class="d-flex">
          <n-button class="me-3" type="primary" tertiary @click="$emit('change-balance')">
            Изменить баланс
          </n-button>
          <n-button type="primary" @click="$emit('block')">
            Заблокировать
          </n-button>
        </div>
      </slot>
    </div>
  </div>
</template>

<script lang="ts" setup>
</script>

<style scoped>

</style>
