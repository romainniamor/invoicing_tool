<template>
  <div class="flex flex-col p-32 gap-5 w-4/6">
    <h1 class="text-6xl weight-700 mb-8">Nouvelle Facture</h1>

    <form
      @submit.prevent="submitForm"
      class="w-full flex flex-col p-6 bg-slate-100 rounded-xl relative"
    >
      <h3 class="py-3 text-xl">Client:</h3>
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
          required
          maxlength="30"
          placeholder="Nom"
          class="w-full mb-4 py-4 px-6 rounded-xl outline-slate-400"
        />
      </div>

      <div class="flex gap-2">
        <input
          v-model="address"
          required
          type="text"
          maxlength="50"
          placeholder="Adresse"
          class="w-2/3 mb-4 py-4 px-6 rounded-xl outline-slate-400"
        />
        <input
          v-model="postal_code"
          required
          type="text"
          maxlength="5"
          placeholder="Code Postal"
          class="w-1/3 mb-4 py-4 px-6 rounded-xl outline-slate-400"
        />
        <input
          v-model="city"
          required
          type="text"
          maxlength="30"
          placeholder="Ville"
          class="w-1/3 mb-4 py-4 px-6 rounded-xl outline-slate-400"
        />
      </div>
      <h3 class="text-xl py-3">Prestations:</h3>
      <div class="flex flex-col gap-3 pb-16">
        <!-- barre de prestations -->
        <div
          v-for="(prestation, index) in prestations"
          :key="index"
          class="w-full flex items-center gap-5 relative"
        >
          <input
            v-model="prestation.description"
            type="text"
            maxlength="30"
            required
            placeholder="Prestation"
            class="w-2/5 py-4 px-6 rounded-xl outline-slate-400"
          />

          <input
            v-model="prestation.quantity"
            type="number"
            required
            min="0"
            placeholder="Quantité"
            class="w-1/5 py-4 px-6 rounded-xl outline-slate-400"
          />

          <input
            v-model="prestation.price"
            type="text"
            required
            min="0"
            placeholder="Prix UHT"
            class="w-1/5 py-4 px-6 rounded-xl outline-slate-400"
          />

          <button
            type="button"
            @click="removePrestation(index)"
            class="py-1 px-3 bg-red-300 text-s text-white rounded-full absolute right-5 top-1/2 transform -translate-y-1/2"
          >
            x
          </button>
        </div>

        <!-- fin des presta -->
      </div>
      <button
        type="button"
        @click="addPrestation"
        class="text-5xl text-slate-400 font-bold px-2 w-full"
      >
        +
      </button>
      <button class="py-4 px-6 w-full bg-green-400 text-white rounded-xl">
        Valider
      </button>
    </form>

    <p>{{ errors }}</p>
  </div>
</template>

<script setup>
import axios from "axios";
import { ref, onMounted, reactive } from "vue";
import { useUserStore } from "@/stores/user";
import { useRouter } from "vue-router";

const userStore = useUserStore();
const router = useRouter();

console.log("l user a un compte?:", userStore.firm.isCreated);
console.log("firmInfo:", userStore.firm.firmInfo);

onMounted(() => {
  userStore.initStore();

  if (!userStore.user.isAuthenticated) {
    router.push({ path: "/login" });
    return;
  }

  if (!userStore.firm.isCreated) {
    router.push({ path: "/account/" });
    return;
  }
});

let errors = ref("");
let first_name = ref("");
let last_name = ref("");
let address = ref("");
let postal_code = ref("");
let city = ref("");
let prestations = ref([
  {
    description: "",
    quantity: "",
    price: "",
  },
]);

function addPrestation() {
  console.log("click du bouton presta");

  const lastPrestation = prestations.value[prestations.value.length - 1];

  if (
    lastPrestation.description &&
    lastPrestation.quantity &&
    lastPrestation.price
  ) {
    prestations.value.push({ description: "", quantity: "", price: "" });
  } else {
    return;
  }
}

function removePrestation(index) {
  console.log("click de remove");
  //condition de suppression pour ne pas enlever toutes les presta (il doit en rester une)
  if (prestations.value.length > 1 && index !== 0) {
    prestations.value.splice(index, 1);
  } else {
    return;
  }
}

async function submitForm() {
  try {
    const payload = {
      first_name: first_name.value,
      last_name: last_name.value,
      address: address.value,
      postal_code: postal_code.value,
      city: city.value,
    };

    for (let i = 0; i < prestations.value.length; i++) {
      const presta = prestations.value[i];
      payload[`presta-${i}-description`] = presta.description;
      payload[`presta-${i}-quantity`] = presta.quantity;
      payload[`presta-${i}-price`] = presta.price;
    }

    payload["presta-TOTAL_FORMS"] = prestations.value.length;
    payload["presta-INITIAL_FORMS"] = 0;
    payload["presta-MIN_NUM_FORMS"] = 0;
    payload["presta-MAX_NUM_FORMS"] = 1000; // Ou un autre nombre max acceptable

    const createBill = await axios.post(
      "http://127.0.0.1:8000/api/v1/create-bill/",
      payload,
      {
        headers: {
          Authorization: "Token " + userStore.user.token,
          "Content-Type": "application/json",
        },
      }
    );
    router.push({ path: "/account/bills/" });
  } catch (error) {
    errors.value = "Erreur de saisie. Veuillez réessayer.";
  }
}
</script>
