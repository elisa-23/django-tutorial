<div v-if="type === 'dd'">
  <!-- Dropdown question text -->
  <input
    type="text"
    placeholder="Dropdown Question"
    v-model="modelValue.question"
  />

  <!-- For each blank -->
  <div
    v-for="(blankAnswer, index) in modelValue.answer"
    :key="'blank' + index"
    class="mt-4"
  >
    <!-- Correct answer for this blank -->
    <input
      type="text"
      placeholder="Blank - correct answer"
      v-model="modelValue.answer[index]"
    />

    <!-- Incorrect options for this blank -->
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

</div>

function addDropdownBlank() {
if (Array.isArray(modelValue.value.answer)) {
modelValue.value.answer.push(""); // add a new correct answer
} else {
modelValue.value.answer = [""];
}

if (Array.isArray(modelValue.value.incorrect)) {
modelValue.value.incorrect.push([""]); // initialize with one wrong option
} else {
modelValue.value.incorrect = [[""]];
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
