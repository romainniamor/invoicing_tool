<template>
  <div class="flex flex-col p-32 gap-14 w-4/6">
    <h1 class="text-6xl weight-700">Création Société</h1>

    <form v-on:submit.prevent="submitForm" class="flex flex-wrap w-full gap-12">
      <div class="flex flex-col p-6 bg-slate-100 rounded-xl">
        <h3 class="py-3 text-xl">Informations Générales:</h3>

        <div class="flex gap-2">
          <input
            v-model="first_name"
            type="text"
            maxlength="30"
            placeholder="Prénom"
            class="w-full mb-4 py-4 px-6 rounded-xl outline-slate-400"
          />
          <input
            v-model="last_name"
            type="text"
            maxlength="30"
            placeholder="Nom"
            class="w-full mb-4 py-4 px-6 rounded-xl outline-slate-400"
          />
        </div>
        <input
          v-model="firm_name"
          type="text"
          maxlength="30"
          placeholder="Raison Sociale"
          class="w-1-3 mb-4 py-4 px-6 rounded-xl outline-slate-400"
        />
        <div class="flex gap-2">
          <input
            v-model="address"
            type="text"
            maxlength="50"
            placeholder="Adresse"
            class="w-2/3 mb-4 py-4 px-6 rounded-xl outline-slate-400"
          />
          <input
            v-model="postal_code"
            type="text"
            maxlength="5"
            placeholder="Code Postal"
            class="w-1/4 mb-4 py-4 px-6 rounded-xl outline-slate-400"
          />
          <input
            v-model="city"
            type="text"
            maxlength="30"
            placeholder="Ville"
            class="w-1/3 mb-4 py-4 px-6 rounded-xl outline-slate-400"
          />
        </div>
        <div class="flex gap-2">
          <input
            v-model="email"
            type="email"
            maxlength="30"
            placeholder="Email"
            class="w-full mb-4 py-4 px-6 rounded-xl outline-slate-400"
          />
          <input
            v-model="phone"
            type="text"
            maxlength="10"
            placeholder="Téléphone"
            class="w-full mb-4 py-4 px-6 rounded-xl outline-slate-400"
          />
        </div>
        <input
          v-model="website"
          type="text"
          maxlength="30"
          placeholder="Site Web"
          class="w-full mb-4 py-4 px-6 rounded-xl outline-slate-400"
        />
        <input
          v-model="siret"
          required
          type="text"
          maxlength="14"
          placeholder="SIRET"
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
      </div>
    </form>
  </div>
</template>

<script setup>
import axios from "axios";
import { ref } from "vue";
import { useUserStore } from "@/stores/user";
import { useRouter } from "vue-router";

const userStore = useUserStore();
const router = useRouter();

console.log("l user a un compte?:", userStore.firm.isCreated);
console.log("firmInfo:", userStore.firm.firmInfo);

// variable de firmForm, utilisation

let first_name = ref("");
let last_name = ref("");
let firm_name = ref("");
let address = ref("");
let postal_code = ref("");
let city = ref("");
let phone = ref("");
let email = ref("");
let website = ref("");
let siret = ref("");
let errors = ref("");

async function submitForm() {
  console.log("submitting");
  axios
    .post(
      "http://127.0.0.1:8000/api/v1/create-firm/",
      {
        first_name: first_name.value,
        last_name: last_name.value,
        firm_name: firm_name.value,
        address: address.value,
        postal_code: postal_code.value,
        city: city.value,
        phone: phone.value,
        website: website.value,
        email: email.value,
        siret: siret.value,
      },
      {
        headers: {
          Authorization: "Token " + userStore.user.token,
          "Content-Type": "application/json",
        },
      }
    )
    .then((response) => {
      console.log("response", response);
      const firm_info = {
        first_name: first_name.value,
        last_name: last_name.value,
        firm_name: firm_name.value,
        address: address.value,
        postal_code: postal_code.value,
        city: city.value,
        phone: phone.value,
        email: email.value,
        website: website.value,
        siret: siret.value,
      };
      userStore.setFirmInfo(firm_info); //appel de setFirmInfo du store
      router.push({ path: "/account" });
      console.log("l user a un compte?:", userStore.firm.isCreated);
      console.log("la firm id:", userStore.firm.id);
    })
    .catch((error) => {
      errors.value = "Erreur de saisie. Réessayez.";
    });
}
</script>
