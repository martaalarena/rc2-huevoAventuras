<script>
  import POLLITOALQUILER from "./pollo-alquiler.png";
  import POLLITOPITAPASEO from "./pollo-pitapaseo.png";
</script>

<div class="content">
  <h2>¡Elije tu HuevoAventura!</h2>

  <div class="subcontent">
    <div class="infopita">
      <img src="" alt="pita" />
      <h3>Nombre de la Pita</h3>
      <p>
        Lorem ipsum dolor sit amet consectetur, adipisicing elit. Cupiditate
        facilis suscipit odio iste totam dignissimos odi voluptatem voluptate ab
        sed.
      </p>
    </div>
    <div class="contentopciones">
      <div class="alquiler">
        <img class="pollitoalquiler" src={POLLITOALQUILER} alt="" />
        <button>Alquiler</button>
      </div>
      <div class="pitapaseo">
        <img class="pollitopaseo" src={POLLITOPITAPASEO} alt="" />
        <button>PitaPaseo</button>
      </div>
    </div>
  </div>
</div>

<style>
    h2 {
        font-size: 36px;
        font-family:'Nunito', sans-serif;
    }
   /*.alquiler{
        margin-left: 100px;
    }*/
  .pollitoalquiler,
  .pollitopaseo {
    width: 200px;
    height: 200px;
  }

  .subcontent {
    display: flex; /* Make subcontent a flex container */
    justify-content: center;
    align-content: center; /* Center elements horizontally within subcontent */
    /* Center elements vertically within subcontent (optional) */
  }

  .content {
    text-align: center;
    justify-content: center;
    align-items: center;
    height: 700px;
  }
  img {
    width: 300px;
    height: 300px;
    padding: 20px;
  }
  .infopita {
    align-items: center;
    width: 400px;
    height: 800px;
    margin: 40px;
  }
  .contentopciones {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 800px;
    height: 400px;
    background-color: #391e6f;
    border-radius: 10px;
    margin: 40px;
  }
  button {
    width: 200px;
    height: 50px;
    border: none; /* Elimina el borde del botón */
    padding: 10px 20px;
    border-radius: 10px;
    background-color: transparent;
    font-family: "Nunito", sans-serif;
    font-size: 20px;
    color: white;
    border-color: white;
    border-width: 2px;
    border-style: solid;
  }
  .subcontent {
    display: flex;
  }
</style>
