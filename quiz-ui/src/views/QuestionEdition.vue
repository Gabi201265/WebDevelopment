<template>
  <div class="QuestionEdition">
    <div v-if=this.question>
      <h1>Delete question {{ this.question.position }} : </h1>
      <button @click="deleteQuestion()">Delete</button>
      <h1>Edit question {{ this.question.position }} : </h1>
      <div>
        <p>Position</p>
        <input type="text" v-model="position" />
        <p>Title</p>
        <input type="text" v-model="title" />
        <br> <br>
        <p>Text</p>
        <input type="text" v-model="text" />
        <br> <br>
        <p>Image</p>
        <button @click="changeImageQuestion()">Change question's picture</button>
        <div v-show="display">
          <ImageUpload @file-change="imageFileChangedHandler" v-model="image"/>
        </div>
        
        <p>Answers (check the right answer)</p>
        <div>
          <div v-for="(answer, index) in possibleAnswers" :key="index">
            <input type="radio" :value="index" v-model="correctAnswerIndex" @change="updatePossibleAnswers()">
            <input type="text" v-model="answer.text" :placeholder="answer.text" @change="updatePossibleAnswers()">
          </div>
        </div>
      </div>
    </div>
    <button @click="backToQuestionList" class="glow-on-hover">Back to question list</button>
    <button v-bind:disabled="correctAnswerIndex === null" @click="editQuestion" class="glow-on-hover">Edit</button>
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";
import ImageUpload from "@/views/ImageUpload.vue";

export default {
  name: "QuestionEdition",
  props: {
    question: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      display: false,
      question: null,
      title:"",
      text:"",
      image:"",
      possibleAnswer : [],
      position: 0,
      correctAnswerIndex: null
    };
  },
  components:{
    ImageUpload
  },
  async created(){
    this.question = this.$route.params.myEditedQuestion;
    if(this.question){
      this.question = JSON.parse(this.question);
      this.id = this.question.id;
      this.title = this.question.title;
      this.text = this.question.text;
      this.image = this.question.image;
      this.possibleAnswers = this.question.possibleAnswers;
      this.position = this.question.position;
      this.correctAnswerIndex = this.possibleAnswers.findIndex(answer => answer.isCorrect);
    }
  },
  methods: {
    async deleteQuestion(){
      try{
        const token = window.localStorage.getItem("token");
        console.log(token);
        const questionDeleteAPIResult = await quizApiService.deleteQuestion(this.question.id, token);
        this.$router.push('/question-list');
      }
      catch(error){
        console.log(error);
      }
    },
    changeImageQuestion(){
      this.display = !this.display;
    },
    imageFileChangedHandler(b64String) {
      this.image = b64String;
    },
    updatePossibleAnswers() {
      this.possibleAnswers.forEach((answer, index) => {
        answer.isCorrect = (index === this.correctAnswerIndex);
        answer.text = this.possibleAnswers[index].text;
      });
    },
    async editQuestion(){
      this.position = parseInt(this.position, 10);
      var question = {
        "position": this.position,
        "title": this.title,
        "text": this.text,
        "image": this.image,
        "possibleAnswers": this.possibleAnswers
      }
      console.log(question);
      const token = window.localStorage.getItem("token");
      const quizInfoAPIResult = await quizApiService.updateQuestion(this.id, question, token);
      this.$router.push('/question-list');
    },
    backToQuestionList(){
      this.$router.push('/question-list');
    }
  }
};
</script>

<style>
.QuestionEdition{
  color: white;
  flex-direction: column;
  padding: 2rem;
  margin-top: 5rem;
  color: #FFFFFF;
}
</style>