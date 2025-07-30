<template>
  <div>
    <h1>{{ question.question }}</h1>
    <div>
      <ul class="space-y-3">
        <li
          v-for="(choice, index) in shuffle([
            question.answer,
            ...question.incorrect,
          ])"
          :key="index"
          class="px-4 py-2 hover:bg-blue-100 rounded cursor-pointer transition"
          @click="selectAnswer(choice)"
        >
          {{ choice }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup lang="ts">
const props = defineProps<{
  question: MultipleChoiceQuestion;
}>();

const emit = defineEmits<{
  answerSelected: [choice: string];
  //(e: "answerSelected", choice: string  | string[]): void;
}>();

function selectAnswer(choice: string) {
  emit("answerSelected", choice);
}
</script>

<style scoped></style>
