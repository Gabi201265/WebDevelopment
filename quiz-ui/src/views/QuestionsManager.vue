<template>
  <div class="questionsManager">
    <div class="questionCounter">{{ currentQuestionPosition }} / {{ totalNumberOfQuestion }}</div>
    <h1>Question {{ currentQuestionPosition }}</h1>
    <QuestionDisplay :question="currentQuestion" @answer-selected="answerClickedHandler" />
    <div class="replayButton">
      <router-link to="/start-new-quiz-page">
        <button class="replayText">Try again</button>
      </router-link>
    </div>
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";
import QuestionDisplay from "@/views/QuestionDisplay.vue";
import participationStorageService from "@/services/ParticipationStorageService";

export default {
  name: "QuestionManager",
  data() {
    return {
      player: {
        playerName: "",
        answers: []
      },
      score: 0,
      registeredScores: [],
      currentQuestionPosition: 1,
      totalNumberOfQuestion: 0,
      currentQuestion: {
        questionTitle: "",
        questionText: "",
        possibleAnswers: [],
        image: ""
      }
    };
  },
  components: {
    QuestionDisplay
  },
  async created() {
    const quizInfoAPIResult = await quizApiService.getQuizInfo();
    if (quizInfoAPIResult.status === 200) {
      this.player.playerName = participationStorageService.getPlayerName();
      this.totalNumberOfQuestion = quizInfoAPIResult.data.size;
      this.loadQuestionByPosition(this.currentQuestionPosition);
    } else {
      console.error("Error, could not find quiz info.");
    }
  },
  methods: {
    async loadQuestionByPosition(currentPosition) {
      const questionInfo = await quizApiService.getQuestion(currentPosition);
      if (questionInfo.status === 200) {
        this.currentQuestion = questionInfo.data;
      } else {
        console.error("Error, could not load current question.");
      }
    },
    async answerClickedHandler(selectedAnswerPosition) {
      console.log("Select answer with the position: " + selectedAnswerPosition);
      this.player.answers[this.currentQuestionPosition - 1] = selectedAnswerPosition + 1;
      let rightAnswer = this.getRightAnswer();
      if (rightAnswer === selectedAnswerPosition) {
        this.score++;
      }
      if (this.currentQuestionPosition === this.totalNumberOfQuestion) {
        this.endQuiz();
      } else {
        this.currentQuestionPosition++;
        this.loadQuestionByPosition(this.currentQuestionPosition);
      }
    },
    async endQuiz() {
      const postPlayerResult = await quizApiService.postScore(this.player);
      participationStorageService.saveParticipationScore(this.score);
      this.$router.push(`/scoreboard/${this.score}`);
    },
    getRightAnswer() {
      let i = 0;
      for (const answer of this.currentQuestion.possibleAnswers) {
        if (answer.isCorrect) return i;
        else i++;
      }
    }
  }
};
</script>

<style>
.questionsManager {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  padding: 2rem;
  color: #ffffff;
  text-align: center;
  margin-top: 5rem;
  overflow: hidden;
}

.questionCounter {
  position: absolute;
  top: 2rem;
  right: 1rem;
  padding: 0.5rem;
  background-color: #ffffff;
  color: #372883;
  border-radius: 4px;
}
.replayButton {
  position: absolute;
  top: 1rem;
  left: 1rem;
  background-color: #ffffff;
  padding: 0.5rem;
  border-radius: 4px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.replayButton .replayText {
  background-color: transparent;
  color: #372883;
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 4px;
  font-size: 18px;
  cursor: pointer;
  outline: none;
  text-decoration: none;
}

.replayButton:hover {
  background-color: #f5f5f5;
}
</style>
