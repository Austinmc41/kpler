import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import PrimeVue from 'primevue/config';
import InputText from 'primevue/inputtext';
import Button from 'primevue/button';
import Toast from 'primevue/toast';
import ToastService from 'primevue/toastservice'
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import ColumnGroup from 'primevue/columngroup';     //optional for column grouping
import Row from 'primevue/row';
import Toolbar from 'primevue/toolbar';
import FileUpload from 'primevue/fileupload';
import Dialog from 'primevue/dialog';
import InputNumber from 'primevue/inputnumber';

import 'primevue/resources/themes/lara-light-indigo/theme.css'
import 'primevue/resources/primevue.min.css' 
import 'primeicons/primeicons.css'


const app = createApp(App);
app.use(PrimeVue);
app.component('Button', Button);
app.component('InputText', InputText);
app.component('Toast', Toast);
app.component('DataTable', DataTable);
app.component('Dialog', Dialog);
app.component('Column', Column);
app.component('ColumnGroup', ColumnGroup);
app.component('FileUpload', FileUpload);
app.component('InputNumber', InputNumber);
app.component('Row', Row);
app.component('Toolbar', Toolbar);
app.use(createPinia());
app.mount('#app');
