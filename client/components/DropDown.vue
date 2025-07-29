<template>
  <div>
    <h1>{{ question.question }}</h1>
    <div>
      <ul class="space-y-3">
        <li v-for="(answer, index) in question.answer">
          <label for="">Blank {{ index + 1 }}</label>
          <select name="" id="" v-model="selectedAnswers[index]">
            <option value="" disabled>Please select an answer</option>
            <option
              v-for="choice in choices[index]"
              :value="choice"
              :key="index"
            >
              {{ choice }}
            </option>
          </select>
        </li>
      </ul>
      <button type="submit" @click="selectAnswer(selectedAnswers)">
        Submit Answers
      </button>
    </div>
    <p>selected: {{ selectedAnswers }}</p>
  </div>
</template>

<script setup lang="ts">
const props = defineProps<{
  question: Question;
}>();

const choices = ref<string[][]>([]);

const selectedAnswers = ref<string[]>(["", ""]);

onMounted(() => {
  choices.value = (props.question.answer as string[]).map((correct, index) =>
    shuffle([correct, ...(props.question.incorrect[index] || [])])
  );
  selectedAnswers.value = (props.question.answer as string[]).map(() => "");
});

const emit = defineEmits<{
  answerSelected: [choice: string[]];
  //(e: "answerSelected", choice: string[]): void;
}>();

function selectAnswer(choice: string[]) {
  emit("answerSelected", choice);
}
</script>

<style scoped></style>
