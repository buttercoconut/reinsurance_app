<template>
  <div>
    <h2>Claim Submission</h2>
    <form @submit.prevent="submitClaim">
      <div class="form-group">
        <label for="policyId">Policy ID</label>
        <input v-model="form.policyId" id="policyId" type="text" required />
      </div>
      <div class="form-group">
        <label for="claimAmount">Claim Amount</label>
        <input v-model.number="form.claimAmount" id="claimAmount" type="number" required />
      </div>
      <div class="form-group">
        <label for="description">Description</label>
        <textarea v-model="form.description" id="description" required></textarea>
      </div>
      <button type="submit">Submit Claim</button>
    </form>
    <p v-if="message" :class="{ success: success, error: !success }">{{ message }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';

const form = ref({
  policyId: '',
  claimAmount: 0,
  description: '',
});
const message = ref('');
const success = ref(false);

const submitClaim = async () => {
  try {
    const response = await axios.post('/api/claims', form.value);
    message.value = 'Claim submitted successfully! ID: ' + response.data.id;
    success.value = true;
    form.value = { policyId: '', claimAmount: 0, description: '' };
  } catch (err) {
    message.value = 'Error submitting claim: ' + err.message;
    success.value = false;
  }
};
</script>

<style scoped>
.form-group {
  margin-bottom: 1rem;
}
label {
  display: block;
  margin-bottom: 0.5rem;
}
input,
textarea {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 4px;
}
button {
  padding: 0.5rem 1rem;
  background-color: #28a745;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
button:hover {
  background-color: #218838;
}
.success {
  color: green;
}
.error {
  color: red;
}
</style>
