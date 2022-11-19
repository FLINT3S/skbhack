<template>
  <main class="authentication-view">
    <div class="container d-flex justify-content-center">
      <transition name="slide-down" appear mode="in-out">
        <n-card class="auth-card" size="large">
          <div class="auth-card__inner">
            <img src="../assets/img/skb-logo.png" alt="" class="auth-logo" />

            <router-view v-slot="{ Component }">
              <transition name="fade" mode="out-in">
                <component :is="Component" />
              </transition>
            </router-view>
          </div>
        </n-card>
      </transition>
    </div>
  </main>
</template>

<script setup lang="ts"></script>

<style scoped lang="scss">
.authentication-view {
  background: url("@/assets/img/login/login-bg.png") no-repeat center center;
  background-size: cover;
  height: 100vh;
  width: 100vw;
  display: flex;
  justify-content: center;
  align-items: center;
}

.auth-card {
  width: 500px;
  padding-top: 60px;
  padding-bottom: 40px;

  @media screen and (max-width: 576px) {
    width: 100%;
  }
}

.auth-card__inner {
  display: flex;
  flex-direction: column;
  text-align: center;
}

.auth-logo {
  width: 270px;
  margin-left: auto;
  margin-right: auto;

  @media screen and (max-width: 576px) {
    width: 100%;
  }
}
</style>

<style lang="scss">
.auth-screen-header {
  font-size: 24px;
  font-weight: 500;
  line-height: 1.2;
  margin-top: 24px;
  margin-bottom: 20px;
  display: block;
  text-align: center;
  color: var(--accent-blue);
}
</style>
