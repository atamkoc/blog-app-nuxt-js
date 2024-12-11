<template>
  <div class="container mx-auto p-4">
    <h1 class="text-3xl font-bold mb-6">Blog Posts</h1>

    <!-- Search Bar -->
    <div class="mb-6">
      <input
        v-model="searchQuery"
        type="text"
        placeholder="Search posts by title or content..."
        class="w-full p-2 border rounded focus:outline-none focus:ring focus:ring-blue-500"
      />
    </div>

    <!-- Spinner -->
    <div v-if="pending">
      <Spinner />
    </div>

    <!-- Error in Data Fetching -->
    <div v-if="error" class="text-center text-red-500">
      <p>{{ error }}</p>
    </div>

    <!-- Posts paginated -->
    <div v-else>
      <div v-if="paginatedFilteredPosts.length > 0" class="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
        <div
          v-for="post in paginatedFilteredPosts"
          :key="post.id"
          class="border rounded-lg p-4 shadow hover:shadow-lg"
        >
          <h2 class="text-xl font-semibold mb-2">{{ post.title }}</h2>
          <p class="text-gray-700 mb-4">{{ post.excerpt }}</p>
          <nuxt-link
            :to="`/posts/${post.id}`"
            class="text-green-500 hover:underline"
          >
            Read More
          </nuxt-link>
        </div>
      </div>

      <!-- No results found -->
      <div v-else class="text-center text-gray-500">
        <p>No posts found matching your search.</p>
      </div>

      <!-- Pagination -->
      <div v-if="paginatedFilteredPosts.length > 0" class="flex justify-between items-center mt-6">
        <!-- Pagination Buttons -->
        <div class="flex space-x-4">
          <button
            :disabled="currentPage === 1"
            @click="changePage(currentPage - 1)"
            class="px-4 py-2 bg-gray-200 rounded hover:bg-gray-300 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            Previous
          </button>
          <button
            :disabled="currentPage === totalPages"
            @click="changePage(currentPage + 1)"
            class="px-4 py-2 bg-gray-200 rounded hover:bg-gray-300 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            Next
          </button>
        </div>

        <!-- Blogs Per Page Dropdown -->
        <div class="flex items-center">
          <label for="postsPerPage" class="mr-2 text-gray-700">
            Blogs per page:
          </label>
          <select
            id="postsPerPage"
            v-model.number="postsPerPage"
            class="p-2 border rounded"
          >
            <option v-for="option in postsPerPageOptions" :key="option" :value="option">
              {{ option }}
            </option>
          </select>
        </div>
      </div>
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
      posts: [], 
      pending: true, 
      error: null, 
      currentPage: 1, 
      postsPerPage: 6, 
      postsPerPageOptions: [6, 9, 12, 15], 
      searchQuery: "", 
    };
  },
  computed: {
    filteredPosts() {
      if (!this.searchQuery.trim()) {
        return this.posts; 
      }
      const query = this.searchQuery.toLowerCase();
      return this.posts.filter(
        (post) =>
          post.title.toLowerCase().includes(query) ||
          post.content.toLowerCase().includes(query)
      );
    },
    paginatedFilteredPosts() {
      const startIndex = (this.currentPage - 1) * this.postsPerPage;
      const endIndex = startIndex + this.postsPerPage;
      return this.filteredPosts.slice(startIndex, endIndex);
    },
    totalPages() {
      return Math.ceil(this.filteredPosts.length / this.postsPerPage);
    },
  },
  methods: {
    // Fetch posts from the API
    async fetchPosts() {
      try {
        const response = await fetch("/posts.json"); 
        if (!response.ok) {
          throw new Error("Failed to fetch posts");
        }
        const data = await response.json();
        this.posts = data;
      } catch (err) {
        this.error = err.message;
      } finally {
        this.pending = false; 
      }
    },
    
    changePage(page) {
      if (page > 0 && page <= this.totalPages) {
        this.currentPage = page;
      }
    },
  },
  watch: {
    postsPerPage() {
      this.currentPage = 1;
    },
    searchQuery() {
      this.currentPage = 1;
    },
  },
  mounted() {
    this.fetchPosts();
  },
};
</script>

<style scoped>
.container {
  max-width: 1200px;
}
</style>
