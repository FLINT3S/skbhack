<template>
  <section class="mt-3">
    <n-h1 class="text-center text-accent">О решении</n-h1>

    <n-card>
      Привет! Мы команда FLINT3S
      <!--      TODO: Описание-->
    </n-card>

    <div class="row mt-4">
      <div class="col-12 col-md-6">
        <n-card>
          <n-h3 class="text-center text-accent">Требования</n-h3>

          <n-list>
            <n-list-item v-for="r in requirements" :key="r.title">
              <n-checkbox :checked="r.completed">{{ r.title }}</n-checkbox>
            </n-list-item>
          </n-list>
        </n-card>
      </div>

      <hr class="d-block d-md-none" />

      <div class="col-12 col-md-6">
        <n-card>
          <n-h3 class="text-center text-accent">Решение</n-h3>
        </n-card>
      </div>
    </div>
  </section>
</template>

<script lang="ts" setup>
import { ref } from "vue";

const requirements = ref([
  { title: "Ролевая модель", completed: true },
  { title: "Регистрация и аторизация пользователя", completed: true },
  {
    title: "Функционал подтверждения регистрации для администратора приложения",
    completed: false,
  },
  { title: "Функционал для блокировки пользователей", completed: false },
  {
    title: "Функционал для пополнения и выведения средств с рублевого счета",
    completed: false,
  },
  {
    title:
      "Функционал открытия нового счета для проведения операций над выбранной пользователем валютой",
    completed: false,
  },
  {
    title:
      "Отображение сводной информации по имеющимся в портфеле пользователя активам. Состав представленной информации должен быть обоснован",
    completed: false,
  },
  {
    title: "Отображение исторический информации должен быть обоснован",
    completed: false,
  },
  {
    title: "Отображение исторической информации о движении валюты ",
    completed: false,
  },
  {
    title:
      "Отображение общей информации о пользователе приложения в удобном и понятном для пользователя виде в т.ч. и информация о реквизитах счетов, с которых совершаются операции над валютами ",
    completed: false,
  },
  {
    title:
      "Функционал торговли, возможность покупать и продавать валюту по рыночному курсу ",
    completed: false,
  },
  {
    title: "Визуализация графика стоимость валюты за период ",
    completed: false,
  },
]);
</script>

<style></style>
