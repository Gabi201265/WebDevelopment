import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import NewQuizPage from '../views/NewQuizPage.vue'
import QuestionsManager from '../views/QuestionsManager.vue'
import QuestionAdminDisplay from '../views/QuestionAdminDisplay.vue'
import ScoreBoard from '../views/ScoreBoard.vue'
import QuestionsList from '../views/QuestionsList.vue'
import QuestionCreation from '../views/QuestionCreation.vue'
import QuestionEdition from '../views/QuestionEdition.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'HomePage',
      component: HomePage
    },
    {
      path: '/start-new-quiz-page',
      name: 'NewQuizPage',
      component: NewQuizPage
    },
    {
      path: '/questions',
      name: 'Questions',
      component: QuestionsManager
    },
    {
      path: '/admin',
      name: 'Admin',
      component: QuestionAdminDisplay
    },
    {
      path: '/scoreboard/:score',
      name: 'ScoreBoard',
      component: ScoreBoard
    },
    {
      path: '/question-list',
      name: 'QuestionsList',
      component: QuestionsList
    },
    {
      path: '/question-creation',
      name: 'QuestionCreation',
      component: QuestionCreation
    },
    {
      path: '/question-edit/:myEditedQuestion',
      name: 'QuestionEdition',
      component: QuestionEdition,
      props: true
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    }
  ]
})

export default router
