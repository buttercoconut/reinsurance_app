<template>
  <div>
    <h2>Risk Assessment</h2>
    <canvas id="riskChart" ref="chartCanvas"></canvas>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import Chart from 'chart.js/auto';

const chartCanvas = ref(null);
const chartInstance = ref(null);

const fetchRiskData = async () => {
  try {
    const response = await fetch('/api/risk');
    const data = await response.json();
    return data;
  } catch (err) {
    console.error('Error fetching risk data', err);
    return [];
  }
};

const renderChart = (data) => {
  if (chartInstance.value) chartInstance.value.destroy();
  chartInstance.value = new Chart(chartCanvas.value, {
    type: 'bar',
    data: {
      labels: data.map(d => d.name),
      datasets: [{
        label: 'Risk Score',
        data: data.map(d => d.score),
        backgroundColor: 'rgba(54, 162, 235, 0.6)',
      }],
    },
    options: { responsive: true },
  });
};

onMounted(async () => {
  const data = await fetchRiskData();
  renderChart(data);
});
</script>

<style scoped>
canvas {
  max-width: 100%;
}
</style>
