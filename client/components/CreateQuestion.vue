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
</script>

<style scoped></style>
