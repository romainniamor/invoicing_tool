<template>
  <div class="w-screen flex justify-center">
    <div class="border-2 border-slate-100 rounded-xl relative p-10">
      <button
        @click="downloadPdf"
        class="py-2 px-4 bg-green-400 text-white absolute top-0 right-0 text-xs m-3"
      >
        Télécharger PDF
      </button>
      <div
        id="renderPdf"
        class="flex flex-col p-10 gap-6"
        style="width: 210mm; font-size: 12px"
      >
        <div class="header flex justify-between w-full">
          <div class="firm flex flex-col w-96">
            <p>
              {{ bill?.client?.produced_by?.first_name }}
              {{ bill?.client?.produced_by?.last_name.toUpperCase() }}
            </p>
            <p>{{ bill?.client?.produced_by?.firm_name }}</p>
            <p>{{ bill?.client?.produced_by?.address }}</p>
            <p>
              {{ bill?.client?.produced_by?.postal_code }}
              {{ bill?.client?.produced_by?.city.toUpperCase() }}
            </p>
            <p>{{ bill?.client?.produced_by?.phone }}</p>
            <p>{{ bill?.client?.produced_by?.email }}</p>
            <p>{{ bill?.client?.produced_by?.website }}</p>
            <p>SIRET: {{ bill?.client?.produced_by?.siret }}</p>
          </div>
          <div>
            <h2 class="text-3xl uppercase w-44 text-right">facture</h2>
          </div>
        </div>
        <div class="client flex justify-between w-full">
          <div class="flex px-2 flex-col w-44 bg-slate-200 py-6">
            <p>N° de facture: {{ bill.num_reference }}</p>
            <p>Date: {{ bill.created_at_formated }}</p>
          </div>
          <div class="firm flex flex-col w-56">
            <p>
              {{ bill?.client?.first_name }}
              {{ bill?.client?.last_name.toUpperCase() }}
            </p>
            <p>{{ bill?.client?.address }}</p>
            <p>
              {{ bill?.client?.postal_code }}
              {{ bill?.client?.city.toUpperCase() }}
            </p>
          </div>
        </div>
        <div class="container w-full">
          <!-- 1iere ligne -->

          <div class="flex w-full border-b bg-slate-200 mb-3 align-center">
            <div class="w-1/6 p-2">Quantité</div>
            <div class="w-3/6 flex-3 p-2">Description</div>
            <div class="w-1/6 p-2">Prix unitaire HT</div>
            <div class="w-1/6 p-2">Prix total HT</div>
          </div>
          <!-- Prestations -->
          <div
            v-for="prestation in bill.prestation"
            :key="prestation.id"
            class="flex w-full border-b border-gray-300"
          >
            <!-- Quantité -->
            <div class="w-1/6 p-2">{{ prestation.quantity }}</div>
            <!-- Description -->
            <div class="w-3/6 p-2">
              {{ prestation.description }}
            </div>
            <!-- Prix unitaire HT -->
            <div class="w-1/6 p-2">{{ prestation.price }} €</div>
            <!-- Prix total HT -->
            <div class="w-1/6 p-2">
              {{ formatDecimals(prestation.calculated_total) }} €
            </div>
          </div>
        </div>
        <!-- box-total -->
        <div
          class="box-tot w-96 flex flex-col bg-slate-300 gap-4 mt-20 ml-auto pl-4 py-10"
        >
          <div class="flex gap-2 w-full">
            <p class="w-2/3">Total HT</p>
            <p class="w-1/3">{{ totalPrestations.toFixed(2) }} €</p>
          </div>
          <div class="flex gap-2 w-full font-bold text-xl">
            <p class="w-2/3">Net à payer</p>
            <p class="w-1/3">{{ totalPrestations.toFixed(2) }} €</p>
          </div>
          <p class="text-xs">TVA non applicable, art. 293 B du CGI</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from "axios";
import { ref, onMounted, computed } from "vue";
import { useRoute } from "vue-router";
import { useUserStore } from "@/stores/user";
import { jsPDF } from "jspdf";

const route = useRoute();
const bill = ref([]);
const totalPrestations = ref([]);
const userStore = useUserStore();

console.log(userStore.user.token);

onMounted(async () => {
  try {
    console.log("route id:", route.params.id);
    const response = await axios.get(
      "http://127.0.0.1:8000/api/v1/bill/" + route.params.id + "/",
      {
        headers: {
          Authorization: "Token " + userStore.user.token,
          "Content-Type": "application/json",
        },
      }
    );

    bill.value = response.data;
    console.log("Value:", bill.value.client.first_name);
    console.log("Value:", bill.value.client.produced_by.first_name);
    console.log("Value:", bill.value.prestation);

    totalPrestations.value = bill.value.prestation.reduce(
      (acc, prestation) => acc + prestation.calculated_total,
      0
    );
  } catch (error) {
    console.error("erreur: ", error);
  }
});

function uppercaseName(value) {
  if (value && typeof value === "string") {
    return value.toUpperCase();
  }
  return value;
}

function downloadPdf() {
  // Création d'une nouvelle instance jsPDF
  const doc = new jsPDF();

  // Sélection de l'élément HTML à convertir
  const render = document.getElementById("renderPdf");

  // Utilisation de la méthode 'html' au lieu de 'fromHTML' qui est obsolète
  doc.html(render, {
    callback: function (doc) {
      doc.setFontSize(10);
      const fileName = bill.value.num_reference;

      const pageCount = doc.internal.getNumberOfPages();
      for (let i = 1; i <= pageCount; i++) {
        doc.setPage(i);
        doc.text(fileName + " - " + "Page " + i + "/" + pageCount, 10, 287, {});
      }
      doc.save(`${fileName}.pdf`);
    },

    autoPaging: "text",

    x: 0,
    y: 0,
    width: 210,
    windowWidth: 810,
  });
}
</script>
