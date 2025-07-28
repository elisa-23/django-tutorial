<template>
  <div>
    <h2>{{ question.question }}</h2>
    <div class="space-y-3">
      <button
        class="px-4 py-2 hover:bg-blue-100 rounded cursor-pointer transition"
        @click="selectAnswer('True')"
      >
        True
      </button>
      <button
        class="px-4 py-2 hover:bg-blue-100 rounded cursor-pointer transition"
        @click="selectAnswer('False')"
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
  (e: "answerSelected", choice: string): void;
}>();

function selectAnswer(choice: string) {
  emit("answerSelected", choice);
}
</script>

<style scoped></style>
