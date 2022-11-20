<template>
  <div></div>
</template>

<script setup lang="ts">
import { useRouter } from "vue-router";
import {Credentials} from "../../data/Credentials";

console.log("Logout");

const router = useRouter();

Credentials.onLogout()
router.replace("/auth/login");
</script>

<style scoped></style>
