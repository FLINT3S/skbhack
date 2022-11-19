<template>
  <div class="user-cell d-flex flex-wrap justify-content-md-between">
    <div>
      <n-h4 class="fw-bold mb-2">{{ fullName }}</n-h4>
      <span class="text-secondary">{{ role }}</span>
    </div>

    <div class="actions ms-auto mt-3 mt-md-0">
      <slot>
        <div class="d-flex">
          <n-button class="me-3" tertiary type="primary" @click="$emit('change-balance')">
            <slot name="action-one">
              Изменить баланс
            </slot>
          </n-button>
          <n-button :type="blocked ? 'success' : 'primary'" @click="$emit('block')">
            <slot name="action-two">
              {{ blocked ? 'Разблокировать' : 'Заблокировать' }}
            </slot>
          </n-button>
        </div>
      </slot>
    </div>
  </div>
</template>

<script lang="ts">
export default defineComponent({
  props: {
    fullName: {
      type: String,
      required: true,
    },
    role: {
      type: String,
      required: true,
    },
    blocked: {
      type: [Boolean],
      default: false,
    }
  },
});
</script>

<style scoped>

</style>
