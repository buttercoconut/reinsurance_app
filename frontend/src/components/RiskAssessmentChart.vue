<template>
  <div>
    <h2>Risk Assessment Chart</h2>
    <canvas id="riskChart" width="400" height="200"></canvas>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { Chart, registerables } from 'chart.js';
Chart.register(...registerables);

const createChart = () => {
  const ctx = document.getElementById('riskChart').getContext('2d');
  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['Risk A', 'Risk B', 'Risk C'],
      datasets: [{
        label: 'Exposure',
        data: [120, 80, 150],
        backgroundColor: ['#ff6384', '#36a2eb', '#ffce56']
      }]
    },
    options: { responsive: true }
  });
};

onMounted(createChart);
</script>

<style scoped>
canvas {
  max-width: 100%;
}
</style>
