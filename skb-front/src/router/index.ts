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
        {
          path: "verify",
          name: "verify",
          component: () => import("../views/Auth/VerifyView.vue"),
        },
        {
          path: "block",
          name: "block",
          component: () => import("../views/Auth/BlockView.vue"),
        }
      ],
    },
    {
      path: "/admin",
      name: "admin",
      component: () => import("../views/AdminPanelView.vue"),
      meta: {
        layout: MainLayout,
      }
    },
    {
      path: "/profile",
      name: "profile",
      component: () => import("../views/ProfileView.vue"),
      meta: {
        layout: MainLayout,
      }
    },
    {
      path: "/account/:id",
      name: "account",
      component: () => import("../views/AccountView.vue"),
      meta: {
        layout: MainLayout,
      }
    },
    {
      path: "/converter",
      name: "converter",
      component: () => import("../views/ConverterView.vue"),
      meta: {
        layout: MainLayout
      }
    },
    {
      path: "/currencyHistory",
      name: "currencyHistory",
      component: () => import("../views/HistoryView.vue"),
      meta: {
        layout: MainLayout
      }
    }
  ],
});

export default router;
