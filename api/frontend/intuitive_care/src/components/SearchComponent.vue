<template>
  <div class="search-container">
    <h2>Buscar no CSV</h2>
    
    <div class="inputs-row">
        <div class="input-group">
            <label for="search" class="label">Buscar:</label>
            <input
            v-model="searchValue"
            type="text"
            id="search"
            class="input"
            placeholder="Digite o que deseja buscar"
            />
        </div>

        <div class="input-group">
            <label for="column" class="label">Coluna:</label>
            <input
            v-model="searchColumn"
            type="text"
            id="column"
            class="input"
            placeholder="Deixe vazio para buscar em todas as colunas"
            />
        </div>
          <button class="button-search" @click="performSearch">Buscar</button>
    </div>

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
.button-search {
  padding: 0.5rem 1rem;
  background-color: #c8a4f4;
  color: black;
  border: 2px solid black;
}
.inputs-row {
  display: flex;        
  gap: 1rem;             
  align-items: center;   
  margin-bottom: 1rem;   
}
.input-group {
  display: flex;        
  flex-direction: row;   
  align-items: center;   
  gap: 0.5rem;           
}
.input{
    width: 40ch;
    padding: 0.5rem;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 1rem;
    size: 1rem;
}

.label{
    font-size: 1.2rem;
    color: black;
}

.search-container {
  max-width: 600px;
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
