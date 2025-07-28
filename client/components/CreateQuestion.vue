<template>
  <div class="card bg-slate-400">
    <h2>{{ count }}</h2>
    <div v-if="type === 'mc'">
      <input type="text" placeholder="Question" v-model="modelValue.question" />
      <input
        type="text"
        placeholder="Correct Answer"
        v-model="modelValue.answer"
      />
      <!-- make correct ans more visible ig -->
      <input
        v-for="(value, index) in modelValue.incorrect"
        type="text"
        placeholder="Wrong Answer"
        :key="index"
        v-model="modelValue.incorrect[index]"
      />
    </div>

    <div v-if="type === 'tf'">
      <input type="text" placeholder="Question" v-model="modelValue.question" />
      <input
        type="radio"
        id="True"
        name="tf"
        value="True"
        v-model="modelValue.answer"
      />
      <label for="True">True</label><br />
      <input
        type="radio"
        id="False"
        name="tf"
        value="False"
        v-model="modelValue.answer"
      />
      <label for="False">False</label><br /><br />
    </div>

    <div v-if="type === 'n'">
      <input type="text" placeholder="Question" v-model="modelValue.question" />
      <input
        type="number"
        placeholder="Correct Answer"
        v-model="modelValue.answer"
      />
    </div>

    <div v-if="type === 'dd'">
      <div
        v-for="(blankQuestion, index) in modelValue.question"
        :key="'questionpart' + index"
        class="mt-4"
      >
        <input
          type="text"
          placeholder="Question part"
          v-model="modelValue.question[index]"
        />
      </div>
      <div
        v-for="(blankAnswer, index) in modelValue.answer"
        :key="'blank' + index"
        class="mt-4"
      >
        <input
          type="text"
          placeholder="Blank - correct answer"
          v-model="modelValue.answer[index]"
        />
        <div class="mt-2 space-y-2">
          <input
            v-for="(wrong, i) in modelValue.incorrect[index]"
            :key="'wrong' + index + '-' + i"
            type="text"
            placeholder="Incorrect Answer"
            v-model="modelValue.incorrect[index][i]"
          />

          <button
            v-if="modelValue.incorrect[index].length < 4"
            @click.prevent="addDropdownIncorrect(index)"
          >
            Add Incorrect Answer
          </button>
        </div>
      </div>

      <button @click.prevent="addDropdownBlank">Add a Blank</button>
      <button @click.prevent="addDropdownQuestionPart">
        Add a Question Part
      </button>
    </div>

    <button class="" @click="removeQuestion">Remove</button>
  </div>
</template>

<script setup lang="ts">
const props = defineProps<{
  type: string;
  count: number;
}>();

const modelValue = defineModel<Question>({ required: true });

const emit = defineEmits<{
  (e: "remove"): void;
}>();

function removeQuestion() {
  emit("remove");
}

/* const ddArray = reactive<
  Array<{
    type: "q" | "b";
    value?: string;
    correct?: string;
  }>
>([{ type: "q", value: "" }]); */

function addDropdownBlank() {
  //ddArray.push({ type: "b" }, { type: "q", value: "" });

  if (
    Array.isArray(modelValue.value.answer) &&
    Array.isArray(modelValue.value.question)
  ) {
    modelValue.value.answer.push("");
    modelValue.value.question.push("");
  } else {
    modelValue.value.answer = [""];
    modelValue.value.question = [""];
  }
  if (Array.isArray(modelValue.value.incorrect)) {
    modelValue.value.incorrect.push([""]);
  } else {
    modelValue.value.incorrect = [[""]];
  }
}

function addDropdownQuestionPart() {
  if (Array.isArray(modelValue.value.question)) {
    modelValue.value.question.push("");
  } else {
    modelValue.value.question = [""];
  }
}

function addDropdownIncorrect(index: number) {
  if (
    Array.isArray(modelValue.value.incorrect[index]) &&
    modelValue.value.incorrect[index].length < 4
  ) {
    modelValue.value.incorrect[index].push("");
  }
}
</script>

<style scoped></style>
