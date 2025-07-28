<!-- <template>
    <div>
        <div v-if="type === 'mc'">
            <form action="">
                <input type="text" placeholder="Question"/>
                <input type="text" placeholder="Correct Answer"/>
                <input v-for="n in 3" type="text" placeholder="Wrong Answer" :key="n"/>
            </form>
        </div>
        <div v-if="type === 'tf'">
            <form>
                <input type="text" placeholder="Question"/>
                <input type="radio" id="True" name="tf" value="True"/>
                <label for="True">True</label><br/>
                <input type="radio" id="False" name="tf" value="False"/>
                <label for="False">False</label><br/>
                <input type="submit" value="Submit"/>
            </form>
        </div>
        <div v-if="type === 'n'">
            <form action="">
                <input type="text" placeholder="Question"/>
                <input type="text" placeholder="Correct Answer"/>
            </form>
        </div>
        <div v-if="type === 'dd'">
            <!-- <form action="">
                <input type="text" placeholder="Question">
                <textarea name="" id=""></textarea>
            </form> 
            <form @sumbit.prevent="">
                <div v-for="item in array">
                    <input v-if="item === 'q'" type="text" placeholder="Question"/>
                    <input v-if="item === 'b'" type="text" placeholder="Blank" :key="num" disabled>
                </div>
                <button @click.prevent="array.push('b', 'q');  num ++">Add a Blank</button>
                <div v-for="item in array">
                    <p v-if="item === 'b'">Blank: {{ num }}</p>
                    <input v-if="item === 'b'" type="text" placeholder="Blank - answer" :key="'answer' + num" />
                    <div class="incorrect" v-if="item === 'b'">
                        <input v-for="index of n" type="text" placeholder="Incorrect Answer" :key="'incorrect' + num"/>
                        <button v-if="n < 4" @click.prevent="n++">Add Incorrect Answers</button>
                    </div>
                </div>
            </form>
        </div>
    </div>
</template>

<script setup lang="ts">
const props = defineProps<{
    type: string
}>();

const n = ref(2);
const num = ref(0);
const array = reactive<string[]>(['q']);

</script>

<style scoped>

</style> -->

<!-- ^old code -> test new one at school bc mac doesn't want to work :( -->

<template>
  <div>
    <div v-if="type === 'mc'">
      <form>
        <input v-model="mc.question" type="text" placeholder="Question" />
        <input
          v-model="mc.correctAnswer"
          type="text"
          placeholder="Correct Answer"
        />
        <input
          v-for="(answer, index) in mc.wrongAnswers"
          :key="'wrong' + index"
          v-model="mc.wrongAnswers[index]"
          type="text"
          placeholder="Wrong Answer"
        />
      </form>
    </div>

    <div v-if="type === 'tf'">
      <form>
        <input v-model="tf.question" type="text" placeholder="Question" />
        <input
          type="radio"
          id="True"
          name="tf"
          value="True"
          v-model="tf.correctAnswer"
        />
        <label for="True">True</label><br />
        <input
          type="radio"
          id="False"
          name="tf"
          value="False"
          v-model="tf.correctAnswer"
        />
        <label for="False">False</label><br />
        <input type="submit" value="Submit" />
      </form>
    </div>

    <div v-if="type === 'n'">
      <form>
        <input v-model="n.question" type="text" placeholder="Question" />
        <input
          v-model="n.correctAnswer"
          type="text"
          placeholder="Correct Answer"
        />
      </form>
    </div>

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

    <PreviewCard
      :type="type"
      :question="getCurrentQuestion()"
      :correctAnswer="getCurrentCorrectAnswer()"
      :wrongAnswers="getCurrentWrongAnswers()"
      :ddArray="type === 'dd' ? ddArray : undefined"
    />
  </div>
</template>

<script setup lang="ts">
const props = defineProps<{ type: "mc" | "tf" | "n" | "dd" }>();

// define objects for each question type
const mc = reactive({
  question: "",
  correctAnswer: "",
  wrongAnswers: ["", "", ""],
});

const tf = reactive({
  question: "",
  correctAnswer: "",
});

const n = reactive({
  question: "",
  correctAnswer: "",
});

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

// functions for the preview card
function getCurrentQuestion(): string {
  if (props.type === "mc") return mc.question;
  if (props.type === "tf") return tf.question;
  if (props.type === "n") return n.question;
  return "";
}

function getCurrentCorrectAnswer(): string {
  if (props.type === "mc") return mc.correctAnswer;
  if (props.type === "tf") return tf.correctAnswer;
  if (props.type === "n") return n.correctAnswer;
  return "";
}

function getCurrentWrongAnswers(): string[] {
  if (props.type === "mc") return mc.wrongAnswers;
  return [];
}
</script>

<style scoped></style>
