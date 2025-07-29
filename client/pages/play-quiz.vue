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
          @answerSelected="handleAnswer"
        />
        <TrueOrFalse
          v-if="currentQuestion?.type === 'tf'"
          :question="currentQuestion!"
          @answerSelected="handleAnswer"
        />
        <Numeral
          v-if="currentQuestion?.type === 'n'"
          :question="currentQuestion!"
          @answerSelected="handleAnswer"
        />
        <DropDown
          v-if="currentQuestion?.type === 'dd'"
          :question="currentQuestion!"
          @answerSelected="handleAnswer"
        />
      </div>
      <!-- <div v-else>
        <p>Quiz completed!</p>
      </div> -->
    </div>
  </div>
</template>

<script setup lang="ts">
const sampleQuiz: Quiz = {
  id: 0,
  title: "Sample Quiz",
  creator: "Someone",
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
      incorrect: [],
      quizId: 0,
    },
    {
      question: "What is 2 + 2?",
      type: "n",
      answer: 4,
      incorrect: [],
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

function handleAnswer(choice: string | string[] | boolean | number) {
  if (!currentQuestion.value) return;

  const question = currentQuestion.value;

  if (question.type === "dd") {
    if (Array.isArray(question.answer) && Array.isArray(choice)) {
      const correct = choice.every(
        (c, index) =>
          Array.isArray(question.answer) && c === question.answer[index]
      );
      if (correct) {
        console.log("Correct!");
      } else {
        console.log("Incorrect!");
      }
    } else {
      console.log("Invalid choice for dropdown question.");
    }
    nextQuestion();
    return;
  }

  if (choice === question.answer) {
    console.log("Correct!");
  } else {
    console.log("Incorrect!");
  }
  nextQuestion();
}
</script>

<style scoped></style>
