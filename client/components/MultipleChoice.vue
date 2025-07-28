<template>
  <div>
    <h2>{{ question.question }}</h2>
    <div>
      <ul class="space-y-3">
        <li
          v-for="(choice, index) in shuffle([
            ...question.answer,
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
  question: Question;
}>();
const emit = defineEmits<{
  (e: "answerSelected", choice: string | string[]): void;
}>();

function selectAnswer(choice: string | string[]) {
  emit("answerSelected", choice);
}
</script>

<style scoped></style>
