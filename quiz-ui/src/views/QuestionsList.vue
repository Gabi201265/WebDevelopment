<template>
<div class="AdminArea">
  <h1>Administrator Area</h1>
  <button class="button" @click="clearScoreboard">Clear scoreboard</button>
  <router-link to="/question-creation">Create question</router-link>
  <h3>Questions List : </h3>
  <div v-for="(question, index) in questionsList" v-bind:key="index" @click="editQuestion(question)"> 
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
</div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";
import QuestionEdition from "@/views/QuestionEdition.vue";

export default {
  name: "QuestionList",
  data() {
      return {
        questionsList:[],
        totalNumberOfQuestion : 0,
        currentQuestion:{
          questionTitle:"",
          questionText:"",
          possibleAnswers:[]
        },
        selectedQuestion: null
      }
      
  },
  components:{
    QuestionEdition
  },
  async created(){
    this.getQuestions();
  },
  methods:{
    async getQuestions(){
      console.log("getting questions");
      const quizInfoAPIResult = await quizApiService.getQuizInfo();
      this.totalNumberOfQuestion = quizInfoAPIResult.data.size;
      for (let i = 0; i < this.totalNumberOfQuestion; i++){
        this.loadQuestionByPosition(i+1);
      }
      console.log("question list:");
      console.log(this.questionsList);
    },
    
    async loadQuestionByPosition(currentPosition){
      var questionInfoAPIResult = await quizApiService.getQuestion(currentPosition);
      this.questionsList[currentPosition-1] = questionInfoAPIResult.data;
    },

    async editQuestion(data){
      this.selectedQuestion = data;
      console.log(this.selectedQuestion);
      this.$router.push({ name: 'QuestionEdition', params: { myEditedQuestion: JSON.stringify(this.selectedQuestion) } });
    },
    async clearScoreboard(){
      const participationDeleteAPIResult = await quizApiService.deleteParticipation();
    },
    logoutAdmin(){
      this.$router.push('/admin')
    }
  }
}
</script>
<style>
.AdminArea{
  padding-top: 30px;
  background: aliceblue;
}

</style>