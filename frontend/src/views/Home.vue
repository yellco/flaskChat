<template>
  <div class="home">
    <Enter msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// @ is an alias to /src
import Enter from '@/components/Enter.vue'

export default {
  name: 'Home',
  components: {
    Enter
  }
}
</script>
