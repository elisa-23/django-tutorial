<template>
  <div>
    <h2>{{ question.question }}</h2>
    <div>
      <ul class="space-y-3">
        <li v-for="(answer, index) in question.answer">
          <label for="">Blank {{ index + 1 }}: </label>
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
        Submit
      </button>
    </div>
    <p>selected: {{ selectedAnswers }}</p>
  </div>
</template>

<script setup lang="ts">
//example
/* const question = <Question>{
  question: "djfajfjl [BLANK-1] jdslajfasldjfslkd [BLANK-2] jdfsalfjslfjd",
  answer: ["a1", "a2"],
  incorrect: [
    ["i1", "i11"],
    ["i2", "i22"],
  ],
  quiz: 1,
};
 */

const props = defineProps<{
  question: Question;
}>();
const choices = ref<string[][]>([]);
const selectedAnswers = ref<string[]>(["", ""]);
onMounted(() => {
  choices.value = props.question.answer.map((correct, index) =>
    shuffle([correct, ...props.question.incorrect[index]])
  );
  selectedAnswers.value = props.question.answer.map(() => "");
});

const emit = defineEmits<{
  (e: "answerSelected", choice: string[]): void;
}>();

function selectAnswer(choice: string[]) {
  emit("answerSelected", choice);
}
</script>

<style scoped></style>
