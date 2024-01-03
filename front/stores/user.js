import { defineStore } from "pinia";

//permet de déterminer si user est authenticated ou non
export const useUserStore = defineStore({
  id: "user",
  state: () => ({
    user: {
      isAuthenticated: false,
      token: null,
      email: null,
    },
    firm: {
      isCreated: false,
      firmInfo: null,
    },
  }),
  actions: {
    initStore() {
      this.user.isAuthenticated = false;
      this.firm.isCreated = false; // Réinitialise isCreated
      if (localStorage.getItem("user.token")) {
        this.user.token = localStorage.getItem("user.token");
        this.user.email = localStorage.getItem("user.email");
        this.user.isAuthenticated = true;
        console.log("user inititialisé:", this.user);
      }
      if (localStorage.getItem("firmInfo")) {
        this.firm.firmInfo = JSON.parse(localStorage.getItem("firmInfo"));
        this.firm.isCreated = true; // Mettre à jour l'état isCreated
      } else {
        this.firm.isCreated = false;
      }
    },

    setToken(token, email) {
      console.log("set-token for:", token, email);
      this.user.token = token;
      this.user.email = token;
      this.user.isAuthenticated = true;

      localStorage.setItem("user.token", token);
      localStorage.setItem("user.email", email);
    },

    removeToken() {
      console.log("remove-token");
      this.user.token = null;
      this.user.email = null;
      this.user.isAuthenticated = false;
      this.firm.isCreated = false;
      this.firm.firmInfo = null;

      localStorage.setItem("user.token", "");
      localStorage.setItem("user.email", "");
    },
    // maj profil user avec les info relative a la firm
    setFirmInfo(firmInfo) {
      this.firm.firmInfo = firmInfo;
      console.log("information de la sociéte dans le store");
      this.firm.isCreated = true; // maj isCreated
      console.log("is created");

      // Sauvegarder firmInfo dans le local storage si nécessaire
      localStorage.setItem("firmInfo", JSON.stringify(firmInfo));
    },
  },
});
