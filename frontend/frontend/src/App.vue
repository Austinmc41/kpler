
<script>
import axios from 'axios'
import {ref} from 'vue';

const text = ref();

// export default {
//   mounted() {
//     axios.get('http://0.0.0.0:8000/api/vessels/').
//     then((response) => {
//       console.log(response.data.payload)
//     })
//   }
// }
</script>

<template>
  <div class="container">
    <span class="p-float-label">
      <InputText id="id" type="text" v-model="value" />
      <label for="id">Vessel ID</label>
    </span>
    <span class="p-float-label">
      <InputText id="time" type="text" v-model="value" />
      <label for="time">Time Received</label>
    </span>
    <span class="p-float-label">
      <InputText id="latitude" type="text" v-model="value" />
      <label for="latitude">Latitude</label>
    </span>
    <span class="p-float-label">
      <InputText id="longitude" type="text" v-model="value" />
      <label for="longitude">Longitude</label>
    </span>
    <Button label="Add Vessel" @click="create"></Button>
  </div>
</template>

<style scoped>
.container {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 20vh;
}
</style>


