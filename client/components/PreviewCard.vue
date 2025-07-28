<template>
  <div class="preview-card">
    <h3>Preview</h3>

    <div v-if="type === 'mc'">
      <p><strong>Question:</strong> {{ question }}</p>
      <ul>
        <li><strong>Correct Answer:</strong> {{ correctAnswer }}</li>
        <li v-for="(ans, index) in wrongAnswers" :key="index">
          Incorrect: {{ ans }}
        </li>
      </ul>
    </div>

    <div v-if="type === 'tf' || type === 'n'">
      <p><strong>Question:</strong> {{ question }}</p>
      <p><strong>Correct Answer:</strong> {{ correctAnswer }}</p>
    </div>

    <div v-if="type === 'dd'">
      <p><strong>Fill-in-the-blank Question:</strong></p>
      <div v-for="(item, index) in ddArray" :key="index">
        <template v-if="item.type === 'q'">
          <p>{{ item.value }}</p>
        </template>
        <template v-else>
          <p>
            <strong>Blank {{ getBlankNumber(index) }}:</strong>
            {{ item.correct }}
          </p>
          <ul>
            <li v-for="(wrong, i) in item.incorrect" :key="i">
              Incorrect: {{ wrong }}
            </li>
          </ul>
        </template>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const props = defineProps<{
  type: string;
  question?: string;
  correctAnswer?: string;
  wrongAnswers?: string[];
  ddArray?: Array<{
    type: "q" | "b";
    value?: string;
    correct?: string;
    incorrect: string[];
  }>;
}>();

function getBlankNumber(currentIndex: number): number {
  if (!props.ddArray) return 0;
  return props.ddArray
    .slice(0, currentIndex + 1)
    .filter((item) => item.type === "b").length;
}
</script>
