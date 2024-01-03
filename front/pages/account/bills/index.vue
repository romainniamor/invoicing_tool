<template>
  <div class="flex flex-col p-32 gap-5">
    <h1 class="text-6xl font-weight-700 mb-8">Mes Factures</h1>
    <div v-if="!bills.length" class="bg-slate-100 rounded-xl relative p-10">
      <p>Vous n'avez pas de facture enregistrée:</p>
      <p>
        Allez dans la rubrique
        <i>'Mes Informations'</i> pour compléter votre profil professionnel.
      </p>
      <p>Puis dans <i>'Nouvelle Facture'</i> pour créer vos factures.</p>
    </div>
    <Bill
      v-for="bill in bills"
      :key="bill.id"
      :bill="bill"
      @toggle-modal="toggleModal"
      @toggle-paid="getPayed"
    />
  </div>

  <div
    :class="{ active: isModalActive }"
    class="modal-container fixed top-0 w-full h-full"
  >
    <div
      @click="toggleModal"
      class="overlay modal-trigger bg-slate-100 w-full absolute h-full"
    ></div>
    <div
      class="modal bg-slate-200 py-10 px-6 rounded-xl flex flex-col justify-center align-center"
    >
      <button
        @click="toggleModal"
        class="close-modal modal-trigger absolute top-2 right-2 py-1 px-3 bg-red-300 text-small text-white rounded-full"
      >
        x
      </button>
      <p class="py-10 text-center">
        Etes vous sur de vouloir supprimer cette facture? Toutes les
        informations seront perdues.
      </p>
      <button @click="deleteBill" class="py-3 bg-green-400 rounded-xl">
        Valider
      </button>
    </div>
  </div>
</template>

<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";
import { useUserStore } from "@/stores/user";
import { useRouter } from "vue-router";

const bills = ref([]);
const userStore = useUserStore();
const router = useRouter();
const firms = ref("");
const billIdToDelete = ref(null);

console.log("Token: ", userStore.user.token);

const isModalActive = ref(false);

function toggleModal(id) {
  billIdToDelete.value = id;
  isModalActive.value = !isModalActive.value;
}

onMounted(() => {
  if (userStore.user.isAuthenticated) {
    console.log("user authentifié");
    getMyBills();
  } else {
    router.push("/");
  }
});

async function getMyFirm() {
  axios
    .get("http://127.0.0.1:8000/api/v1/my-firm/", {
      headers: {
        Authorization: "Token " + userStore.user.token,
        "Content-Type": "application/json",
      },
    })
    .then((response) => {
      firms.value = response.data;
      console.log("firm:", firms.value);
    })
    .catch((error) => {
      console.error("erreur: ", error);
    });
}

async function getMyBills() {
  axios
    .get("http://127.0.0.1:8000/api/v1/my-bills/", {
      headers: {
        Authorization: "Token " + userStore.user.token,
        "Content-Type": "application/json",
      },
    })
    .then((response) => {
      bills.value = response.data;
      console.log("bills user authentifié :", bills.value);
    })
    .catch((error) => {
      console.error("erreur: ", error);
    });
}

async function deleteBill() {
  if (!billIdToDelete.value) {
    console.error("No bill ID to delete");
    return;
  }
  axios
    .delete(`http://127.0.0.1:8000/api/v1/delete/${billIdToDelete.value}/`, {
      headers: {
        Authorization: "Token " + userStore.user.token,
        "Content-Type": "application/json",
      },
    })
    .then((response) => {
      console.log("response:", response);
      console.log("deleting bill");
      // reinitialisation de la valeur
      billIdToDelete.value = null;
      // ferme modal
      toggleModal();
      // maj list
      getMyBills();
    })
    .catch((error) => {
      console.error("erreur: ", error);
    });
}

async function getPayed(id) {
  console.log(`la facture ${id} a été cliquée`);

  // Trouver la facture correspondante dans le tableau des factures
  let bill = bills.value.find((bill) => bill.id === id);
  console.log("bill", bill);

  if (!bill) {
    console.error("Facture non trouvée");
    return;
  }

  const newPayedStatus = !bill.payed;

  try {
    // Mettre à jour la facture sur le serveur
    const response = await axios.put(
      `http://127.0.0.1:8000/api/v1/edit-bill/${id}/`,
      { payed: newPayedStatus }, // Envoyer le nouvel état 'payed'
      {
        headers: {
          Authorization: "Token " + userStore.user.token,
          "Content-Type": "application/json",
        },
      }
    );
    console.log("newPayedStatus", newPayedStatus);
    console.log("Facture mise à jour", response.data);

    // Mettre à jour l'état local
    bill.payed = newPayedStatus;
    getMyBills();
  } catch (error) {
    console.error("Erreur lors de la mise à jour de la facture", error);
  }
}
</script>

<style scoped>
.modal-btn {
  padding: 10px 14px;
  font-size: 18px;
  margin: 100px auto;
  display: block;
  min-width: 130px;
  cursor: pointer;
  background: blue;
}

.modal-container {
  visibility: hidden;
  transition: visibility 0.3s;
}

.modal-container.active {
  visibility: visible;
}

.overlay {
  transition: opacity 0.3s 0.2s ease-out;
}

.modal-container.active .overlay {
  opacity: 0.5;
  transition: opacity 0.3s ease-out;
}

.modal {
  opacity: 0;
  width: 95%;
  max-width: 500px;
  min-width: 300px;
  position: absolute;
  top: 40%;
  left: 50%;
  transform: translate(-50%, calc(-50% - 50px));
  transition: opacity 0.4s ease-out, transform 0.4s ease-out;
}

.modal-container.active .modal {
  opacity: 1;
  transform: translate(-50%, -50%);
  transition: opacity 0.4s 0.2s ease-out, transform 0.4s 0.2s ease-out;
}

.modal-container.active {
  display: block;
  visibility: visible;
}
</style>
