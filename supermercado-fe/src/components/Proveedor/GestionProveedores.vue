<template>
  <button class="regresar" @click="$router.push('/user/administrar')">
    Regresar
  </button>
  <div class="contenedor">
    <h1>Gestión de Proveedores</h1>
    <button @click="$router.push('/user/administrar/g_proveedores/ingresar')">
      Ingresar proveedor
    </button>
    <button @click="$router.push('/user/administrar/g_proveedores/actualizar')">
      Actualizar proveedor
    </button>
    <button @click="$router.push('/user/administrar/g_proveedores/reporte')">
      Reporte de proveedores
    </button>
    <button @click="$router.push('/user/administrar/g_proveedores/eliminar')">
      Eliminar proveedor
    </button>
  </div>
</template>
<script>
export default {
  name: "Proveedores",
  data: function () {},
  methods: {},
  created: function () {},
};
</script>
<style scoped>
.contenedor {
  margin: auto;
  height: 450px;
  width: 450px;
  background: #9f83fa;
  border-radius: 20px;
  align-items: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
h1 {
  font-size: 40px;
  color: rgb(255, 255, 255);
  text-align: center;
}
button {
  width: 300px;
  height: 40px;
  margin-bottom: 5px;
  color: #000000;
  text-align: center;
  font-size: 20px;
  border-radius: 10px;
  background: #ffffff;
  border: 1px solid #000000;
  filter: blur(0.3px);
  border-radius: 20px;
  cursor: pointer;
  transition: all 0.5s;
}

button:hover {
  width: 300px;
  height: 40px;
  text-align: center;
  font-size: 20px;
  border-radius: 10px;
  border: 1px solid #000000;
  filter: blur(0.3px);
  border-radius: 20px;
  color: #e5e7e9;
  background: crimson;
  border: 1px solid #283747;
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
  transition-duration: 0.5s;
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
  filter: blur(0.4px);
  border-radius: 20px;
}
</style>