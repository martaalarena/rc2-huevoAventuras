<script>
  import D3G from "./D3G.jpeg";
</script>

<div class="card">
  <img src={D3G} alt="Banner" />
  <div class="description">
    <h2>Nombre Pita</h2>
    <p>
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Quia soluta eius
      commodi suscipit perferendis deleniti accusantium, dolore tempora
      praesentium quaerat ipsa perspiciatis! Quo a ducimus facilis
    </p>
  </div>
  <a href="/pitaopcion">
    <button class="opction">TE ELIJO A TI</button>
  </a>
</div>

<style>
  .card {
    width: 150px;
    height: 250px;
  }
  img {
    width: 150px;
    height: 150px;
    border-radius: 10px;
  }
  .description {
    text-align: center;
    font-family: "Nunito", sans-serif;
    font-size: 7px;
  }
  .opction {
    display: flex;
    justify-content: center;
    background-color: #5df19b;
    border-radius: 5px;
    border: none; /* Elimina el borde del botón */
    padding: 5px 10px;
    margin: 10px;
  }
</style>
