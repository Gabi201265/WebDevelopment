<template>
  <div class="QuestionDisplay">
    <div class="title">{{ question.title }}</div>
    <div class="question-text">{{ question.text }}</div>
    <div class="question-container">
      <img v-if="question.image" :src="question.image" class="question-image" />
      <div class="container">
        <form>
          <label v-for="(answer, index) in question.possibleAnswers" :key="index">
            <input type="radio" name="radio" @change="handleAnswerChange(index)" />
            <span>{{ answer.text }}</span>
          </label>
        </form>
      </div>
    </div>
    <button class="cssbuttons-io"  @click="$emit('answer-selected', selectedIndex)">
      <span><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M13 17l5-5-5-5M6 17l5-5-5-5"/></svg> Next</span>
    </button>
  </div>
</template>

<script>
export default {
  name: "QuestionDisplay",
  emits: ["answer-selected"],
  data() {
    return {
      selectedIndex: null
    };
  },
  props: {
    question: {
      type: Object
    }
  },
  methods: {
    handleAnswerChange(index) {
      this.selectedIndex = index;
      console.log(this.selectedIndex);
    }
  }
};
</script>

<style>
.QuestionDisplay {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  margin-bottom: 20px;
  position: relative; /* Ajout */
}

.title {
  font-size: 24px;
  margin-bottom: 10px;
}

.question-text {
  font-size: 18px;
  margin-bottom: 20px;
}

.question-container {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 20px;
}

.question-image {
  width: 200px;
  height: auto;
  margin-right: 20px;
}

.cssbuttons-io {
  position: relative;
  font-family: inherit;
  font-weight: 500;
  font-size: 18px;
  letter-spacing: 0.05em;
  border-radius: 0.8em;
  border: none;
  background: linear-gradient(to right, #8e2de2, #4a00e0);
  /* background: linear-gradient(to right,#7cc4fb, #8c4ad8); */
  color: ghostwhite;
  overflow: hidden;
}

.cssbuttons-io svg {
  width: 1.2em;
  height: 1.2em;
  margin-right: 0.5em;
}

.cssbuttons-io span {
  position: relative;
  z-index: 10;
  transition: color 0.4s;
  display: inline-flex;
  align-items: center;
  padding: 0.8em 1.2em 0.8em 1.05em;
}

.cssbuttons-io::before,
.cssbuttons-io::after {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 0;
}

.cssbuttons-io::before {
  content: "";
  background: #000;
  width: 120%;
  left: -10%;
  transform: skew(30deg);
  transition: transform 0.4s cubic-bezier(0.3, 1, 0.8, 1);
}

.cssbuttons-io:hover::before {
  transform: translate3d(100%, 0, 0);
}

.cssbuttons-io:active {
  transform: scale(0.95);
}

.container form {
  display: flex;
  flex-wrap: wrap;
  flex-direction: column;
}

.container label {
  display: flex;
  cursor: pointer;
  font-weight: 500;
  position: relative;
  overflow: hidden;
  margin-bottom: 0.375em;
}

.container  label input {
  position: absolute;
  left: -9999px;
}

.container label input:checked + span {
  background-color: #414181;
  color: #7cc4fb;
}

.container label input:checked + span:before {
  box-shadow: inset 0 0 0 0.4375em #00005c;
}

.container label span {
  display: flex;
  align-items: center;
  padding: 0.375em 0.75em 0.375em 0.375em;
  border-radius: 99em;
  transition: 0.25s ease;
  color: white;
}

.container label span:hover {
  background-color: #d6d6e5;
}

.container label span:before {
  display: flex;
  flex-shrink: 0;
  content: "";
  background-color: #fff;
  width: 1.5em;
  height: 1.5em;
  border-radius: 50%;
  margin-right: 0.375em;
  transition: 0.25s ease;
  box-shadow: inset 0 0 0 0.125em #00005c;
}

</style>
