<template>
  <div class="search-container">
    <h2>Buscar no CSV</h2>
    
    <label for="search">Busca:</label>
    <input
      v-model="searchValue"
      type="text"
      id="search"
      placeholder="Digite o valor a buscar"
    />

    <label for="column">Coluna:</label>
    <input
      v-model="searchColumn"
      type="text"
      id="column"
      placeholder="Deixe vazio para buscar em todas as colunas"
    />

    <button @click="performSearch">Buscar</button>

    <div v-if="errorMessage" class="error">
      {{ errorMessage }}
    </div>

    <div v-if="searchExecuted">        
        <div v-if="results.length">
        <h3>Resultados ({{ results.length }})</h3>
        <table>
            <thead>
            <tr>
                <th v-for="(value, key) in results[0]" :key="key">{{ key }}</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="(row, rowIndex) in results" :key="rowIndex">
                <td v-for="(value, key) in row" :key="key">
                {{ value }}
                </td>
            </tr>
            </tbody>
        </table>
        </div>
        <div v-else>
        <p>Nenhum resultado encontrado.</p>
        </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "SearchComponent",
  data() {
    return {
      searchValue: "",
      searchColumn: "",
      results: [],
      errorMessage: "",
      searchExecuted: false,
    };
  },
  methods: {
    async performSearch() {
      this.errorMessage = "";
      this.results = [];
      this.searchExecuted = false;
      try {
        const baseUrl = "http://localhost:8000";
        const response = await axios.get(`${baseUrl}/search`, {
          params: {
            search: this.searchValue,
            column: this.searchColumn,
          },
        });
        console.log(response.data);
        this.results = response.data;
      } catch (error) {
        if (error.response) {
          this.errorMessage = error.response.data.detail || error.response.statusText;
        } else {
          this.errorMessage = error.message;
        }
      } finally {
        this.searchExecuted = true;
      }
    },
  },
};
</script>

<style scoped>
.search-container {
  max-width: 600px;
  margin: 0 auto;
}

.error {
  color: red;
  margin: 1rem 0;
}

table {
  margin-top: 1rem;
  border-collapse: collapse;
  width: 100%;
  border: 1px solid #ccc;
}

th, td {
  border: 1px solid #ccc;
  padding: 0.5rem;
}
</style>
