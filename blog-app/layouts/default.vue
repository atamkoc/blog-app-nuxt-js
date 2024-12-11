<template>
  <div class="flex flex-col min-h-screen">
    <!-- Navigation Bar -->
    <header class="bg-green-600 text-white">
      <nav class="container mx-auto flex items-center justify-between p-4">
        <!-- Logo -->
        <div class="flex items-center">
          <nuxt-link to="/" class="hover:underline"
            ><img
              src="/e-mission-logo.png"
              alt="E-Mission Logo"
              class="h-8 mr-2"
          /></nuxt-link>
        </div>

        <!-- Navigation Links -->
        <ul class="flex space-x-4">
          <li>
            <nuxt-link to="/" class="hover:underline">Home</nuxt-link>
          </li>
          <li>
            <nuxt-link to="/contact" class="hover:underline">Contact</nuxt-link>
          </li>
        </ul>
      </nav>
    </header>

    <!-- Main Content -->
    <main class="flex-grow container mx-auto p-4">
      <slot />
    </main>

    <!-- Footer -->
    <footer class="bg-green-700 text-white text-center py-4">
      All lefts reserved.
      <a href="mailto:ak.tamkoc@tum.de" class="underline">ak.tamkoc@tum.de</a>
    </footer>
  </div>
</template>

<style scoped>
/* Optional: Customize footer or global styles */
</style>
