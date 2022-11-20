<template>
  <div></div>
</template>

<script setup lang="ts">
import { useRouter } from "vue-router";
import {Credentials} from "../../data/Credentials";

console.log("Logout");

const router = useRouter();

Credentials.onLogout()
location.reload()
</script>

<style scoped></style>
