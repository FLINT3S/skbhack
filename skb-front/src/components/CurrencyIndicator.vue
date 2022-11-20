<template>
  <div class="currency-indicator d-flex align-items-center" :class="(computedGrowth ? 'grow-up' : 'grow-down') + ' ' + (changed ? 'change-pulse' : '')">
    <div class="currency-indicator__title me-1">
      <span>{{ title }}</span>
    </div>
    <div class="currency-indicator__value d-flex align-items-center" :class="computedGrowth ? 'up' : 'down'">
      <span>{{ currencySymbol }}{{ value.toFixed(2) }}</span>
      <span class="material-icons-round">
        {{ computedGrowth ? 'arrow_drop_up' : 'arrow_drop_down' }}
      </span>
    </div>
  </div>
</template>

<script lang="ts">
import {defineComponent} from "vue";

export default defineComponent({
  data() {
    return {
      oldValue: 0,
      changed: false
    };
  },
  props: {
    title: {
      type: String,
      required: true
    },
    value: {
      type: Number,
      required: true
    },
    growth: {
      type: [Boolean, String],
      default: "auto"
    },
    currencySymbol: {
      type: String,
      required: true
    }
  },
  watch: {
    value: {
      handler: function (newValue, oldValue) {
        this.changed = true
        setTimeout(() => {
          this.changed = false
        }, 800)
      },
      immediate: true
    }
  },
  computed: {
    computedGrowth() {
      if (this.growth === "auto") {
        let res;

        if (this.oldValue === 0) {
          res = Math.random() > 0.5;
        }

        res = this.value > this.oldValue;
        this.oldValue = this.value;

        return res;
      } else {
        return this.growth;
      }
    }
  }
});
</script>

<style scoped lang="scss">
.currency-indicator {
  font-size: 18px;
  font-weight: 500;
}

.currency-indicator__value {
  font-weight: 600;
  &.up {
    color: #279E57
  }

  &.down {
    color: #B63434
  }
}

.change-pulse {
  &.grow-up {
    animation: pulse-green .8s ease-in-out 1;
  }

  &.grow-down {
    animation: pulse-red .8s ease-in-out 1;
  }
}

@keyframes pulse-green {
  0%, 100% {
    text-shadow: 0 0 0px rgba(39, 158, 87, 0);
  }

  50% {
    text-shadow: 0 0 10px rgba(39, 158, 87, .6);
  }
}

@keyframes pulse-red {
  0%, 100% {
    text-shadow: 0 0 0px rgba(182, 52, 52, 0);
  }

  50% {
    text-shadow: 0 0 10px rgba(182, 52, 52, .6);
  }
}
</style>
