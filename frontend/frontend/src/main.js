import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import PrimeVue from 'primevue/config';
import InputText from 'primevue/inputtext';
import Button from 'primevue/button';
import Toast from 'primevue/toast';
import ToastService from 'primevue/toastservice'

import 'primevue/resources/themes/lara-light-indigo/theme.css'
import 'primevue/resources/primevue.min.css' 
import 'primeicons/primeicons.css'


const app = createApp(App);
app.use(PrimeVue);
app.component('Button', Button)
app.component('InputText', InputText)
app.component('Toast', Toast)
app.use(createPinia());
app.mount('#app');
