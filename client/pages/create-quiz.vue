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
      <option value="mc">Multiple Choice</option>
      <option value="tf">True or False</option>
      <option value="n">Numerical</option>
      <option value="dd" disabled>DropDown</option>
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
const currentType = ref("");
const currentQuesCount = ref(0);
const forms = ref<Question[]>([]); //the actual question data with answers+incorrect
interface QuestionInstance {
  id: number;
  type: string;
}
const questions = ref<QuestionInstance[]>([]); //only questions' id and type, MERGE/SYNC "forms" AND "questions" LATER
function addBlankQuestion(id: number, type: string) {
  if (currentType.value === "") {
    alert("no question type chosen");
    return;
  }
  currentQuesCount.value++;
  questions.value.push({ id: id, type: type });
  forms.value.push({
    question: "",
    answer: "",
    incorrect: ["", "", ""],
    quiz: 1, // figure out quiz id later
  });
}
function removeQuestion(index: number) {
  //only removes from questions array, emit is used in CreateQuestion component to remove whole thing
  currentQuesCount.value--;
  questions.value.splice(index, 1);
}
function createQuiz() {
  console.log("All questions:", forms.value);
  //add quiz to api
  //add questions to api
}
</script>

<style scoped></style>
