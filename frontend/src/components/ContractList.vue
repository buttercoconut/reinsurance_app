<template>
  <div>
    <h1>Reinsurance Contracts</h1>
    <ul>
      <li v-for="contract in contracts" :key="contract.id">
        {{ contract.reinsurer_name }} - {{ contract.primary_insurer_name }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue"
import axios from "axios"

const contracts = ref([])

onMounted(async () => {
  try {
    const response = await axios.get("http://localhost:8000/contracts/")
    contracts.value = response.data
  } catch (error) {
    console.error("Error fetching contracts", error)
  }
})
</script>

<style scoped>
ul {
  list-style-type: none;
  padding: 0;
}
li {
  margin: 0.5rem 0;
}
</style>
