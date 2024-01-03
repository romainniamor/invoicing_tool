<template>
  <div>
    <nav
      class="p-4 flex items-center justify-between z-50 top-0 left-0 w-full bg-white"
    >
      <nuxtLink to="/">Logo</nuxtLink>
      <div class="flex items-center space-x-4">
        <template v-if="userStrore.user.isAuthenticated">
          <nuxtLink
            class="py-4 px-6 bg-slate-300 rounded-xl hover:bg-slate-200"
            to="/account/"
            >Mon Compte</nuxtLink
          >
          <button
            v-on:click="logout"
            class="py-4 px-6 bg-slate-300 rounded-xl hover:bg-slate-200"
            to="/"
          >
            Se Deconnecter
          </button>
        </template>
        <template v-else
          ><nuxtLink
            class="py-4 px-6 bg-slate-300 rounded-xl hover:bg-slate-200"
            to="/auth/login"
            >Se Connecter</nuxtLink
          >
          <nuxtLink
            class="py-4 px-6 bg-slate-400 rounded-xl hover:bg-slate-200"
            to="/auth/signup"
            >Créer un Compte
          </nuxtLink>
        </template>
      </div>
    </nav>

    <div id="app-content">
      <slot />
    </div>
  </div>
</template>

<script setup>
import { useUserStore } from "@/stores/user";
import { useRouter } from "vue-router";

const router = useRouter();

const userStrore = useUserStore();

function logout() {
  userStrore.removeToken();
  router.push({ path: "/" });
  console.log("deconnection");
}
</script>

<style></style>
