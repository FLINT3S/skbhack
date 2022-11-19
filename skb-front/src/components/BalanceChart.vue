<template>
  <Doughnut style="max-height: 300px" :chart-data="chartData" :chart-options="chartOptions"/>
</template>

<script lang="ts">
// @ts-nocheck
import {Doughnut} from 'vue-chartjs'
import {ArcElement, BarElement, CategoryScale, Chart as ChartJS, Legend, LinearScale, Title, Tooltip} from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale, ArcElement)


export default {
  components: {Doughnut},
  data() {
    return {
      chartOptions: {
        // responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            display: true,
            position: "right",
            labels: {
              usePointStyle: true,
              boxWidth: 6
            }
          },
          title: {
            display: false,
          }
        }
      }
    }
  },
  props: {
    chartData: {
      type: Object,
      required: true
    }
  }
}
</script>

<style scoped>

</style>
