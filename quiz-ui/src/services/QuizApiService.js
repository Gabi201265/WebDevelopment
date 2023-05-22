import axios from "axios";

const instance = axios.create({
  baseURL: `${import.meta.env.VITE_API_URL}`,
  json: true
});

export default {
  async call(method, resource, data = null, token = null) {
    var headers = {
      "Content-Type": "application/json",
    };
    if (token != null) {
      headers.authorization = "Bearer " + token;
    }

    return instance({
      method,
      headers: headers,
      url: resource,
      data,
    })
      .then((response) => {
        return { status: response.status, data: response.data };
      })
      .catch((error) => {
        console.error(error);
      });
  },
  getQuizInfo() {
    return this.call("get", "quiz-info");
  },
  getQuestion(position) {
    return this.call("get", `questions?position=${position}`);
  },
  // getQuestionByPosition(position) {
  //   return this.call("get", `questions/position?${position}`);
  // },
  // getQuestionById(index) {
  //   return this.call("get", `questions/${index}`);
  // },
  async postScore(player){
    return this.call("post", "participations", player);
  },
  async loginAdmin(pwd){
    return this.call("post", "login", pwd)
  },
  async deleteParticipation(token){
    return this.call("delete", "participations/all", null, token);
  },
  async deleteAllQuestions(token){
    return this.call("delete", "questions/all", null, token);
  },
  async createQuestion(question, token){
    return this.call("post", "questions", question, token);
  },
  async deleteQuestion(index, token){
    return this.call("delete", `questions/${index}`, null, token);
  },
  async updateQuestion(index, question, token){
    return this.call("put", `questions/${index}`, question, token);
  },
  async getAllParticipations(){
    return this.call("get", "classement");
  }

};