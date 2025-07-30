<template>
  <div>
    <input type="text" placeholder="title" v-model="title" />
    <CreateQuestion
      v-for="(question, index) in questionData"
      :type="question.type"
      :count="index + 1"
      @remove="removeQuestion(index)"
      v-model="questionData[index]!"
    />
    <select name="" id="" v-model="currentType">
      <option value="multiple_choice">Multiple Choice</option>
      <option value="true/false">True or False</option>
      <option value="numerical">Numerical</option>
      <option value="dropdown" disabled>DropDown</option>
    </select>
    <button @click="addBlankQuestion(currentType)">Add Question</button>
    <p>Number of Questions: {{ currentQuesCount }}</p>
    <button @click="createQuiz">Create Quiz</button>
  </div>
</template>

<script setup lang="ts">
const title = ref("");
const currentType = ref<QuestionType>("multiple_choice");
const currentQuesCount = ref(0);
const quizTypes = <QuestionType[]>[];
const questionData = ref<CreateQuestion[]>([]);
function addBlankQuestion(type: QuestionType) {
  /* if (currentType.value === "") {
    alert("no question type chosen");
    return;
  } */
  currentQuesCount.value++;
  quizTypes.push(type);
  let emptyQuestion: CreateQuestion; // says its being used before declared if not declared here
  if (type === "dropdown") {
    emptyQuestion = {
      question: "",
      answer: [""],
      incorrect: [[""]],
      type: "dropdown",
    };
  } else if (type === "multiple_choice") {
    emptyQuestion = {
      question: "",
      answer: "",
      incorrect: ["", "", ""],
      type: "multiple_choice",
    };
  } else if (type === "true/false") {
    emptyQuestion = {
      question: "",
      answer: true, //how to use default boolean here
      type: "true/false",
    };
  } else if (type === "numerical") {
    emptyQuestion = {
      question: "",
      answer: 0, // use default num
      type: "numerical",
    };
  }
  questionData.value.push(emptyQuestion!); // says cannot find name emptyQuestion if declared inside if/else
}
function removeQuestion(index: number) {
  //only removes from questions array & quizTypes, emit is used in CreateQuestion component to remove whole component
  currentQuesCount.value--;
  questionData.value.splice(index, 1);
  quizTypes.splice(index, 1);
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
    const createdQuestion = await fetchEndpoint<CreateQuestion>(
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
