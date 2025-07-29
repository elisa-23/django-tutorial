<template>
  <div>
    <input type="text" placeholder="title" v-model="title" />
    <CreateQuestion
      v-for="(question, index) in questions"
      :type="question.type"
      :count="index + 1"
      @remove="removeQuestion(index)"
      v-model="forms[index]"
    />
    <select name="" id="" v-model="currentType">
      <option value="multipleChoice">Multiple Choice</option>
      <option value="trueOrFalse">True or False</option>
      <option value="numerical">Numerical</option>
      <option value="dropDown" disabled>DropDown</option>
    </select>
    <button @click="addBlankQuestion(currentQuesCount, currentType)">
      Add Question
    </button>
    <p>Number of Questions: {{ currentQuesCount }}</p>
    <button @click="createQuiz">Create Quiz</button>
  </div>
</template>

<script setup lang="ts">
const title = ref("");
const currentType = ref("multipleChoice");
const currentQuesCount = ref(0);
const quizTypes = <number[]>[];
const forms = ref<Question[]>([]); //the actual question data with answers+incorrect
interface QuestionInstance {
  id: number;
  type: string;
}
const questionTypes = {
  multipleChoice: 1,
  trueOrFalse: 2,
  dropDown: 3,
  numerical: 4,
};
const questions = ref<QuestionInstance[]>([]); //only questions' id and type, MERGE/SYNC "forms" AND "questions" LATER
function addBlankQuestion(
  id: number,
  type: "multipleChoice" | "trueOrFalse" | "dropDown" | "numerical"
) {
  if (currentType.value === "") {
    alert("no question type chosen");
    return;
  }
  currentQuesCount.value++;
  questions.value.push({ id: id, type: type });
  quizTypes.push(questionTypes[type]);
  if (type === "dropDown") {
    forms.value.push({
      question: "",
      answer: [""],
      incorrect: [[""]],
      type: "dd",
      quiz: 1, // figure out quiz id later
    });
  } else {
    forms.value.push({
      question: "",
      answer: "",
      incorrect: ["", "", ""],
      type: type,
      quiz: 1, // figure out quiz id later
    });
  }
}
function removeQuestion(index: number) {
  //only removes from questions array, emit is used in CreateQuestion component to remove whole thing
  currentQuesCount.value--;
  questions.value.splice(index, 1);
}

const userStore = useUserStore();

async function createQuiz() {
  console.log("All questions:", forms.value);
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

  //add questions to api
  forms.value.forEach(async (question) => {
    const createdQuestion = await fetchEndpoint<Question>(
      "/questions/",
      "POST",
      question
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
