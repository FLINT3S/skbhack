<template>
  <section>
    <n-card>
      <div class="text-center">
        Привет! Мы команда FLINT3S, разработавшая это приложение в рамках хакатона "Sovcombank Team Challenge 2022"
        <br>
        <br>
        <div class="fw-bold">
          Подписывайтесь, ставьте лайки - <a href="https://vk.com/ftitdev">vk.com/ftitdev</a>
        </div>
      </div>

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

          <span>В чем крутость нашего решения?</span>

          <ul class="mt-2">
            <li>Микросервисы - (в нашем решении их пока 4, но может стать намного больше :) ) это залог повышения показателей доступности и отказоустойчивости</li>
            <li>CI/CD - непрерывная интеграция и zero-down-time обеспечивают “бесшовное” обновление и ни у кого из пользователей не будет наблюдаться задержек</li>
            <li>За счет технология Docker Swarm обеспечена масштабируемость приложения: можно развернуть сколько угодно инстансов новых микросервисов (на момент предоставления решения это уже успешно хостится на двух нодах)</li>
          </ul>
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
    completed: true,
  },
  { title: "Функционал для блокировки пользователей", completed: true },
  {
    title: "Функционал для пополнения и выведения средств с рублевого счета",
    completed: true,
  },
  {
    title:
      "Функционал открытия нового счета для проведения операций над выбранной пользователем валютой",
    completed: true,
  },
  {
    title:
      "Отображение сводной информации по имеющимся в портфеле пользователя активам. Состав представленной информации должен быть обоснован",
    completed: true,
  },
  {
    title: "Отображение исторический информации должен быть обоснован",
    completed: true,
  },
  {
    title: "Отображение исторической информации о движении валюты ",
    completed: true,
  },
  {
    title:
      "Отображение общей информации о пользователе приложения в удобном и понятном для пользователя виде в т.ч. и информация о реквизитах счетов, с которых совершаются операции над валютами ",
    completed: true,
  },
  {
    title:
      "Функционал торговли, возможность покупать и продавать валюту по рыночному курсу ",
    completed: true,
  },
  {
    title: "Визуализация графика стоимость валюты за период ",
    completed: false,
  },
]);
</script>

<style></style>
