<template>
  <div>
    <h1>{{ question.question }}</h1>
    <div>
      <form @sumbit.prevent="selectAnswer(userAnswer)">
        <input type="number" v-model="userAnswer" required />
        <button type="submit"></button>
      </form>
    </div>
  </div>
</template>

<script setup lang="ts">
const props = defineProps<{
  question: Question;
}>();

const userAnswer = ref(0);

const emit = defineEmits<{
  (e: "answerSelected", choice: number): void;
}>();

function selectAnswer(choice: number) {
  emit("answerSelected", choice);
}
</script>

<style scoped></style>
