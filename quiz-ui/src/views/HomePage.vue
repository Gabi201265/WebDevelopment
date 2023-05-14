<template>
  <div>
    <h1>Home page</h1>
    <div v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
      {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
    </div>
    <router-link to="/start-new-quiz-page" class="glow-on-hover">Démarrer le quiz !</router-link>
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";

export default {
  name: "HomePage",
  data() {
    return {
      registeredScores: []
    };
  },
  async created() {
    var quizInfoPromise = quizApiService.getQuizInfo();
    var quizInfoAPIResult = await quizInfoPromise;
    this.registeredScores = quizInfoAPIResult.data.scores;
    console.log("Composant Home page 'created'");
    console.log("Registered Scores :", this.registeredScores);
  }
};
</script>

<style>
h1 {
  padding: 0%
}

a {
  text-align: center;
}
</style>