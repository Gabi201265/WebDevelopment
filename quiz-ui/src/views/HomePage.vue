<template>
  <div>
    <h1>Home page</h1>
    <div v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
      {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
    </div>
    <router-link to="/start-new-quiz-page" class="glow-on-hover">
      <button class="cssbuttons-io-button"> Démarrer le quiz !
        <div class="icon">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24"><path fill="none" d="M0 0h24v24H0z"></path><path fill="currentColor" d="M16.172 11l-5.364-5.364 1.414-1.414L20 12l-7.778 7.778-1.414-1.414L16.172 13H4v-2z"></path></svg>
        </div>
      </button>
    </router-link>
    <h1>Top scores :</h1>
    <div v-for="bestScore in topScores()" v-bind:key="bestScore.date">
      {{ bestScore.playerName }} - {{ bestScore.score }}
    </div>
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
  },
  methods: {
    topScores() {
      return this.registeredScores.slice(0, 3); // Récupérer uniquement les trois premiers scores
    }
  }
};
</script>

<style>
.cssbuttons-io-button {
  background: #A370F0;
  color: white;
  font-family: inherit;
  padding: 0.35em;
  padding-left: 1.2em;
  font-size: 17px;
  font-weight: 500;
  border-radius: 0.9em;
  border: none;
  letter-spacing: 0.05em;
  display: flex;
  align-items: center;
  box-shadow: inset 0 0 1.6em -0.6em #714da6;
  overflow: hidden;
  position: relative;
  height: 2.8em;
  padding-right: 3.3em;
}

.cssbuttons-io-button .icon {
  background: white;
  margin-left: 1em;
  position: absolute;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 2.2em;
  width: 2.2em;
  border-radius: 0.7em;
  box-shadow: 0.1em 0.1em 0.6em 0.2em #7b52b9;
  right: 0.3em;
  transition: all 0.3s;
}

.cssbuttons-io-button:hover .icon {
  width: calc(100% - 0.6em);
}

.cssbuttons-io-button .icon svg {
  width: 1.1em;
  transition: transform 0.3s;
  color: #7b52b9;
}

.cssbuttons-io-button:hover .icon svg {
  transform: translateX(0.1em);
}

.cssbuttons-io-button:active .icon {
  transform: scale(0.95);
}

</style>

 <!-- <template>
  <div class="home-page">
    <div class="content">
      <h1>Bienvenue sur le Quizz Futuriste</h1>
      <p>Testez vos connaissances dans un monde futuriste et moderne</p>
      <button class="start-button" @click="startQuiz">Démarrer le Quizz</button>
    </div>
    <div class="scoreboard">
      <h2>Tableau des Scores</h2>
      <table>
        <thead>
          <tr>
            <th>Position</th>
            <th>Joueur</th>
            <th>Score</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(score, index) in globalScores" :key="index">
            <td>{{ index + 1 }}</td>
            <td>{{ score.player }}</td>
            <td>{{ score.score }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="top-scores">
      <h2>Meilleurs Scores</h2>
      <div v-for="(score, index) in topScores" :key="index" class="score">
        <div class="medal">{{ index + 1 }}</div>
        <div class="player">{{ score.player }}</div>
        <div class="score-value">{{ score.score }}</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      globalScores: [
        { player: "Joueur 1", score: 95 },
        { player: "Joueur 2", score: 88 },
        { player: "Joueur 3", score: 72 },
        // Ajoutez d'autres scores ici
      ],
      topScores: [
        { player: "Joueur 1", score: 95 },
        { player: "Joueur 2", score: 88 },
        { player: "Joueur 3", score: 72 },
      ],
    };
  },
  methods: {
    startQuiz() {
      // Code pour démarrer le quiz
    },
  },
};
</script>

<style scoped>
.home-page {
  background: transparent;
  backdrop-filter: blur(10px);
  transition: all .3s ease-in;
  color: #ffffff;
  padding: 50px;
  text-align: center;
}

.content {
  margin-bottom: 30px;
}

h1 {
  font-size: 36px;
  margin-bottom: 20px;
}

p {
  font-size: 18px;
  margin-bottom: 30px;
}

.start-button {
  background-color: #9f5afd;
  color: #ffffff;
  border: none;
  padding: 12px 24px;
  font-size: 16px;
  border-radius: 4px;
  cursor: pointer;
}

.scoreboard {
  background-color: #2a2351;
  padding: 30px;
  margin-bottom: 30px;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

th,
td {
  padding: 10px;
  border-bottom: 1px solid #ffffff;
}

th {
  text-align: left;
  font-weight: bold;
}

.top-scores {
  background-color: #2a2351;
  padding: 30px;
  display: flex;
  justify-content: space-around;
}

.score {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.medal {
  width: 60px;
  height: 60px;
  background-color: #9f5afd;
  color: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
  font-weight: bold;
  border-radius: 50%;
  margin-bottom: 10px;
}

.player {
  font-size: 18px;
  margin-bottom: 5px;
}

.score-value {
  font-size: 24px;
  font-weight: bold;
}
</style> -->