<template>
  <div class="renderPdf flex flex-col w-screen p-14 gap-12">
    <div class="header flex justify-between w-full">
      <div class="firm flex flex-col w-96">
        <p>Prenom Nom</p>
        <p>Raison Sociale</p>
        <p>Adresse code postal</p>
        <p>tel</p>
        <p>em@il</p>
        <p>www.siteweb.com</p>
        <p>SIREN:NoSiren</p>
      </div>
      <div>
        <h2 class="text-6xl px-6 py-4 bg-slate-200 mr-6 uppercase">facture</h2>
      </div>
    </div>
    <div class="client flex justify-between w-full">
      <div class="flex flex-col w-96 bg-slate-200 px-5 py-9">
        <p>N° de facture:</p>
        <p>date</p>
      </div>
      <div class="firm flex flex-col w-96">
        <p>Prenom Nom</p>
        <p>Raison Sociale</p>
        <p>Adresse code postal</p>
      </div>
    </div>
    <div class="container w-full">
      <!-- 1iere ligne -->

      <div class="flex w-full border-b bg-slate-200 mb-3">
        <div class="w-1/6 p-2">Quantité</div>
        <div class="w-3/6 flex-3 p-2">Description</div>
        <div class="w-1/6 p-2">Prix unitaire HT</div>
        <div class="w-1/6 p-2">Prix total HT</div>
      </div>
      <!-- Prestations -->
      <div class="flex w-full border-b border-gray-300">
        <!-- Quantité -->
        <div class="w-1/6 p-2">1</div>
        <!-- Description -->
        <div class="w-3/6 p-2">
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Lorem ipsum
          dolor sit amet consectetur adipisicing elit. Lorem ipsum dolor sit
          amet consectetur adipisicing elit.
        </div>
        <!-- Prix unitaire HT -->
        <div class="w-1/6 p-2">20€</div>
        <!-- Prix total HT -->
        <div class="w-1/6 p-2">20€</div>
      </div>
      <div class="flex w-full border-b border-gray-300">
        <!-- Quantité -->
        <div class="w-1/6 p-2">3</div>
        <!-- Description -->
        <div class="w-3/6 flex-3 p-2">
          Lorem ipsum dolor sit amet consectetur adipisicing elit.
        </div>
        <!-- Prix unitaire HT -->
        <div class="w-1/6 p-2">20€</div>
        <!-- Prix total HT -->
        <div class="w-1/6 p-2">60€</div>
      </div>
    </div>
    <!-- box-total -->
    <div
      class="box-tot w-96 flex flex-col bg-slate-300 mr-6 gap-4 mt-20 ml-auto pl-4 py-10"
    >
      <div class="flex gap-2 w-full">
        <p class="w-2/3">Total HT</p>
        <p class="w-1/3">80€</p>
      </div>
      <div class="flex gap-2 w-full font-bold text-xl">
        <p class="w-2/3">Net à payer</p>
        <p class="w-1/3">80€</p>
      </div>
      <p class="text-xs">TVA non applicable, art. 293 B du CGI</p>
    </div>
  </div>
</template>

<script setup></script>
