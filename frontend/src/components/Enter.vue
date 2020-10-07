<template>
  <div>
    <div class="container mt-5 mb-4">
        <h1>Chat Room</h1>
    </div>
    <div class="container">
      <ul id="messages"></ul>
        <div class="row">
            <div class="col-7">
              <div class="username">
                <label for="message_input">Username:</label>
                <input type="text" ref="username_input" v-model="username" placeholder="Enter your username">
              </div>
              <div class="message">
                <label for="message_input">Message:</label>
                <input type="text" ref="message_input" placeholder="Enter your message">
                <button @click="sendMessage">Send</button>
              </div>
            </div>
        </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';
import axios, { AxiosResponse } from 'axios'

@Component({sockets:{
      connect(){
        console.log('connect was called');    
      },
      disconnect(){
        console.log('disconnect was called');
      },
      message(data) {
        console.log(data);
        // TODO delete getElementById
        document.getElementById("messages")!.append('<li class="text-muted"><strong>' + data.user + ':</strong>' + data.msg + '</li><br>')
      }
  }})

export default class Enter extends Vue {
  @Prop() private msg!: string;

  private username = null;
  private host = "https://chat.yellco.ru";

  // login() {
  //   const data = new FormData();
  //   data.append('username', (this.$refs.username as HTMLInputElement).value);

  //   axios
  //     .post(this.host + '/chat/login', data)
  //     .then(response => {
  //         response.data === "ok" ? this.username = "" : null;
  //       })    
  // }

  // logout() {
  //   axios
  //     .get(this.host + '/chat/logout')
  //     .then(response => ( response.data === "ok" ? this.username = "" : null))
  //   console.log(this.username);
  // }

  // getUsername() {
  //   axios
  //     .get(this.host + '/chat/username')
  //     .then(response => (this.username = response.data))
  //     .catch(error => console.log(error.response));    
  // }

  sendMessage() {
    this.$socket.emit('chat-message', {
      msg: (this.$refs.message_input as HTMLInputElement).value,
      user: this.username
    });
    (this.$refs.message_input as HTMLInputElement).value = "";
  }

  mounted() {
    // this.getUsername();
  }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
