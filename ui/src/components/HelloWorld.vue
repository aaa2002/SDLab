<template>
  <v-container>
    <ul>
      <li v-for="user in users" :key="user.id">
        user.name
      </li>
    </ul>
  </v-container>
</template>

<script setup>

import { ref } from 'vue'

const users = ref([])

fetch('http://localhost:8000/users')
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    // Do something with the fetched user data
    console.log(data);
  })
  .catch(error => {
    // Handle any errors that occur during the fetch
    console.error('Fetch error:', error);
  });

</script>
