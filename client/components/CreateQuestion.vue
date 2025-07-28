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
    <!-- <div v-if="type === 'dd'">        DO LATER
      <form action=""></form>
      <button @click="addDropdown">add dropdown</button>
      <div v-for="word in sentence">     sentence = ["word", "word", "", "word", ""]
        <p v-if="word.length > 0">{{word}}</p>
        <input v-if="word.length === 0" type="text">
      </div>
    </div> -->
    <div v-if="type === 'dd'">
      <form @submit.prevent="">
        <div v-for="(item, index) in ddArray" :key="'dd' + index">
          <input
            v-if="item.type === 'q'"
            v-model="item.value"
            type="text"
            placeholder="Question"
          />
          <div v-if="item.type === 'b'">
            <input
              v-model="item.correct"
              type="text"
              placeholder="Blank - correct answer"
            />
            <div class="mt-2 space-y-2">
              <input
                v-for="(wrong, i) in item.incorrect"
                :key="'wrong' + index + '-' + i"
                v-model="item.incorrect[i]"
                type="text"
                placeholder="Incorrect Answer"
              />
              <button
                v-if="item.incorrect.length < 4"
                @click.prevent="item.incorrect.push('')"
              >
                Add Incorrect Answer
              </button>
            </div>
          </div>
        </div>
        <button @click.prevent="addBlank()">Add a Blank</button>
      </form>
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

const ddArray = reactive<
  Array<{
    type: "q" | "b";
    value?: string;
    correct?: string;
    incorrect: string[];
  }>
>([{ type: "q", value: "", incorrect: [] }]);

function addBlank() {
  ddArray.push(
    { type: "b", correct: "", incorrect: [] },
    { type: "q", value: "", incorrect: [] }
  );
}
</script>

<style scoped></style>
