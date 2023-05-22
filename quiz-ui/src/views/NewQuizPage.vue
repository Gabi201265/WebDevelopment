<template>
  <div class="newQuizPage">
    <form>
      <div class="mb-3">
        <input class="inputName" required type="text" id="playerName" placeholder="Username"
          v-model="username" />
      </div>
      <button :disabled="!username" @click="launchNewQuiz" type="submit" class="designButton">
        Discover the future !
      </button>
    </form>
  </div>
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


<style>
.newQuizPage {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  padding: 2rem;
  color: #FFFFFF;
  text-align: center;
}

@keyframes shake{
  0%, 100% {translate: 0;}
  25% {translate: 8px 0;}
  75% {translate: -8px 0;}
}
.inputName {
  width: 300px;
  height: 60px;
  padding: 0 20px;
  background: transparent;
  border-radius: 8px;
  border: 2px solid #fe4567;
  color: #FFFFFF;
  font-size: 24px;
  margin-bottom: 20px;
  animation: shake 0.14s 3;
  color: aliceblue;
}
.inputName:valid {
  border-color: #45feaf;
  animation: none;
}

.designButton {
  width: 300px;
  height: 60px;
  padding: 0 20px;
  background-color: #a370f0;
  color: #ffffff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 24px;
}

</style>
