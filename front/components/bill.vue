<template>
  <div
    class="w-full flex items-center relative p-5 bg-slate-100 rounded-xl hover:bg-slate-200"
  >
    <div class="flex w-1/5">
      <p class="py-3 text-xl">{{ bill.num_reference }}</p>
    </div>
    <div class="flex w-1/5">
      <p class="py-3 text-xl">{{ bill.created_at_formated }}</p>
    </div>
    <div class="flex w-1/5">
      <p class="py-3 text-xl">
        {{ bill.client.first_name }} {{ bill.client.last_name.toUpperCase() }}
      </p>
    </div>
    <div class="flex w-1/5">
      <p class="py-3 text-xl">{{ calculateTotalBill(bill.prestation) }}€</p>
    </div>
    <div class="absolute flex gap-3 right-5 top-1/2 transform -translate-y-1/2">
      <nuxtLink :to="`/account/bills/${bill.id}`"
        ><button class="py-3 px-5 bg-green-400 rounded-xl">
          Details
        </button></nuxtLink
      >
      <button
        @click="$emit('toggle-paid', bill.id)"
        v-if="bill.payed"
        class="py-3 w-24 bg-green-400 rounded-xl"
      >
        Payée
      </button>

      <button
        @click="$emit('toggle-paid', bill.id)"
        v-else
        class="py-3 w-24 bg-slate-400 rounded-xl"
      >
        Impayée
      </button>
      <button
        @click="$emit('toggle-modal', bill.id)"
        class="py-3 px-5 bg-red-300 text-white rounded-full"
      >
        x
      </button>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from "vue-router";

const props = defineProps({
  bill: {
    type: [Object],
  },
});

const calculateTotalBill = (prestations) => {
  return prestations.reduce(
    (acc, prestation) => acc + prestation.calculated_total,
    0
  );
};
</script>
