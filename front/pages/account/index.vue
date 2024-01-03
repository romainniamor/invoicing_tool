<template>
  <div class="flex flex-col p-32 gap-14">
    <h1 class="text-6xl weight-700">Mon compte</h1>
    <div class="services flex flex-wrap gap-2">
      <template v-if="!userStore.firm.isCreated"
        ><nuxtLink to="/account/firm/create-firm/"
          ><div class="product">
            <div class="logo">
              <Icon
                class="text-8xl color-white"
                name="tabler:align-box-left-bottom"
                color="white"
              />
            </div>
            <h3>Mes Informations</h3>
            <div class="product-content">
              <p>
                Vous souhaitez créer une ou plusieurs factures? Rentrez vos
                informations d'entreprise.
                <br />Celles-ci seront automatiquement visibles sur vos
                prochaines factures.
              </p>
            </div>
          </div></nuxtLink
        ></template
      >
      <template v-else>
        <nuxtLink to="/account/firm/edit-firm"
          ><div class="product">
            <div class="logo">
              <Icon
                class="text-8xl color-white"
                name="tabler:align-box-left-bottom"
                color="white"
              />
            </div>
            <h3>Mes Informations</h3>
            <div class="product-content">
              <p>
                Vous souhaitez créer une ou plusieurs factures? Rentrez vos
                informations d'entreprise.
                <br />Celles-ci seront automatiquement visibles sur vos
                prochaines factures.
              </p>
            </div>
          </div></nuxtLink
        >
      </template>

      <nuxtLink
        to="/account/new-bill"
        :class="{ unavailable: !userStore.firm.isCreated }"
        ><div class="product">
          <div class="logo">
            <Icon
              class="text-8xl color-white"
              name="mingcute:add-fill"
              color="white"
            />
          </div>
          <h3>Nouvelle Facture</h3>
          <div class="product-content">
            <p>
              Vos informations personnelles sont intégrées au modèle. Vous
              n'avez plus qu'a compléter le document avec vos prestations.
              L'application s'occupe de faire le reste. Votre facture est
              disponible en pdf ainsi que dans votre espace mes factures.
            </p>
          </div>
        </div></nuxtLink
      >
      <nuxtLink to="/account/bills">
        <div class="product">
          <div class="logo">
            <Icon
              class="text-8xl color-white"
              name="ep:document-copy"
              color="white"
            />
          </div>
          <h3>Mes Factures</h3>
          <div class="product-content">
            <p>
              Passez moins de temps à gérer votre facturation pour vous
              concentrer sur l’essentiel ! En plus de pouvoir facturer
              rapidement, vous pouvez facilement suivre et gérer les factures
              crées.
            </p>
          </div>
        </div>
      </nuxtLink>

      <nuxtLink to="/account/help">
        <div class="product">
          <div class="logo">
            <Icon
              class="text-8xl color-white"
              name="fe:question"
              color="white"
            />
          </div>
          <h3>La facturation</h3>
          <div class="product-content">
            <p>
              Un doute? N'hésitez pas à consulter cette rubrique. Vous trouverez
              de nombreuses informations utiles à votre facturation.
            </p>
          </div>
        </div>
      </nuxtLink>
      <nuxtLink to="/">
        <div class="product">
          <div class="logo">
            <Icon
              class="text-8xl color-white"
              name="ep:histogram"
              color="white"
            />
          </div>
          <h3>Dashboard</h3>
          <div class="product-content">
            <p>Retrouvez prochainement une nouvelle fonctionnalité.</p>
          </div>
        </div></nuxtLink
      >
    </div>
  </div>
</template>

<script setup>
import { useUserStore } from "@/stores/user";

const userStore = useUserStore();
console.log("compte cree:", userStore.firm.isCreated);
console.log("compte info:", userStore.firm.firmInfo);
</script>

<style scoped>
.product {
  width: 350px;
  height: 400px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 20px;
  overflow: hidden;
  cursor: pointer;
  border-radius: 15px;
  transition: transform 0.3s ease-in;
}
.product .logo {
  background-color: #b6c1d0;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  margin: auto;
  padding: 15px;
}
.product h3 {
  transition: 0.9s;
  font-size: 2em;
  font-weight: 600;
  text-align: center;
}

.product-content {
  height: 200px;
  text-align: justify;
  position: relative;
}

.product-content::before {
  content: "";
  width: 100%;
  background-color: #b6c1d0;
  height: 2px;
  position: absolute;
  top: -20px;
  left: 0;
}

.product p {
  line-height: 1.6;
  font-size: 14px;
  transition: 0.9s;
  font-weight: 500;
}

.product:hover {
  transform: translateY(-5px);
  box-shadow: 0px 9px 10px 2px #a4a4a4;
}
.product:hover .logo {
  box-shadow: 0 0 0 600px #b6c1d0;
  transition: 1.5s;
}

.product:hover h3,
.product:hover p {
  color: white;
}

.product:hover .product-content::before {
  background: #dedede;
}

.unavailable {
  pointer-events: none;
  opacity: 0.65;
}
.unavailable:hover {
  background: transparent;
}
</style>
