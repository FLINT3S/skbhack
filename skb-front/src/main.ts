import {createApp} from "vue";
import {createPinia} from "pinia";

import App from "./App.vue";
import router from "./router";

import "./assets/styles/main.scss";

import {create, NButton, NConfigProvider} from "naive-ui";
import * as Sentry from "@sentry/vue";
import {BrowserTracing} from "@sentry/tracing";

const naive = create({
  components: [NButton, NConfigProvider],
});

const app = createApp(App);

Sentry.init({
  app,
  dsn: "https://39581eb2505b4abca3423dba70d1b159@o4504187440398336.ingest.sentry.io/4504187459600384",
  integrations: [
    new BrowserTracing({
      routingInstrumentation: Sentry.vueRouterInstrumentation(router),
      tracePropagationTargets: ["localhost", "my-site-url.com", /^\//],
    }),
  ],
  tracesSampleRate: 1.0,
});


app.use(createPinia());
app.use(router);
app.use(naive);

app.mount("#app");
