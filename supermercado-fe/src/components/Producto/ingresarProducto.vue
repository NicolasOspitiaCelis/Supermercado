<template>
  <button
    class="regresar"
    @click="$router.push('/user/administrar/g_productos')"
  >
    Regresar
  </button>
  <div class="cont">
    <div class="contenedor">
      <h1>Registrar Producto</h1>
      <form v-on:submit.prevent="ingresarProducto">
        <div class="input-form">
          <label for="nombre">Id Proveedor: </label>
          <input type="number" v-model="producto.proveedor" />
        </div>
        <div class="input-form">
          <label for="nombre">Nombre : </label>
          <input type="text" v-model="producto.name" />
        </div>
        <div class="input-form">
          <label for="nombre">Categoria : </label>
          <input type="text" v-model="producto.category" />
        </div>
        <div class="btn-cont">
          <button class="form-button" type="submit">Registrar</button>
        </div>
      </form>
    </div>
  </div>
</template>
<script>
import axios from "axios";
export default {
  name: "ingresarProducto",
  data: function () {
    return {
      producto: {
        name: "",
        proveedor: "",
        category: "",
      },
    };
  },
  methods: {
    ingresarProducto: async function () {
      if (
        localStorage.getItem("token_access") === null ||
        localStorage.getItem("token_refresh") === null
      ) {
        this.$emit("logOut");
        return;
      }
      await this.verifyToken();
      let token = localStorage.getItem("token_access");
      axios
        .post(
          "https://supermercado-be.herokuapp.com/producto/",
          this.producto,
          {
            headers: { Authorization: `Bearer ${token}` },
          }
        )
        .then(() => {
          alert("Registro exitoso.");
        })
        .catch((error) => {
          console.log(error);

          alert(error + ". ERROR: Fallo en el registro del producto.");
        });
    },
    verifyToken: function () {
      return axios
        .post(
          "https://supermercado-be.herokuapp.com/refresh/",
          { refresh: localStorage.getItem("token_refresh") },
          {
            headers: {},
          }
        )
        .then((result) => {
          localStorage.setItem("token_access", result.data.access);
        })
        .catch(() => {
          this.$emit("logOut");
        });
    },
  },
};
</script>
<style scoped>
.cont {
  display: flex;
}

.contenedor {
  margin: auto;
  height: 450px;
  min-width: 450px;
  background: #9f83fa;
  border-radius: 20px;
  align-items: center;
  padding: 10px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.input-form {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 15px;
  margin-bottom: 5px;
}

.input-form label {
  font-size: 20px;
}

.input-form input {
  padding: 10px;
  border-radius: 5px;
  border: 1px solid black;
}

.btn-cont > .form-button {
  background-color: white;
  width: 100%;
  font-size: 20px;
  border-radius: 8px;
  padding: 10px;
  cursor: pointer;
  transition: all 0.5s;
}

.btn-cont > .form-button:hover {
  background-color: crimson;
}

.btn-cont {
  display: flex;
  gap: 10px;
}

h1 {
  font-size: 40px;
  color: rgb(255, 255, 255);
  text-align: center;
}

.regresar {
  width: 150px;
  height: 40px;
  margin: 0px 0px 0px 50px;
  color: #000000;
  text-align: center;
  font-size: 20px;
  border-radius: 10px;
  background: #ffffff;
  border: 1px solid #000000;
  filter: blur(0.3px);
  border-radius: 20px;
}
.regresar:hover {
  width: 150px;
  height: 40px;
  margin: 0px 0px 0px 50px;
  color: #000000;
  text-align: center;
  font-size: 20px;
  border-radius: 10px;
  background: crimson;
  border: 1px solid #000000;
  filter: blur(0.3px);
  border-radius: 20px;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th,
td {
  text-align: left;
  font-size: 20px;
  border: 1px solid #000000;
  padding: 5px;
  background-color: #f5edf8;
}
</style>