<script>
  import LOGO from "./Logo.png";
</script>

<div class="header">
  <img src={LOGO} alt="Logo" />
  <ul>
    <li><a href="#">Alquileres</a></li>
    <li><a href="#">Pita Paseo</a></li>
    <li><button>Tus Pitas</button></li>
  </ul>
</div>

<style>
  .header {
    height: 50px;
    background-color: #5df19b;
    padding: 10px;
    align-items: center;
    display: flex;
    justify-content: flex-end;
  }
  .header ul {
    list-style: none;
    display: flex;
    justify-content: flex-end;
    align-items: center;
  }
  .header li a {
    padding: 10px; /* Ajusta el valor según tu diseño */
  }
 a {
    text-decoration: none;
    color: #391e6f;
  }
   button {
    background-color: #391e6f; /* Ajusta el color de fondo */
    color: white; /* Ajusta el color del texto */
    border: none; /* Elimina el borde del botón */
    padding: 10px 20px;
    border-radius: 10px;
  }
  img {
    width: 100px; /* Ajusta el ancho según sea necesario */
    height: auto; /* Mantener la relación de aspecto */
    margin-right: 10px;
    justify-content: start;
  }
</style>
