<template>
  <div>
    <div>
      <h2>{{ question.question }}</h2>
      <div>
        <form @submit.prevent="selectAnswer(userAnswer)">
          <input type="number" v-model="userAnswer" required />
          <button type="submit"></button>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const props = defineProps<{
  question: Question;
}>();

const userAnswer = ref<number>(0);

const emit = defineEmits<{
  (e: "answerSelected", choice: number): void;
}>();

function selectAnswer(choice: number) {
  emit("answerSelected", choice);
}

//change answer to string after submission
</script>

<style scoped></style>
