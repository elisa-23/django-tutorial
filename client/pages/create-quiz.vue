<template>
  <div>
    <input type="text" placeholder="title" v-model="title" />
    <CreateQuestion
      v-for="(question, index) in questionData"
      :type="question.type"
      :count="index + 1"
      @remove="removeQuestion(index)"
      v-model="questionData[index]"
    />
    <select name="" id="" v-model="currentType">
      <option value="multipleChoice">Multiple Choice</option>
      <option value="trueOrFalse">True or False</option>
      <option value="numerical">Numerical</option>
      <option value="dropDown" disabled>DropDown</option>
    </select>
    <button @click="addBlankQuestion(currentType)">Add Question</button>
    <p>Number of Questions: {{ currentQuesCount }}</p>
    <button @click="createQuiz">Create Quiz</button>
  </div>
</template>

<script setup lang="ts">
const title = ref("");
const currentType = ref<QuestionType>("multipleChoice");
const currentQuesCount = ref(0);
const quizTypes = <number[]>[];
const questionData = ref<Question[]>([]); //the actual question data with answers+incorrect
const questionTypes = {
  multipleChoice: 1,
  trueOrFalse: 2,
  dropDown: 3,
  numerical: 4,
};
function addBlankQuestion(type: QuestionType) {
  /* if (currentType.value === "") {
    alert("no question type chosen");
    return;
  } */
  currentQuesCount.value++;
  quizTypes.push(questionTypes[type]);
  if (type === "dropDown") {
    questionData.value.push({
      question: "",
      answer: [""],
      incorrect: [[""]],
      type: "dropDown",
    });
  } else {
    questionData.value.push({
      question: "",
      answer: "",
      incorrect: ["", "", ""],
      type: type,
    });
  }
}
function removeQuestion(index: number) {
  //only removes from questions array, emit is used in CreateQuestion component to remove whole component
  currentQuesCount.value--;
  questionData.value.splice(index, 1);
}

const userStore = useUserStore();

async function createQuiz() {
  console.log("All questions:", questionData.value);
  console.log("user:", userStore.userInfo);
  //add quiz to api
  const createdQuiz = await fetchEndpoint<Quiz>("/quizzes/", "POST", {
    title: title.value,
    creator: userStore.userInfo.id,
    types: quizTypes,
  });
  if (!createdQuiz) {
    alert("Failed to create quiz. Please try again.");
    return;
  }
  console.log(createdQuiz);

  const currentQuizID = createdQuiz.id;
  //add questions to api
  questionData.value.forEach(async (question) => {
    const createdQuestion = await fetchEndpoint<Question>(
      "/questions/",
      "POST",
      { ...question, quiz: currentQuizID }
    );
    if (!createdQuestion) {
      alert("Failed to create question. Please try again.");
      return;
    }
    console.log(createdQuestion);
  });
}
</script>

<style scoped></style>
