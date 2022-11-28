
<script>
import axios from 'axios'
import {ref, onMounted} from 'vue';
import VesselService from './service/VesselService'
const text = ref();


export default {
    setup() {
        onMounted(() => {
            vesselService.value.getVessels().then(data => vessels.value = data.data.payload);
        })
        
        const vessel = ref({});
        const submitted = ref(false);
        const vesselDialog = ref(false);
        const vessels = ref();
        const vesselService = ref(new VesselService());
        const ident = ref();
        ident.value = 0 
        const def_lat = ref();
        const def_long = ref();
        def_lat.value = 0.000000
        def_long.value = 0.000000

         const openNew = () => {
            vessel.value = {};
            submitted.value = false;
            vesselDialog.value = true;
        };

        return {vessels, vessel, vesselDialog, submitted, openNew, def_lat, def_long, ident}
    },

}
</script>

<template>
  <div class="container">
    <div class="tools">
            <Toolbar class="mb-4">
                <template #start>
                    <Button label="New" icon="pi pi-plus" class="p-button-success mr-2" @click="openNew" />
                    <Button label="Delete" icon="pi pi-trash" class="p-button-danger" @click="confirmDeleteSelected" :disabled="!selectedProducts || !selectedProducts.length" />
                </template>

                <template #end>
                    <FileUpload mode="basic" accept="image/*" :maxFileSize="1000000" label="Import" chooseLabel="Import" class="mr-2 inline-block" />
                    <Button label="Export" icon="pi pi-upload" class="p-button-help" @click="exportCSV($event)"  />
                </template>
            </Toolbar>
  </div>
  </div>
  <div class="container">
      <div class="card">
            <h3>Vessel Positions</h3>
            <DataTable :value="vessels" responsiveLayout="scroll">
                <Column field="vessel_id" header="Vessel ID" :sortable="true"></Column>
                <Column field="received_time_utc" header="Time Received" :sortable="true"></Column>
                <Column field="latitude" header="Latitude" :sortable="true"></Column>
                <Column field="longitude" header="Longitude" :sortable="true"></Column>
            </DataTable>
        </div>

    <Dialog v-model:visible="vesselDialog" :style="{width: '450px'}" header="Vessel Details" :modal="true" class="p-fluid">
            <div class="formgrid grid">
            <div class="field col">
                    <label>Vessel ID</label>
                    <InputNumber v-model="ident" id="vessel_ident"/>
                </div>
                  <div class="field col date">
                    <label>Date and Time</label>
                    <input type="datetime-local" id='date_time' name="datetime">
                </div>
                <div class="field col">
                    <label>Latitude</label>
                    <InputNumber v-model="def_lat" mode="decimal" id="latitude" :minFractionDigits="2" :maxFractionDigits="6" :min="-90" :max="90"/>
                </div>
                <div class="field col">
                    <label>Longitude</label>
                    <InputNumber v-model="def_long" mode="decimal" id="longitude" :minFractionDigits="2" :maxFractionDigits="6" :min="-180" :max="180"/>
                </div>
            </div>
            <template #footer>
                <Button label="Cancel" icon="pi pi-times" class="p-button-text" @click="hideDialog"/>
                <Button label="Save" icon="pi pi-check" class="p-button-text" @click="saveVessel" />
            </template>
        </Dialog>
  </div>
</template>

<style scoped>
.container {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 20vh;
}

.card{
  width: 75vw;
}

.tools {
  width:75vw;
}

.col {
  margin-top:25px
}

.date {
display:flex;
flex-direction: column;
}
</style>


