<template>
  <div></div>
</template>

<script setup lang="ts">
async function handleLogin() {
  const token = await requestEndpoint<{
    access: string;
    refresh: string;
  }>("/api/token/", "POST", {
    email: "elisahu@gmail.com",
    password: "huhuhu",
  });
  console.log(token);
}

onMounted(async () => {
  await handleLogin();
});
</script>

<style scoped></style>
