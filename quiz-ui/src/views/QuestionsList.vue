<template>
  <div class="AdminArea">
    <h3>Administrator Area</h3>
    <button class="button" @click="clearScoreboard">Clear scoreboard</button>
    <button class="button" @click="deleteQuestions">Delete All Questions</button>
    <router-link to="/question-creation">
      <button class="button">Create question</button>
    </router-link>
    <h3>Questions List:</h3>
    <div v-for="(question, index) in questionsList" :key="index" @click="editQuestion(question)">
      <div v-if="question">
        position : {{ question.position }} <br>
        title : {{ question.title }} <br>
        text : {{question.text}} <br> <br>
      </div>
      <div v-else>
        Question non définie <br><br>
      </div>
    </div>
    <button @click="logoutAdmin" class="glow-on-hover">Sign out</button>

    <div v-if="showPopup" class="popup">
      {{ popupMessage }}
    </div>
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";
import QuestionEdition from "@/views/QuestionEdition.vue";

export default {
  name: "QuestionList",
  data() {
    return {
      questionsList: [],
      totalNumberOfQuestion: 0,
      currentQuestion: {
        questionTitle: "",
        questionText: "",
        possibleAnswers: []
      },
      selectedQuestion: null,
      showPopup: false,
      popupMessage: ""
    };
  },
  components: {
    QuestionEdition
  },
  async created() {
    this.getQuestions();
  },
  methods: {
    async getQuestions() {
      console.log("getting questions");
      const quizInfoAPIResult = await quizApiService.getQuizInfo();
      this.totalNumberOfQuestion = quizInfoAPIResult.data.size;
      for (let i = 0; i < this.totalNumberOfQuestion; i++) {
        this.loadQuestionByPosition(i + 1);
      }
      console.log("question list:");
      console.log(this.questionsList);
    },

    async loadQuestionByPosition(currentPosition) {
      var questionInfoAPIResult = await quizApiService.getQuestion(currentPosition);
      this.questionsList[currentPosition - 1] = questionInfoAPIResult.data;
    },

    async editQuestion(data) {
      this.selectedQuestion = data;
      console.log(this.selectedQuestion);
      this.$router.push({ name: "QuestionEdition", params: { myEditedQuestion: JSON.stringify(this.selectedQuestion) } });
    },

    async clearScoreboard() {
      const token = window.localStorage.getItem("token");
      const participationDeleteAPIResult = await quizApiService.deleteParticipation(token);

      this.showPopup = true;
      this.popupMessage = "All participations have been deleted";

      setTimeout(() => {
        this.showPopup = false;
      }, 1000);
    },

    async deleteQuestions() {
      const token = window.localStorage.getItem("token");
      const allQuestionsDeleteAPIResult = await quizApiService.deleteAllQuestions(token);

      this.showPopup = true;
      this.popupMessage = "All questions have been deleted";

      setTimeout(() => {
        this.showPopup = false;
      }, 1000);
    },

    logoutAdmin() {
      this.$router.push("/admin");
    }
  }
};
</script>

<style>
.AdminArea {
  color: white;
  flex-direction: column;
  padding: 2rem;
  margin-top: 5rem;
  color: #FFFFFF;
}

.popup {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: blue;
  color: white;
  padding: 1rem;
  border-radius: 5px;
  z-index: 999;
}
</style>
