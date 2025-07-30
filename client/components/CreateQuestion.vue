<template>
  <div class="card bg-slate-400">
    <h2>{{ count }}</h2>
    <div v-if="type === 'multiple_choice'">
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

    <div v-if="type === 'true/false'">
      <input type="text" placeholder="Question" v-model="modelValue.question" />
      <input
        type="radio"
        id="True"
        name="true/false"
        value="True"
        v-model="modelValue.answer"
      />
      <label for="True">True</label><br />
      <input
        type="radio"
        id="False"
        name="true/false"
        value="False"
        v-model="modelValue.answer"
      />
      <label for="False">False</label><br /><br />
    </div>

    <div v-if="type === 'numerical'">
      <input type="text" placeholder="Question" v-model="modelValue.question" />
      <input
        type="number"
        placeholder="Correct Answer"
        v-model="modelValue.answer"
      />
    </div>

    <!-- <div v-if="type === 'dropdown'">
      <input
        type="text"
        placeholder="Dropdown Title"
        v-model="modelValue.question"
        class="mb-4"
      />

      <div
        v-for="(part, index) in modelValue.parts"
        :key="'part-' + index"
        class="mb-4"
      >
        <div v-if="part.type === 'questionPart'">
          <input
            type="text"
            placeholder="Question text"
            v-model="part.text"
            class="w-full"
          />
        </div>

        <div v-else-if="part.type === 'blank'">
          <input
            type="text"
            placeholder="Correct Answer"
            v-model="part.answer"
          />
          <div class="mt-2 space-y-2">
            <input
              v-for="(wrong, i) in part.incorrect"
              :key="'wrong-' + index + '-' + i"
              type="text"
              placeholder="Incorrect Answer"
              v-model="part.incorrect[i]"
            />
            <button
              v-if="part.incorrect.length < 4"
              @click.prevent="addIncorrectOption(index)"
            >
              Add Incorrect Answer
            </button>
          </div>
        </div>
      </div>

      <div class="mt-4 space-x-2">
        <button @click.prevent="addQuestionPart">Add Question Text</button>
        <button @click.prevent="addBlankPart">Add Blank</button>
      </div>
    </div> -->

    <button class="" @click="removeQuestion">Remove</button>
  </div>
</template>

<script setup lang="ts">
const props = defineProps<{
  type: string;
  count: number;
}>();

//const modelValue = defineModel<Question>({ required: true });
const modelValue = defineModel<CreateQuestion>({ required: true });

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

/* function addQuestionPart() {
  if (modelValue.value.parts) {
    modelValue.value.parts.push({
      type: "questionPart",
      text: "",
    });
  }
}

function addBlankPart() {
  if (modelValue.value.parts) {
    modelValue.value.parts.push({
      type: "blank",
      answer: "",
      incorrect: [""],
    });
  }
}

function addIncorrectOption(index: number) {
  if (modelValue.value.parts) {
    const part = modelValue.value.parts[index];
    if (part) {
      if (part.type === "blank" && part.incorrect.length < 4) {
        part.incorrect.push("");
      }
    }
  }
} */
</script>

<style scoped></style>
