<template>
  <div class="container mx-auto p-4">
    <div v-if="pending">
      <Spinner />
    </div>

    <div v-if="error" class="text-center text-red-500">
      <p>{{ error }}</p>
    </div>

    <div v-else-if="post">
      <h1 class="text-3xl font-bold mb-4">{{ post.title }}</h1>
      <p class="text-gray-700">{{ post.content }}</p>
      <nuxt-link to="/" class="text-green-500 hover:underline mt-6 block">
        Back to Home
      </nuxt-link>
    </div>
  </div>
</template>

<script>
import Spinner from "@/components/Spinner.vue";

export default {
  components: {
    Spinner,
  },
  data() {
    return {
      post: null,
      pending: true,
      error: null,
    };
  },
  methods: {
    async fetchPost() {
      this.pending = true;
      this.error = null;

      try {
        const response = await fetch("/posts.json");
        if (!response.ok) {
          throw new Error("Failed to fetch posts");
        }

        const posts = await response.json();
        const postId = Number(this.$route.params.id);
        this.post = posts.find((p) => p.id === postId);

        if (!this.post) {
          throw new Error("Post not found");
        }
      } catch (err) {
        this.error = err.message;
      } finally {
        this.pending = false;
      }
    },
  },
  mounted() {
    this.fetchPost();
  },
};
</script>

<style scoped>
.container {
  max-width: 800px;
}
</style>
