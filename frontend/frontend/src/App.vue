
<script>
import axios from 'axios';
import {ref, onMounted} from 'vue';
import { useToast } from "primevue/usetoast";
import VesselService from './service/VesselService';

// setting up skeleton functionality
const vessel_dummy = new Array(10)
const vessels = ref();
const vesselService = ref(new VesselService());
const isLoading = ref(true);
const loaded = ref(false);
// loading user data 
const loadUserData = async() => {
          return vesselService.value.getVessels().then((data) => {
              vessels.value = data.data.payload
              isLoading.value = false
              loaded.value = true
            }) 

}



export default {
    setup() {
        onMounted(() => {
              loadUserData();
        })


    const date_builder = function (s) {

        // getting all of the date things :)
        const date = new Date(s)
        const month = date.toLocaleString('default', { month: 'long' });
        const day = date.getDate()
        const year = date.getFullYear()
        const str_time = date.toLocaleString('en-US', {
            hour: 'numeric',
            minute: 'numeric',
            hour12: true
        })

    // building date string from date things and returning date string
    const date_string = `${month} ${day}, ${year}, ${str_time}`
    return date_string
   }

   
        // toast notification variables
        const text = ref();
        const severity = ref();
        const summary = ref(); 
        const toast = useToast();
        const notif = () => {
          toast.add({severity:severity.value, summary:summary.value, detail:text.value });
        }
        
        // variables for handling dialog actions
        const submitted = ref(false);
        const vesselDialog = ref(false);

        

        // vessel variables and default values for creation
        const vessel = ref({});
        const ident = ref();
        ident.value = 0 
        const def_lat = ref();
        const def_long = ref();
        def_lat.value = 0.000000;
        def_long.value = 0.000000;

        // status for create request
        const stat = ref();


        // opens dialog
        const openNew = () => {
            ident.value = 0;
            def_lat.value = 0.000000;
            def_long.value = 0.000000;
            vessel.value = {};
            submitted.value = false;
            vesselDialog.value = true;
        };
        // When cancel, done creating, or error
        const hideDialog = () => {
            vesselDialog.value = false;
            submitted.value = false;
            ident.value = 0;
            def_lat.value = 0.000000;
            def_long.value = 0.000000;
        };
        //create new vessel position 
        const saveVessel = () => {
            let obj = new Object();
            let date_time = document.getElementById('date_time').value;
            obj.vessel_id = ident.value;
            obj.received_time_utc = date_time;
            obj.latitude = def_lat.value;
            obj.longitude = def_long.value;

            // serialize
            let json_vessel = JSON.stringify(obj);


            // attempt creation of new vessel position if successful toaster success else toaster failre with error
            vesselService.value.postVessel(json_vessel).then((response) => {
              stat.value = response.data.status;
              if (stat.value == 200){
                severity.value = "success"
                summary.value = "Success"
                text.value = "Vessel added"
                notif();
                submitted.value = true;
                vesselDialog.value = false;
                ident.value = 0;
                def_lat.value = 0.000000;
                def_long.value = 0.000000;
                console.log("success");
                vesselService.value.getVessels().then(data => vessels.value = data.data.payload);
              }
              else {
                console.log("failed");
              }  
            })
            .catch((error)=> {
 
              severity.value = "error"
              summary.value = "User Error"

              if (typeof error.response.data.errors.geo_coordinate !== "undefined") {
                text.value = error.response.data.errors.geo_coordinate[0]
                notif();
                console.log(error.response.data.errors.geo_coordinate);
              }
              
              if (typeof error.response.data.errors.received_time_utc !== "undefined"){
                text.value = error.response.data.errors.received_time_utc[0]
                notif();
                console.log(error.response.data.errors.received_time_utc );
              }
            })

                                  
          
        };
       


        return {vessels, vessel, vesselDialog, submitted, openNew, def_lat, def_long, ident, hideDialog, saveVessel, loaded, isLoading, vessel_dummy, date_builder}
    },

}
</script>

<template>
  <Toast></Toast>
  <div class="container">
    <div class="tools">
            <Toolbar class="mb-4">
                <template #start>
                    <Button label="New Vessel" icon="pi pi-plus" class="p-button-success mr-2" @click="openNew" />
                </template>

                <template #end>
                    <FileUpload mode="basic" accept="image/*" :maxFileSize="1000000" label="Import" chooseLabel="Import" class="mr-2 inline-block" />
                    <Button label="Export" icon="pi pi-upload" class="p-button-help" @click="exportCSV($event)"  />
                </template>
            </Toolbar>
    </div>
  </div>
  <div v-if="loaded" class="container">
      <div v-if="loaded" class="card">
            <h3 v-if="loaded">Vessel Positions</h3>
            <DataTable  v-if="loaded" :value="vessels" responsiveLayout="scroll" :paginator="true" :rows="10">
                <Column field="vessel_id" header="Vessel ID" :sortable="true"></Column>
                <Column field="received_time_utc" header="Time Received" :sortable="true">
                <template #body="slotProps">
                        {{date_builder(slotProps.data.received_time_utc)}}
                </template>
                </Column>
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
  <div v-if="isLoading" class="container">
    <div  v-if="isLoading" class="card">
    <h3 v-if="isLoading">Vessel Positions</h3>
      <DataTable  v-if="isLoading" :value="vessel_dummy" responsiveLayout="scroll" :paginator="true" :rows="10">
                <Column field="vessel_id" :sortable="true"  header="Vessel ID">
                    <template #body>
                        <Skeleton></Skeleton>
                    </template>
                </Column>
                <Column field="received_time_utc" :sortable="true" header="Time Received">
                    <template #body>
                        <Skeleton></Skeleton>
                    </template>
                </Column>
                <Column field="latitude" :sortable="true" header="Latitude">
                    <template #body>
                        <Skeleton></Skeleton>
                    </template>
                </Column>
                <Column field="longitude" :sortable="true" header="Longitude">
                    <template #body>
                        <Skeleton></Skeleton>
                    </template>
                </Column>
        </DataTable>
    </div>
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


