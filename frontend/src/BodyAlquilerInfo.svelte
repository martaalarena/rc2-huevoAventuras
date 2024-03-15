<script>
  import GALLINAPASEO from "./Mask group-2.png";
</script>

<div class="content-info">
  <div class="info">
    <h2>¡Pon una pita en tu vida!</h2>
    <p>
      Disfruta del primer servicio web de alquiler de pitas en España. Nuestras
      gallinas sabrán cómo animar tu fiesta, entretener a los niños, hacer de tu
      cita un éxito... Multiplica los likes en tus redes sociales con nuestra
      selección de tiernos pollitos o escoge una de nuestras gallinas de razas
      increíbles para combinar con tus mejores looks.
    </p>
  </div>
  <img src={GALLINAPASEO} alt="" />
</div>

<style>
  .content-info {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .info {
    display: flex;
    flex-direction: column;    
    justify-content: center;
    align-items: center;
    height: 350px;
    text-align: justify;
    margin: 20px;
    font-size: 20px;
    font-family:"Nunito", sans-serif; ;
   
  }
  img {
    justify-content: end;
    height: 350px;
  }
</style>
