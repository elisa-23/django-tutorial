<template>
  <div>
    <h1>{{ quizzes[0]?.title }}</h1>
    <div class="flex flex-col space-y-4">
      <div
        v-if="
          currentQuestionIndex < quizQuestions.length && currentQuestionDefined
        "
      >
        <MultipleChoice
          v-if="currentQuestion?.question_type === 1"
          :question="currentQuestion!"
          @answerSelected="handleAnswer"
        />
        <TrueOrFalse
          v-if="currentQuestion?.question_type === 2"
          :question="currentQuestion!"
          @answerSelected="handleAnswer"
        />
        <DropDown
          v-if="currentQuestion?.question_type === 3"
          :question="currentQuestion!"
          @answerSelected="handleAnswer"
        />
        <Numeral
          v-if="currentQuestion?.question_type === 4"
          :question="currentQuestion!"
          @answerSelected="handleAnswer"
        />
      </div>
      <div v-else>
        <p>Quiz completed!</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
async function getQuiz() {
  const quizzes = await fetchEndpoint<Quiz[]>("/quizzes/", "GET", undefined, {
    id: 1,
  });

  const questions = await fetchEndpoint<Question[]>(
    `/questions/`,
    "GET",
    undefined,
    {
      quizId: 1,
    }
  );
  return [quizzes, questions] as [Quiz[], Question[]];
}

const quizzes = ref<Quiz[]>([]);
const quizQuestions = ref<Question[]>([]);

onMounted(async () => {
  const quizData = await getQuiz();
  quizzes.value = quizData[0];
  quizQuestions.value = quizData[1];
});

const currentQuestionIndex = ref(0);

const currentQuestion = computed(() => {
  return quizQuestions.value[currentQuestionIndex.value];
});

const currentQuestionDefined = computed(
  () => currentQuestion.value !== undefined
);

function nextQuestion() {
  if (currentQuestionIndex.value < quizQuestions.value.length - 1) {
    currentQuestionIndex.value++;
  }
}

function handleAnswer(choice: string | string[] | boolean | number) {
  if (!currentQuestion.value) return;

  const question = currentQuestion.value;

  if (question.question_type === 3) {
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
