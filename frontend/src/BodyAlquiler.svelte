<script>
  import POLLITOALQUILER from "./pollo-alquiler.png";
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
      <div class="formularioalquiler">
        <h2 class="titulo">Escoge tus opciones de ALQUILER:</h2>
        <form class="content-form">
          <label>Día de recogida:</label>
          <input type="text"  />
          <label>Día de devolución:</label>
          <input type="text" />
        </form>
        <button type="submit">Reserva ahora!</button>
       
        
      </div>
      <div class="alquiler">
        <img class="pollitoalquiler" src={POLLITOALQUILER} alt="" />
      </div>
    </div>
  </div>
</div>

<style>
  h2 {
    font-size: 36px;
    font-family: "Nunito", sans-serif;
  }
  .alquiler {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 50px;
    margin-right: 50px;
  }
  .pollitoalquiler,
  .pollitopaseo {
    width: 200px;
    height: 200px;
    margin-bottom: 10px;
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
    justify-content: end;

    width: 800px;
    height: 400px;
    background-color: #391e6f;
    border-radius: 10px;
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
