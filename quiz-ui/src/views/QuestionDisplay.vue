<template>
  <div class="QuestionDisplay">
    <h1>{{ question.title }}</h1>
    <h2>{{ question.text }}</h2>
    <img v-if="question.image" :src="question.image" />
    <!-- Affichage des reponses -->
    <div class="container">
      <div v-for="(answer, index) in question.possibleAnswers" v-bind:key="answer.position" @click="$emit('answer-selected', index)">
      {{ answer.text }} 
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "QuestionDisplay",
  emits: ["answer-selected"],
  data() {
    return {}
  },
  props: {
    question: {
      type: Object
    }
  },
  methods: {
    selectAnswer(index) {
      const selectedAnswerId = index+1;
      this.$emit('answer-selected', selectedAnswerId);
    }
  }
};
</script>
