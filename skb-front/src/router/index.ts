import {createRouter, createWebHashHistory} from "vue-router";
import HomeView from "../views/HomeView.vue";
import MainLayout from "../layout/MainLayout.vue";

const router = createRouter({
  history: createWebHashHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/about",
      name: "about",
      component: () => import("../views/AboutView.vue"),
      meta: {
        layout: MainLayout,
      },
    },
    {
      path: "/auth",
      name: "auth",
      component: () => import("../views/AuthView.vue"),
      children: [
        {
          path: "login",
          name: "login",
          component: () => import("../views/Auth/LoginView.vue"),
        },
        {
          path: "register",
          name: "register",
          component: () => import("../views/Auth/RegisterView.vue"),
        }
      ]
    }
  ],
});

export default router;
