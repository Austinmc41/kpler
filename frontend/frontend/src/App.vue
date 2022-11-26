
<template>
<h1>My name is Austin how are you</h1>
</template>


<script>
import axios from 'axios'

export default {
  mounted() {
    axios.get('http://0.0.0.0:8000/api/vessels/').
    then((response) => {
      console.log(response.data.payload)
    })
  }
}
</script>

