<template>
  <div>
    <h2>Submit a Claim</h2>
    <form @submit.prevent="submitClaim">
      <div>
        <label for="contractId">Contract ID:</label>
        <input id="contractId" v-model="form.contractId" required />
      </div>
      <div>
        <label for="amount">Amount:</label>
        <input id="amount" type="number" v-model="form.amount" required />
      </div>
      <div>
        <label for="description">Description:</label>
        <textarea id="description" v-model="form.description" required></textarea>
      </div>
      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';

const form = ref({
  contractId: '',
  amount: 0,
  description: ''
});

const submitClaim = async () => {
  try {
    await axios.post('/api/claims', form.value);
    alert('Claim submitted successfully');
    form.value = { contractId: '', amount: 0, description: '' };
  } catch (err) {
    console.error('Error submitting claim', err);
    alert('Failed to submit claim');
  }
};
</script>

<style scoped>
form {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}
label {
  font-weight: bold;
}
input, textarea {
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 4px;
}
button {
  width: fit-content;
  padding: 0.5rem 1rem;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
button:hover {
  background-color: #369870;
}
</style>
