<template>
    <div class="admin">
        <h1>Page administrateur</h1>
        <div v-show="display">
        <p>Saissiez le mot de passe :</p>
        <input type="text" v-model="password" style="color:black"/>
        <button class="OkButton" @click="loginAdmin">Valider le mot de passe</button>
        <p>{{message}}</p>
        </div>
    </div>
</template>
  
<script>
import quizApiService from "@/services/QuizApiService";

export default {
    name: "AdminVue",
    data() {
        return {
            display:true,
            password : "",
            message : ""
        }
    },

    methods:{
        async loginAdmin(){
        var body = {
            "password": this.password
        }
        var loginPromise = quizApiService.loginAdmin(body);
        var loginAPIResult = await loginPromise;
        try{
            if (loginAPIResult.status == 200){
            this.message = "right password";
            console.log(loginAPIResult);
            this.display = !this.display;
            //saving token
            window.localStorage.setItem("token", loginAPIResult.data.token);
            this.$router.push('/question-list');
            }
        }
        catch(error){
            this.message = "mot de passe incorrect";
        }
        },
        async logoutAdmin(){
        },
    }
};
</script>