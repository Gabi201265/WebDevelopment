<template>
  <form>
    <div class="mb-3">
      <label for="playerName" class="form-label h5 text-white">Entrez votre nom :</label>
      <input type="text" class="form-control form-control-lg" id="playerName" placeholder="Votre nom"
        v-model="username" />
    </div>
    <button @click="launchNewQuiz" type="submit" class="btn btn-primary btn-lg w-100 rounded-pill">
      Découvrir mon avenir
    </button>
  </form>
</template>

<script>
import participationStorageService from "@/services/ParticipationStorageService";

export default {
  name: 'NewQuizPage',
  data() {
    return {
      username: ''
    };
  },
  methods: {
    launchNewQuiz() {
      participationStorageService.savePlayerName(this.username);
      console.log("Launch new quiz with", participationStorageService.getPlayerName());
      this.$router.push('/questions');
    },
  }
}
</script>
