<template>
  <div>
    <h1>{{ sampleQuiz.title }}</h1>
    <h2>Made by: {{ sampleQuiz.creator }}</h2>
    <div class="flex flex-col space-y-4">
      <div
        v-if="
          currentQuestionIndex < sampleQuiz.questions.length &&
          currentQuestionDefined
        "
      >
        <MultipleChoice
          v-if="currentQuestion?.type === 'mc'"
          :question="currentQuestion!"
        />
        <TrueOrFalse
          v-if="currentQuestion?.type === 'tf'"
          :question="currentQuestion!"
        />
        <Numeral
          v-if="currentQuestion?.type === 'n'"
          :question="currentQuestion!"
        />
        <DropDown
          v-if="currentQuestion?.type === 'dd'"
          :question="currentQuestion!"
        />
      </div>
      <div v-else>
        <p>Quiz completed!</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const sampleQuiz = <Quiz>{
  id: 0,
  title: "Sample Quiz",
  creator: "elisa",
  questions: [
    {
      question: "What is the capital of France?",
      type: "mc",
      answer: "Paris",
      incorrect: ["London", "Berlin", "Madrid"],
      quizId: 0,
    },
    {
      question: "Is the sky blue?",
      type: "tf",
      answer: true,
      quizId: 0,
    },
    {
      question: "What is 2 + 2?",
      type: "n",
      answer: 4,
      quizId: 0,
    },
    {
      question:
        "Complete the pangram: The [Blank 1] brown fox [Blank 2] over the lazy dog",
      type: "dd",
      answer: ["quick", "jumps"],
      incorrect: [
        ["fast", "slow", "tired"],
        ["leaps", "hops", "runs"],
      ],
      quizId: 0,
    },
  ],
};

const currentQuestionIndex = ref(0);

const currentQuestion = computed(() => {
  return sampleQuiz.questions[currentQuestionIndex.value];
});

const currentQuestionDefined = computed(
  () => currentQuestion.value !== undefined
);

function nextQuestion() {
  if (currentQuestionIndex.value < sampleQuiz.questions.length - 1) {
    currentQuestionIndex.value++;
  }
}

function answerQuestion(choice: string | string[] | boolean | number) {}

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
