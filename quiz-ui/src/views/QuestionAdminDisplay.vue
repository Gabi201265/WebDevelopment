<template>
  <div class="adminArea">
    <h1>Administrator Area</h1>
    <div class="inputContainer" :class="{ shake: passwordInvalid && showPopup }">
      <input type="password" placeholder="Enter Password" v-model="password" :style="{ borderColor: passwordInvalid ? 'red' : 'initial' }" />
    </div>
    <button class="buttonConnection" @click="loginAdmin">Log in</button>
    <div v-if="showPopup" :class="{ popupInvalid: passwordInvalid }">
      <p>{{ popupMessage }}</p>
    </div>
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";

export default {
  name: "AdminVue",
  data() {
    return {
      password: "",
      passwordInvalid: false,
      showPopup: false,
      popupMessage: ""
    };
  },

  methods: {
    async loginAdmin() {
      var body = {
        password: this.password
      };
      const loginAPIResult = await quizApiService.loginAdmin(body);
      try {
        if (loginAPIResult.status == 200) {
          window.localStorage.setItem("token", loginAPIResult.data.token);
          this.$router.push("/question-list");
        }
      } catch (error) {
        this.passwordInvalid = true;
        this.showPopup = true;
        this.popupMessage = "Password invalid";
        setTimeout(() => {
          this.showPopup = false;
          this.passwordInvalid = false;
        }, 1000);
      }
    }
  }
};
</script>

<style>
.adminArea {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  padding: 2rem;
  color: #ffffff;
  text-align: center;
}

.inputContainer {
  position: relative;
  width: 300px;
}

input[type="password"] {
  padding: 0.5rem;
  border-radius: 4px;
  border: 1px solid #372883;
  margin-bottom: 1rem;
  width: 100%;
  font-size: 24px;
}

.inputContainer.invalid input[type="password"] {
  border-width: 2px;
  border-color: red;
}

.buttonConnection {
  padding: 0.5rem 1rem;
  border-radius: 4px;
  background-color: #a370f0;
  color: aliceblue;
  border: none;
  cursor: pointer;
  width: 300px;
  font-size: 24px;
  margin-top: 1rem;
}

.popupInvalid {
  position: fixed;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  width: 200px;
  height: 50px;
  background-color: #ff0000;
  color: #ffffff;
  border-radius: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.shake {
  animation: shake 0.5s ease-in-out infinite;
}

.shake .inputContainer {
  animation: shake 0.5s ease-in-out infinite;
}

@keyframes shake {
  0% { transform: translateX(0); }
  25% { transform: translateX(-5px); }
  50% { transform: translateX(5px); }
  75% { transform: translateX(-5px); }
  100% { transform: translateX(0); }
}
</style>
