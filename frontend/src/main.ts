import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import VueSocketio from 'vue-socket.io'

Vue.use(new VueSocketio({
  debug: true,
  connection: 'https://chat.yellco.ru'
}))

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
