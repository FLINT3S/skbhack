<template>
  <div></div>
</template>

<script setup lang="ts">
import { useRouter } from "vue-router";

console.log("Logout");

const router = useRouter();

router.replace("/auth/login");
</script>

<style scoped></style>
