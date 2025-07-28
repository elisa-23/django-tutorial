<template>
  <div>
    <DropDown :question="question" />
  </div>
</template>

<script setup lang="ts">
const question = <Question>{
  question: "dhsagfhkh [Blank 1] uhsaifhiu [Blank 2] ahfkhklkg",
  answer: ["a1", "a2"],
  incorrect: [
    ["l1", "l2", "l3"],
    ["l4", "l5", "l6"],
  ],
  quizId: 1,
};

async function handleLogin() {
  const token = await requestEndpoint<{
    access: string;
    refresh: string;
  }>("/api/token/", "POST", {
    email: "hu@gmail.com",
    password: "huhu",
  });
  console.log(token);
}

onMounted(async () => {
  await handleLogin();
});
</script>

<style scoped></style>
