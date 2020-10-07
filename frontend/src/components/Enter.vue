<template>
  <div>
    <div class="container">
      <div ref="messages" id="messages">
        <div class="message_block" v-for="(message, i) in messages" :key="message.msg + i">
          <span class="username"><strong>{{message.username}}</strong></span>
          <p class="message">{{message.msg}}</p>
        </div>
      </div>
      <div class="input_block">
        <div class="input">
          <div class="username_input">
            <input type="text" ref="username_input" v-model="username" placeholder="Username...">
          </div>
          <div class="message_input">
            <input type="text" ref="message_input" placeholder="Message...">
          </div>
        </div>
        <div class="button" @click="sendMessage">></div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Enter',
  sockets: {
    connect(){
      console.log('connect was called');    
    },
    disconnect(){
      console.log('disconnect was called');
    },
    message(data) {
      console.log(typeof(data));
      if (typeof(data) === 'object' && 'msg' in data) {
        this.messages.push({
          username: data.user,
          msg: data.msg,
        })
        // this.$refs.messages.append(`<li class="text-muted"><strong>${data.user}:</strong>${data.msg}</li>`)
      }
    }
  },

  data () {
    return {
      username: null,
      host: "https://chat.yellco.ru",
      messages: [],
    }
  },

  methods: {
    sendMessage() {
      if ((this.$refs.message_input.value).length !== 0) {
        this.$socket.emit('chat-message', {
          msg: this.$refs.message_input.value,
          user: this.username
        });
        this.$refs.message_input.value = "";
      }
    },
  },

  computed: {
  },

  mounted () {
    // this.$socket.subscribe("kebab-case", function(data) {
    //     console.log("This event was fired by eg. sio.emit('kebab-case')", data)
    // })
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

#messages{
  padding-top: 10px;
  padding-left: 10px;
  padding-right: 10px;
  height: calc(100vh - 90px - 78px - 30px);
  max-height: calc(100vh - 90px - 78px - 30px);
  overflow-y: auto;
  background: #f5faff;

  .message_block {
    display: block;
    border: 1px solid black;
    width: 60%;
    box-shadow: 0 1px 0 0 rgba(50,50,50,.3);
    border-radius: 4px;
    word-break: break-all;
    margin: 0 5px 5px;
    padding: 1rem;
    text-align: left;
    background: white;

    .message {
      margin: 0;
      padding: 0;
    }
  }
}

.input_block {
  display: flex;
  padding: 10px;

  .input {
    width: 90%;
    input {
      width:100%;
      padding: 10px;
      font-size: 18px;
      outline: none;
      width: calc(100% - 23px);
    }
  }
  .button {
    width:10%;
    cursor: pointer;
    border: 1px solid black;
    display: flex;
    justify-content: center;
    align-items: center;
  }
}
</style>
