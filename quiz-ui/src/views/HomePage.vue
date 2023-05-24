<template>
  <div>
    <div class="parallax-wrapper">
      <div class="parallax">
        <div class="parallax-item parallax-item_0">
          <img src="/src/img/sky_01.png" alt="sky" />
        </div>
        <div class="parallax-item parallax-item_1">
          <img src="/src/img/loon_3.png" alt="sky" width="145" height="145" />
        </div>
        <div class="parallax-item parallax-item_2">
          <img src="/src/img/loon_1.png" alt="sky" width="75" height="75" />
        </div>
        <div class="parallax-item parallax-item_3">
          <img src="/src/img/loon_2.png" alt="sky" width="145" height="145" />
        </div>
        <div class="parallax-item parallax-item_4">
          <img src="/src/img/rock_03.png" alt="rock" />
        </div>
        <div class="parallax-item parallax-item_5">
          <img src="/src/img/rock_05.png" alt="rock" />
        </div>
        <div class="parallax-item parallax-item_6">
          <img src="/src/img/rock_04.png" alt="rock" />
        </div>
        <div class="parallax-item parallax-item_7">
          <img src="/src/img/rock_06.png" alt="rock" />
        </div>
        <div class="rounded-text">
          Welcome to the new world ! <br>
          <a href="#bottom" class="scroll-link">Travel to the new world</a>
        </div>
        <span class="parallax-cover" id="bottom">
          <div class="afterHeader">
            <h2>Total Score Board</h2>
            <div class="score-container">
              <div class="score-board">
                <div class="score-column" v-for="column in scoreColumns" v-bind:key="column.id">
                  <div class="score-entry" v-for="scoreEntry in column.scores">
                    {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
                  </div>
                </div>
              </div>
              <div class="top-scores">
                <h2>Master of spiritual elevation</h2>
                <div class="top-scores-list" >
                  <span v-for="(bestScore, index) in topScores()">
                    <img v-if="index === 0" src="/src/assets/icons/1st-place-medal.svg"/>
                    <img v-else-if="index === 1" src="/src/assets/icons/2nd-place-medal.svg"/>
                    <img v-else-if="index === 2" src="/src/assets/icons/3rd-place-medal.svg"/>
                    - {{ bestScore.playerName }}
                  </span>
                </div>
              </div>
            </div>
            <h3>Start the journey !</h3>
            <router-link to="/start-new-quiz-page" class="glow-on-hover">
              <button class="buttonMagic custom-button">TRAVEL ! 
                <div class="star-1">
                  <svg xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 784.11 815.53" style="shape-rendering:geometricPrecision; text-rendering:geometricPrecision; image-rendering:optimizeQuality; fill-rule:evenodd; clip-rule:evenodd" version="1.1" xml:space="preserve" xmlns="http://www.w3.org/2000/svg"><defs></defs><g id="Layer_x0020_1"><metadata id="CorelCorpID_0Corel-Layer"></metadata><path d="M392.05 0c-20.9,210.08 -184.06,378.41 -392.05,407.78 207.96,29.37 371.12,197.68 392.05,407.74 20.93,-210.06 184.09,-378.37 392.05,-407.74 -207.98,-29.38 -371.16,-197.69 -392.06,-407.78z" class="fil0"></path></g></svg>
                </div>
                <div class="star-2">
                  <svg xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 784.11 815.53" style="shape-rendering:geometricPrecision; text-rendering:geometricPrecision; image-rendering:optimizeQuality; fill-rule:evenodd; clip-rule:evenodd" version="1.1" xml:space="preserve" xmlns="http://www.w3.org/2000/svg"><defs></defs><g id="Layer_x0020_1"><metadata id="CorelCorpID_0Corel-Layer"></metadata><path d="M392.05 0c-20.9,210.08 -184.06,378.41 -392.05,407.78 207.96,29.37 371.12,197.68 392.05,407.74 20.93,-210.06 184.09,-378.37 392.05,-407.74 -207.98,-29.38 -371.16,-197.69 -392.06,-407.78z" class="fil0"></path></g></svg>
                </div>
                <div class="star-3">
                  <svg xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 784.11 815.53" style="shape-rendering:geometricPrecision; text-rendering:geometricPrecision; image-rendering:optimizeQuality; fill-rule:evenodd; clip-rule:evenodd" version="1.1" xml:space="preserve" xmlns="http://www.w3.org/2000/svg"><defs></defs><g id="Layer_x0020_1"><metadata id="CorelCorpID_0Corel-Layer"></metadata><path d="M392.05 0c-20.9,210.08 -184.06,378.41 -392.05,407.78 207.96,29.37 371.12,197.68 392.05,407.74 20.93,-210.06 184.09,-378.37 392.05,-407.74 -207.98,-29.38 -371.16,-197.69 -392.06,-407.78z" class="fil0"></path></g></svg>
                </div>
                <div class="star-4">
                  <svg xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 784.11 815.53" style="shape-rendering:geometricPrecision; text-rendering:geometricPrecision; image-rendering:optimizeQuality; fill-rule:evenodd; clip-rule:evenodd" version="1.1" xml:space="preserve" xmlns="http://www.w3.org/2000/svg"><defs></defs><g id="Layer_x0020_1"><metadata id="CorelCorpID_0Corel-Layer"></metadata><path d="M392.05 0c-20.9,210.08 -184.06,378.41 -392.05,407.78 207.96,29.37 371.12,197.68 392.05,407.74 20.93,-210.06 184.09,-378.37 392.05,-407.74 -207.98,-29.38 -371.16,-197.69 -392.06,-407.78z" class="fil0"></path></g></svg>
                </div>
                <div class="star-5">
                  <svg xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 784.11 815.53" style="shape-rendering:geometricPrecision; text-rendering:geometricPrecision; image-rendering:optimizeQuality; fill-rule:evenodd; clip-rule:evenodd" version="1.1" xml:space="preserve" xmlns="http://www.w3.org/2000/svg"><defs></defs><g id="Layer_x0020_1"><metadata id="CorelCorpID_0Corel-Layer"></metadata><path d="M392.05 0c-20.9,210.08 -184.06,378.41 -392.05,407.78 207.96,29.37 371.12,197.68 392.05,407.74 20.93,-210.06 184.09,-378.37 392.05,-407.74 -207.98,-29.38 -371.16,-197.69 -392.06,-407.78z" class="fil0"></path></g></svg>
                </div>
                <div class="star-6">
                  <svg xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 784.11 815.53" style="shape-rendering:geometricPrecision; text-rendering:geometricPrecision; image-rendering:optimizeQuality; fill-rule:evenodd; clip-rule:evenodd" version="1.1" xml:space="preserve" xmlns="http://www.w3.org/2000/svg"><defs></defs><g id="Layer_x0020_1"><metadata id="CorelCorpID_0Corel-Layer"></metadata><path d="M392.05 0c-20.9,210.08 -184.06,378.41 -392.05,407.78 207.96,29.37 371.12,197.68 392.05,407.74 20.93,-210.06 184.09,-378.37 392.05,-407.74 -207.98,-29.38 -371.16,-197.69 -392.06,-407.78z" class="fil0"></path></g></svg>
                </div>
              </button>
            </router-link>
          </div>
        </span>
      </div>
    </div>
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";

export default {
  name: "HomePage",
  data() {
    return {
      registeredScores: [],
      scoreColumns: [] // Tableau pour stocker les colonnes de scores
    };
  },
  async created() {
    var quizInfoPromise = quizApiService.getQuizInfo();
    var quizInfoAPIResult = await quizInfoPromise;
    this.registeredScores = quizInfoAPIResult.data.scores;
    this.updateScoreColumns(); // Appeler la fonction pour mettre à jour les colonnes de scores
    console.log("Composant Home page 'created'");
    console.log("Registered Scores :", this.registeredScores);
  },
  methods: {
    topScores() {
      const topThreeScores = this.registeredScores.slice(0, 3); // Récupérer uniquement les trois premiers scores
      return topThreeScores.map((score, index) => ({
        ...score,
        stars: Array(3-index).fill(0) // Générer un tableau avec le nombre d'étoiles correspondant au score
      }));
    },
    updateScoreColumns() {
      const columnCount = Math.ceil(this.registeredScores.length / 10); // Calculer le nombre de colonnes nécessaires
      this.scoreColumns = []; // Réinitialiser le tableau des colonnes
      for (let i = 0; i < columnCount; i++) {
        const start = i * 10; // Indice de début de la colonne
        const end = (i + 1) * 10; // Indice de fin de la colonne
        const scores = this.registeredScores.slice(start, end); // Extraire les scores pour la colonne actuelle
        this.scoreColumns.push({ id: i, scores }); // Ajouter la colonne au tableau des colonnes
      }
    }
  }
};
</script>


<style>

.afterHeader {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  padding: 2rem;
  color: #FFFFFF;
  text-align: center;
  margin-top: 2rem;
}
.score-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.score-board {
  margin-bottom: 1.5rem;
  display: flex;
  flex-wrap: wrap; /* Permettre le retour à la ligne des colonnes */
  justify-content: center;
}

.score-column {
  margin: 0 1rem; /* Espacement entre les colonnes */
}

.score-entry {
  margin-bottom: 0.5rem; /* Espacement entre les scores */
}

.top-scores {
  margin-bottom: 1.5rem;
}

.top-scores-list {
  text-align: left;
  align-items: center;
  justify-content: center;
  display: flex;
}

.top-scores-list span {
  display: flex;
  align-items: center;
  font-size: 24px;
}

.top-scores-list img {
  width: 40px; 
  margin-left: 20px; 
}

.top-scores-list span:not(:last-child) {
  margin-right: 10px;
}

h2, h3 {
  font-size: 2.5rem;
  font-weight: bold;
  margin-bottom: 1.5rem;
}

.rounded-text {
  text-align: center;
  font-size: 24px;
  border-radius: 10px;
  background-color: rgba(255, 255, 255, 0.7); /* Couleur de fond avec transparence */
  padding: 20px;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: #2c3e50;
}

.scroll-link {
  display: block;
  text-align: center;
  margin-top: 10px;
  color: #7cc4fb; /* Couleur du lien */
  font-weight: bold; /* Texte en gras */
  text-decoration: none; /* Soulignement du lien */
}

.scroll-link:hover {
  color: #8c4ad8; /* Couleur de surlignement */
}


/* Le bouton */
.custom-button {
  position: relative;
  padding: 12px 35px;
  background: #a370f0;
  font-size: 17px;
  font-weight: 500;
  /* color: #181818; */
  color: white;
  border: 3px solid #a370f0;
  border-radius: 8px;
  box-shadow: 0 0 0 #fec1958c;
  transition: all .3s ease-in-out;
  margin-top: 1em;
}

.star-1 {
  position: absolute;
  top: 20%;
  left: 20%;
  width: 25px;
  height: auto;
  filter: drop-shadow(0 0 0 #fffdef);
  z-index: -5;
  transition: all 1s cubic-bezier(0.05, 0.83, 0.43, 0.96);
}

.star-2 {
  position: absolute;
  top: 45%;
  left: 45%;
  width: 15px;
  height: auto;
  filter: drop-shadow(0 0 0 #fffdef);
  z-index: -5;
  transition: all 1s cubic-bezier(0, 0.4, 0, 1.01);
}

.star-3 {
  position: absolute;
  top: 40%;
  left: 40%;
  width: 5px;
  height: auto;
  filter: drop-shadow(0 0 0 #fffdef);
  z-index: -5;
  transition: all 1s cubic-bezier(0, 0.4, 0, 1.01);
}

.star-4 {
  position: absolute;
  top: 20%;
  left: 40%;
  width: 8px;
  height: auto;
  filter: drop-shadow(0 0 0 #fffdef);
  z-index: -5;
  transition: all .8s cubic-bezier(0, 0.4, 0, 1.01);
}

.star-5 {
  position: absolute;
  top: 25%;
  left: 45%;
  width: 15px;
  height: auto;
  filter: drop-shadow(0 0 0 #fffdef);
  z-index: -5;
  transition: all .6s cubic-bezier(0, 0.4, 0, 1.01);
}

.star-6 {
  position: absolute;
  top: 5%;
  left: 50%;
  width: 5px;
  height: auto;
  filter: drop-shadow(0 0 0 #fffdef);
  z-index: -5;
  transition: all .8s ease;
}

.custom-button:hover {
  background: transparent;
  color: #a370f0;
  box-shadow: 0 0 25px #fec1958c;
}

.custom-button:hover .star-1 {
  position: absolute;
  top: -80%;
  left: -30%;
  width: 25px;
  height: auto;
  filter: drop-shadow(0 0 10px #fffdef);
  z-index: 2;
}

.custom-button:hover .star-2 {
  position: absolute;
  top: -25%;
  left: 10%;
  width: 15px;
  height: auto;
  filter: drop-shadow(0 0 10px #fffdef);
  z-index: 2;
}

.custom-button:hover .star-3 {
  position: absolute;
  top: 55%;
  left: 25%;
  width: 5px;
  height: auto;
  filter: drop-shadow(0 0 10px #fffdef);
  z-index: 2;
}

.custom-button:hover .star-4 {
  position: absolute;
  top: 30%;
  left: 80%;
  width: 8px;
  height: auto;
  filter: drop-shadow(0 0 10px #fffdef);
  z-index: 2;
}

.custom-button:hover .star-5 {
  position: absolute;
  top: 25%;
  left: 115%;
  width: 15px;
  height: auto;
  filter: drop-shadow(0 0 10px #fffdef);
  z-index: 2;
}

.custom-button:hover .star-6 {
  position: absolute;
  top: 5%;
  left: 60%;
  width: 5px;
  height: auto;
  filter: drop-shadow(0 0 10px #fffdef);
  z-index: 2;
}

.fil0 {
  fill: #FFFDEF
}

/* Le fond ! */
.parallax-wrapper {
  position: relative;
  height: 100vh;
  width: 100%;
  overflow: hidden;
  /* border-radius: 15px; */
}
.parallax-cover {
  background: #372883;
  display: block;
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  z-index: 2;
}
.parallax {
  perspective: 100px;
  background-color: #fb87db;
  overflow-x: hidden;
  overflow-y: auto;
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
}

.parallax-item {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
}

.parallax-item img {
  position: absolute;
  left: 0;
  bottom: 0;
}

.parallax-item_0 img {
  width: 100%;
}

.parallax-item_1 img {
  left: 50%;
  transform: translateX(-50px);
  margin-left: -20px;
}

.parallax-item_0 {
  transform: translateZ(-350px) scale(4.5);
}

.parallax-item_1 {
  transform: translateZ(-300px) scale(4);
}

.parallax-item_2 {
  transform: translateZ(-250px) scale(3.5);
}

.parallax-item_3 {
  transform: translateZ(-200px) scale(3);
}

.parallax-item_4 {
  transform: translateZ(-150px) scale(2.5);
}

.parallax-item_5 {
  transform: translateZ(-100px) scale(2);
}

.parallax-item_6 {
  transform: translateZ(-50px) scale(1.5);
}

.parallax-item_7 {
  transform: translateZ(0px) scale(1);
}

.parallax-item_1 img {
  bottom: 100px;
  left: auto;
  right: 200px;
}

.parallax-item_2 img {
  bottom: 300px;
  left: auto;
  right: 50px;
}

.parallax-item_3 img {
  bottom: 300px;
}

.parallax-item_4 img {
  bottom: 200px;
}

.parallax-item_6 img {
  right: 0;
  left: auto;
}

.parallax-item_5 img {
  left: -5px;
  bottom: -6px;
}

</style>