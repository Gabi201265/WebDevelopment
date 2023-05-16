<template>
  <form>
    <div class="mb-3">
      <input required type="text" id="playerName" placeholder="Votre nom" style="color:black"
        v-model="username" />
    </div>
    <button :disabled="!username" @click="launchNewQuiz" type="submit" class="btn btn-primary btn-lg w-100 rounded-pill">
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


<style scoped>

@keyframes shake{
  0%, 100% {translate: 0;}
  25% {translate: 8px 0;}
  75% {translate: -8px 0;}
}
input {
  width: 210px;
  height: 56px;
  padding: 0 16px;
  background: transparent;
  border-radius: 4px;
  border: 1px solid #fe4567;
  color: #f9f9f9;
  animation: shake 0.14s 3;
}

input:valid {
  border-color: #45feaf;
  animation: none;
}

</style>
