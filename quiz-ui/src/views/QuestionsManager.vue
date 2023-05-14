<template>
  <div class="questions">
    <!--h1>This is the questions page</h1-->
    <h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }}</h1>
    <QuestionDisplay :question="currentQuestion" @answer-selected="answerClickedHandler" />
      <div class="flex">
        <router-link to="/">Accueil</router-link>
        <router-link to="/start-new-quiz-page">Rejouer</router-link>
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
      player:{
        playerName:"",
        answers :[]
      },
      score: 0,
      // display: true,
      // displayScoreboard : false,
      registeredScores: [],
      currentQuestionPosition: 1,
      totalNumberOfQuestion: 0,
      currentQuestion:{
        questionTitle:"",
        questionText:"",
        possibleAnswers:[],
        image:""
      }
    }
  },
  components:{
    QuestionDisplay
  },
  async created(){
    const quizInfoAPIResult = await quizApiService.getQuizInfo();
    if (quizInfoAPIResult.status === 200){
      this.player.playerName = participationStorageService.getPlayerName();
      this.totalNumberOfQuestion= quizInfoAPIResult.data.size;
      this.loadQuestionByPosition(this.currentQuestionPosition);
    }
    else{
      console.error("Error, could not find info quizz.")
    }
  },
  methods: {
    async loadQuestionByPosition(currentPosition){
      const questionInfo = await quizApiService.getQuestion(currentPosition);
      if (questionInfo.status === 200){
        this.currentQuestion = questionInfo.data;
        console.log(this.currentQuestion);
      }
      else{
        console.error("Error, could not load current question.")
      }
    },
    async answerClickedHandler(selectedAnswerPosition){
      console.log("Select answer with the position : " + selectedAnswerPosition);
      // Pour être raccord avec la partie quizApiService, et la colonne position de nos réponses !
      this.player.answers[this.currentQuestionPosition-1] = selectedAnswerPosition+1;
      // Récupérationd e la question pour vérifier si le joueur a la bonne réponse (comme pour ce que l'on a fait dans l'api) !
      let rightAnswer = this.getRightAnswer();
      // Fin du quizz si c'est la dernière question
      if (this.currentQuestionPosition == this.totalNumberOfQuestion){
        this.endQuiz();
      }
      else{
        // Si bonne réponse, on incrémente le score
        if (rightAnswer == selectedAnswerPosition){
          this.score++;
          console.log("Score : " + this.score);
        }
        // On passe à la question suivante
        this.currentQuestionPosition++;
        this.loadQuestionByPosition(this.currentQuestionPosition);
      }

    },
    async endQuiz(){
      const postPlayerResult = await quizApiService.postScore(this.player);
      console.log("Score total : " + this.score);
      participationStorageService.saveParticipationScore(this.score);
      console.log(participationStorageService.getParticipationScore());
      this.$router.push(`/scoreboard/${this.score}`);
    },
    getRightAnswer: function (){
      var i = 0;
      for (const answer of this.currentQuestion.possibleAnswers){
        console.log(answer);
        if (answer.isCorrect == true) return i;
        else i++;
      }
    }
  }
};
</script>