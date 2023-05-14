<template>
    <div class="ScoreBoard">
      <h3> Votre score : {{ sessionScore }}</h3>
      <h4> Scoreboard :</h4>
      <div v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
        {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
      </div>
    </div>
  </template>
  
  <script>
  import quizApiService from "@/services/QuizApiService";
  
  export default {
    // eslint-disable-next-line vue/multi-word-component-names
    name: "ScoreBoard",
    data() {
      return {
        registeredScores: [],
        sessionScore: 0
      };
    },
    async created() {
        this.sessionScore = this.$route.params.score;
        var quizInfoPromise = quizApiService.getQuizInfo();
        var quizInfoAPIResult = await quizInfoPromise;
        this.registeredScores = quizInfoAPIResult.data.scores;
        console.log("Composant Home page 'created'");
        console.log("Registered Scores :", this.registeredScores);
    },
};
</script>
