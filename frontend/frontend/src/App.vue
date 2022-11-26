
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
  <div class="card">
            <h3>Vessel Positions</h3>
            <DataTable :value="products" responsiveLayout="scroll">
                <Column field="Vessel ID" header="Vessel ID" :sortable="true"></Column>
                <Column field="time" header="Time Received" :sortable="true"></Column>
                <Column field="latitude" header="Latitude" :sortable="true"></Column>
                <Column field="longitude" header="Longitude" :sortable="true">
                    <template #body="slotProps">
                        {{formatCurrency(slotProps.data.price)}}
                    </template>
                </Column>
            </DataTable>
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


