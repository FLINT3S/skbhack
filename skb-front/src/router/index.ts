import { createRouter, createWebHashHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import MainLayout from "../layout/MainLayout.vue";

const router = createRouter({
  history: createWebHashHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
      meta: {
        layout: MainLayout,
      },
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
      redirect: "/auth/login",
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
        },
        {
          path: "logout",
          name: "logout",
          component: () => import("../views/Auth/LogoutView.vue"),
        },
      ],
    },
  ],
});

export default router;
