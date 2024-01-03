<template>
  <div class="flex flex-col p-32 gap-14">
    <h1 class="text-6xl weight-700">Créer un compte</h1>
    <div
      class="flex flex-col max-w-sm py-10 px-6 bg-slate-100 rounded-xl"
      style="width: 450px"
    >
      <form v-on:submit.prevent="submitForm" class="flex flex-col w-full">
        <input
          v-model="email"
          type="email"
          placeholder="Votre Email..."
          class="w-full mb-4 py-4 px-6 rounded-xl outline-slate-400"
        />
        <input
          v-model="password"
          type="password"
          placeholder="Votre mot de passe..."
          class="w-full mb-4 py-4 px-6 rounded-xl outline-slate-400"
        />
        <input
          v-model="password2"
          type="password"
          placeholder="Confirmer votre mot de passe..."
          class="w-full mb-4 py-4 px-6 rounded-xl outline-slate-400"
        />

        <button class="py-4 px-6 bg-green-400 text-white rounded-xl">
          Valider
        </button>
        <div class="error h-5">
          <div
            v-if="errors.length"
            class="py-4 my-3 text-red-700 flex justify-center"
          >
            <p>{{ errors }}</p>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";

const router = useRouter();

let email = ref("");
let password = ref("");
let password2 = ref("");
let errors = ref("");

async function submitForm() {
  axios
    .post("http://127.0.0.1:8000/api/v1/users/", {
      username: email.value,
      password: password.value,
    })
    .then((response) => {
      console.log("response", response);
      router.push({ path: "/auth/login" });
    })
    .catch((error) => {
      errors.value = "Erreur de saisie. Réessayez.";
    });
}
</script>
