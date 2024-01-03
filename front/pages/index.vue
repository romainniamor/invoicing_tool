<template>
  <header class="w-full">
    <img class="header-img" src="../assets/images/header.jpg" alt="" />
    <div class="title font-prestage">
      <span>Créez et gérez</span>
      <span>vos factures en</span>
      <span>ligne facilement.</span>
    </div>
  </header>
</template>

<script setup>
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

import { onMounted, ref } from "vue";

gsap.registerPlugin(ScrollTrigger);

onMounted(() => {
  const headerTl = gsap.timeline();

  headerTl
    .to(".header-img", {
      height: "100%",
      filter: "blur(0px)",
      ease: "power3.out",
      duration: 1,
    })
    .to(
      ".title span",
      {
        duration: 2,
        y: 30,
        opacity: 1,
        ease: "power3.out",
        stagger: 0.3,
      },
      "-=.2"
    );
});
</script>

<style scoped>
.header-img {
  height: 20%;
  width: 100%;
  object-fit: cover;
  filter: blur(15px);
  position: absolute;
  top: 0;
  left: 0;
  z-index: -1;
}

header .title {
  display: flex;
  flex-direction: column;
  font-weight: 700;
  font-size: 5em;
  line-height: 1.2em;
  position: absolute;
  top: 30%;
  left: 6%;
}

header .title span {
  opacity: 0;
  letter-spacing: 0.2em;
}
</style>
