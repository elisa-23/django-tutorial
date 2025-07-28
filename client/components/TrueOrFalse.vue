<template>
  <div>
    <h1>{{ question.question }}</h1>
    <div class="flex items-center space-x-4">
      <button
        class="px-4 py-2 hover:bg-blue-100 rounded cursor-pointer transition"
        @click="selectAnswer(true)"
      >
        True
      </button>
      <button
        class="px-4 py-2 hover:bg-blue-100 rounded cursor-pointer transition"
        @click="selectAnswer(false)"
      >
        False
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
const props = defineProps<{
  question: Question;
}>();

const emit = defineEmits<{
  (e: "answerSelected", choice: boolean): void;
}>();

function selectAnswer(choice: boolean) {
  emit("answerSelected", choice);
}
</script>

<style scoped></style>
