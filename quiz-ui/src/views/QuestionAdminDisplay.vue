<template>
    <div class="admin">
        <h1>Page administrateur</h1>
          <input type="text" placeholder="Password" v-model="password" style="color:black"/>
          <button @click="loginAdmin">Connexion</button>
          <p>{{message}}</p>
    </div>
</template>
  
<script>
import quizApiService from "@/services/QuizApiService";

export default {
  name: "AdminVue",
  data() {
    return {
      password : "",
      message : ""
    }
  },

  methods: {
    async loginAdmin(){
      var body = {
        "password": this.password
      }
      const loginAPIResult = await quizApiService.loginAdmin(body);
      try{
        if (loginAPIResult.status == 200){
          this.message = "password valid";
          //saving token
          window.localStorage.setItem("token", loginAPIResult.data.token);
          this.$router.push('/question-list');
        }
      }
      catch(error){
        this.message = "password invalid";
      }
    }
  }
};
</script>