<template>
    <div class="createQuestion">
      <h1>Create question</h1>
      <div >
        <p>Position</p>
        <input type="text" v-model="position" />

        <p>Title</p>
        <input type="text" v-model="title" required />
        
        <p>Text</p>
        <input type="text" v-model="text" required />
        
        <p>Image</p>
        <ImageUpload @file-change="imageFileChangedHandler"/>
        
        <p>Answers (check the right answer)</p>
        <div>
          <input type="text" v-model="possibleAnswer[0]" placeholder="Réponse 1" />
          <input type="radio" value="0" name="reponse" Checked/>
        </div>
        <div>
          <input type="text" v-model="possibleAnswer[1]" placeholder="Réponse 2" />
          <input type="radio" value="1" name="reponse"/>
        </div>
        <div>
          <input  type="text" v-model="possibleAnswer[2]" placeholder="Réponse 3" />
          <input type="radio" value="2"  name="reponse"/>
        </div>
        <div>
          <input  type="text" v-model="possibleAnswer[3]" placeholder="Réponse 4" />
          <input type="radio" value="3" name="reponse"/>
        </div>
    
      </div>
      <button @click="backToQuestionList" class="glow-on-hover">Back to question list</button>
      <button @click="createQuestion" class="glow-on-hover">Create</button>
    </div>
    </template>
    
<script>
import quizApiService from "@/services/QuizApiService";
import ImageUpload from "@/views/ImageUpload.vue";
export default {
  name: "QuestionCreation",
  data() {
    return {
      position:"",
      title:"",
      text:"",
      image:"",
      possibleAnswer : [],
      selectedAnswer : 0,
      totalNumberOfQuestion : 0
    }
  },
  components:{
    ImageUpload
  },
  async created() {
    const quizInfoAPIResult = await quizApiService.getQuizInfo();
    var quizInfo = quizInfoAPIResult.data.size;
    this.totalNumberOfQuestion= quizInfo;
  },
  methods:{
    imageFileChangedHandler(b64String) {
      this.image = b64String;
    },
    async createQuestion(){
      var reponse = document.querySelector('input[name="reponse"]:checked').value;
      console.log(reponse);
      var possibleAnswers = [];
      for (var i = 0; i < 4; i++){
        var isCorrect = true;
        if (i != parseInt(reponse))
            isCorrect = false;
        else
          isCorrect = true;
        var object = {
          "text" : this.possibleAnswer[i],
          "isCorrect" : isCorrect
        }
        possibleAnswers.push(object);
      }

      // La position, insertion ou ajout !
      this.position = parseInt(this.position, 10);
      if (!this.position || isNaN(this.position)) {
        this.position = this.totalNumberOfQuestion + 1;
        console.log("Good !");
      }
      var question = {
        "position": this.position,
        "title": this.title,
        "text": this.text,
        "image": this.image,
        "possibleAnswers": possibleAnswers
      }
      console.log(question);
      const token = window.localStorage.getItem("token");
      const quizInfoAPIResult = await quizApiService.createQuestion(question, token);
      console.log(quizInfoAPIResult);
      this.$router.push('/question-list');
    },
    backToQuestionList(){
      this.$router.push('/question-list');
    }
  }
}; 
</script>
<style>
.createQuestion{
  color: white;
  flex-direction: column;
  padding: 2rem;
  margin-top: 5rem;
  color: #FFFFFF;
}
</style>
 