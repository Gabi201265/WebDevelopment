<template>
  <div class="ScoreBoard">
    <h3 class="endGame"> Good game ! </h3>
    <div class="grid-container">
      <div class="pastParticipations">
        <p class="pastParticipationsTitle">Past participations :</p>
        <span v-for="topScore in pastParticipations" :key="topScore.id">
          Score : {{ topScore[2] }}
        </span>
      </div>
      <div class="playerName">
        <h2>Pseudo : {{ playername }}</h2>
        <p class="yourScores">Your score : {{ sessionScore }}</p>
        <p class="ranking">Ranking : {{ ranking }}</p>
      </div>
    </div>
    <button class="buttonMagic custom-button-scoreboard" @click="backToHomePage">Home !
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
  </div>
</template>
  
  <script>
  import quizApiService from "@/services/QuizApiService.js";
  import participationStorageService from "@/services/ParticipationStorageService.js"
  export default {
  name: 'ScorePage',
  data() {
    return {
      playername: "",
      ranking: 0, 
      sessionScore: 0,
      pastParticipations: [],
      registeredScores: [] 
    };
  },
  async created() {
    this.sessionScore = this.$route.params.score;
    this.playername = participationStorageService.getPlayerName();
    this.getParticipations();
  },
  methods: {
    backToHomePage() {
      participationStorageService.clear();
      this.$router.push('/');
    },
    async getParticipations(){
      try {
        const getAllParticipationsAPIResult = await quizApiService.getAllParticipations();
        if (getAllParticipationsAPIResult.status === 200) {
          const scores = getAllParticipationsAPIResult.data.scores;
          console.log("Scores " + scores);
          const lastParticipation = scores.length;
          let currentId = 0;
          for(let i=0; i<lastParticipation; i++){
            if(scores[i][1] === this.playername){
              this.pastParticipations.push(scores[i]);
            }
            if(scores[i][1] === this.playername && scores[i][0] > currentId){
              this.ranking = i+1;
              currentId = scores[i][0];                    
            }
            
          }
          if (this.ranking == 1){
            this.ranking=`${this.ranking}st`;
          }
          else if (this.ranking == 2) {
            this.ranking=`${this.ranking}nd`;
          } 
          else if (this.ranking == 3) {
            this.ranking=`${this.ranking}rd`;
          } 
          else if (this.ranking >= 4) {
            this.ranking=`${this.ranking}th`;
          } 
        }
        else {
          console.error("Erreur lors de la récupération des scores du quiz");
        }
      } catch (error) {
        console.error("Erreur lors de la requête API", error);
      }
    }
  },
};
</script>
<style>
.ScoreBoard{
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  padding: 2rem;
  color: #FFFFFF;
  text-align: center;
}

.playerName{
  margin-bottom: 2em;
  margin-left:-17em;
  text-align: center;
}
.grid-container {
  display: grid;
  width: 100%;
  grid-template-columns:15em 1fr;
}

.pastParticipations{
  margin-top: -2em;
  display: flex;
  flex-direction: column;
  border: 4px solid white; /* Définit une bordure d'épaisseur 1 pixel et de couleur noire */
  padding: 10px; /* Ajoute un espace de remplissage autour du texte pour éviter qu'il ne touche la bordure */
}
.pastParticipations:hover{
  background: linear-gradient(45deg, #8c4ad8, #7cc4fb);
  /* background: linear-gradient(to right, #8e2de2, #4a00e0); */
}
.pastParticipationsTitle {
  border-bottom: 2px solid white;
  font-size: large;
}

.endGame{ 
  color: aliceblue;
  margin-bottom: 1em;
  font-size: 4rem;
}
.endGame:hover{
  background: linear-gradient(45deg, #7cc4fb, #8c4ad8);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.yourScores{
  font-size: 2rem;
}
.ranking{
  font-size: 4rem;
}
/* Le même bouton que le home */
.custom-button-scoreboard {
  position: relative;
  padding: 24px 70px;
  background: #a370f0;
  font-size: 40px;
  font-weight: 500;
  color: white;
  border: 3px solid #a370f0;
  border-radius: 8px;
  box-shadow: 0 0 0 #fec1958c;
  transition: all .3s ease-in-out;
  margin-top: 1em ;
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

.custom-button-scoreboard:hover {
  background: transparent;
  color: #a370f0;
  box-shadow: 0 0 25px #fec1958c;
}

.custom-button-scoreboard:hover .star-1 {
  position: absolute;
  top: -80%;
  left: -30%;
  width: 25px;
  height: auto;
  filter: drop-shadow(0 0 10px #fffdef);
  z-index: 2;
}

.custom-button-scoreboard:hover .star-2 {
  position: absolute;
  top: -25%;
  left: 10%;
  width: 15px;
  height: auto;
  filter: drop-shadow(0 0 10px #fffdef);
  z-index: 2;
}

.custom-button-scoreboard:hover .star-3 {
  position: absolute;
  top: 55%;
  left: 25%;
  width: 5px;
  height: auto;
  filter: drop-shadow(0 0 10px #fffdef);
  z-index: 2;
}

.custom-button-scoreboard:hover .star-4 {
  position: absolute;
  top: 30%;
  left: 80%;
  width: 8px;
  height: auto;
  filter: drop-shadow(0 0 10px #fffdef);
  z-index: 2;
}

.custom-button-scoreboard:hover .star-5 {
  position: absolute;
  top: 25%;
  left: 115%;
  width: 15px;
  height: auto;
  filter: drop-shadow(0 0 10px #fffdef);
  z-index: 2;
}

.custom-button-scoreboard:hover .star-6 {
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
</style>

