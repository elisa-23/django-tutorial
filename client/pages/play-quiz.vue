<template>
  <div>
    <h1>Play Quiz</h1>
  </div>
</template>

<script setup lang="ts">
const props = defineProps<{
  questionType: "mc" | "tf" | "n" | "dd";
}>();

/* async function fetchQuiz(quizId: number) {
  const response = await fetch(`/quizzes/${quizId}`);
  if (!response.ok) {
    throw new Error("Failed to fetch quiz");
  }
  const data = response.json();
  return data;
}

onMounted(async () => {
  await fetchQuiz(0);
}); */
</script>

<style scoped></style>
