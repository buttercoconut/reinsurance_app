<template>
  <div id="app">
    <h1>Reinsurance App</h1>
    <ContractList />
  </div>
</template>

<script setup>
import ContractList from "./components/ContractList.vue"
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
