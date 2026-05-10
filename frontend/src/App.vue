<template>
  <div id="app">
    <h1>Reinsurance Management Dashboard</h1>
    <nav>
      <router-link to="/contracts">Contracts</router-link>
      <router-link to="/risk">Risk Assessment</router-link>
      <router-link to="/claims">Claims</router-link>
    </nav>
    <router-view />
  </div>
</template>

<script setup>
import { createRouter, createWebHistory } from 'vue-router';
import ContractList from './components/ContractList.vue';
import RiskAssessmentChart from './components/RiskAssessmentChart.vue';
import ClaimForm from './components/ClaimForm.vue';

const routes = [
  { path: '/contracts', component: ContractList },
  { path: '/risk', component: RiskAssessmentChart },
  { path: '/claims', component: ClaimForm },
  { path: '/', redirect: '/contracts' },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.isReady().then(() => {
  // router ready
});

export default router;
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  margin: 2rem;
}
nav {
  margin-bottom: 1rem;
}
nav a {
  margin-right: 1rem;
  text-decoration: none;
  color: #42b983;
}
nav a.router-link-exact-active {
  font-weight: bold;
}
</style>
