<template>
  <div>
    <h2>Reinsurance Contracts</h2>
    <table class="table">
      <thead>
        <tr>
          <th>ID</th>
          <th>Insurer</th>
          <th>Premium</th>
          <th>Coverage Limit</th>
          <th>Status</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="contract in contracts" :key="contract.id">
          <td>{{ contract.id }}</td>
          <td>{{ contract.insurer_name }}</td>
          <td>{{ contract.premium | currency }}</td>
          <td>{{ contract.coverage_limit | currency }}</td>
          <td>{{ contract.status }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const contracts = ref([]);

const fetchContracts = async () => {
  try {
    const response = await axios.get('/api/contracts');
    contracts.value = response.data;
  } catch (err) {
    console.error('Failed to fetch contracts', err);
  }
};

onMounted(() => {
  fetchContracts();
});
</script>

<style scoped>
.table {
  width: 100%;
  border-collapse: collapse;
}
.table th,
.table td {
  border: 1px solid #ddd;
  padding: 8px;
}
.table th {
  background-color: #f2f2f2;
}
</style>
