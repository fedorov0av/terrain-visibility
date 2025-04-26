<template>
  <div class="station-form">
    <h2>Настройка станции</h2>
    <form @submit.prevent="submitForm">
      <div>
        <label for="x">X:</label>
        <input
          id="x"
          type="number"
          v-model.number="form.x"
          required
        />
      </div>
      <div>
        <label for="y">Y:</label>
        <input
          id="y"
          type="number"
          v-model.number="form.y"
          required
        />
      </div>
      <div>
        <label for="h">Высота (h):</label>
        <input
          id="h"
          type="number"
          v-model.number="form.h"
          required
        />
      </div>
      <div>
        <label for="r">Радиус (r):</label>
        <input
          id="r"
          type="number"
          v-model.number="form.r"
          required
        />
      </div>
      <button type="submit">Построить зону</button>
    </form>

    <div v-if="geojson">
      <h3>Результат (GeoJSON)</h3>
      <pre>{{ geojson }}</pre>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";

const form = ref({
  x: 47,
  y: 10,
  h: 1,
  r: 4,
});

const geojson = ref(null);

const submitForm = async () => {
  try {
    const params = new URLSearchParams(form.value).toString();
    const response = await fetch(
      `http://localhost:8080/api/visibility?${params}`
    );
    if (!response.ok) throw new Error("Ошибка ответа от сервера");

    const data = await response.json();
    geojson.value = JSON.stringify(data, null, 2);
  } catch (error) {
    console.error("Ошибка при получении зоны видимости:", error);
  }
};
</script>

<style scoped>
.station-form {
  max-width: 500px;
  margin: 2rem auto;
  padding: 3rem;
  border: 5px solid #ccc;
  border-radius: 8px;
}
.station-form div {
  margin-bottom: 1rem;
}
label {
  display: block;
  margin-bottom: 0.25rem;
}
input {
  width: 100%;
  padding: 0.5rem;
}
button {
  padding: 0.5rem 1rem;
  background-color: #3475f4;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
</style>
