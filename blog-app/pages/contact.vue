<template>
  <div class="container mx-auto p-6 max-w-lg">
    <h1 class="text-3xl font-bold mb-4 text-center">Contact Us</h1>
    <form class="space-y-4">
      <!-- Name Field -->
      <div>
        <label for="name" class="block text-gray-700 font-semibold mb-2">Your Name</label>
        <input
          type="text"
          id="name"
          placeholder="Enter your name"
          class="w-full p-2 border rounded focus:outline-none focus:ring focus:ring-green-500"
        />
      </div>

      <!-- Email Field -->
      <div>
        <label for="email" class="block text-gray-700 font-semibold mb-2">Your Email</label>
        <input
          type="email"
          id="email"
          placeholder="Enter your email"
          class="w-full p-2 border rounded focus:outline-none focus:ring focus:ring-green-500"
        />
      </div>

      <!-- Message Field -->
      <div>
        <label for="message" class="block text-gray-700 font-semibold mb-2">Your Message</label>
        <textarea
          id="message"
          rows="5"
          placeholder="Enter your message"
          class="w-full p-2 border rounded focus:outline-none focus:ring focus:ring-green-500"
        ></textarea>
      </div>

      <!-- Submit Button -->
      <div class="text-center">
        <button
          type="button"
          class="px-6 py-2 bg-green-600 text-white font-semibold rounded hover:bg-green-700"
        >
          Submit
        </button>
      </div>
    </form>
  </div>
</template>

<style scoped>
.container {
  max-width: 500px;
}
</style>

