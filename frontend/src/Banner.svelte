<script>
  import HERO from "./HERO.jpg";
</script>

<div class="banner">
  <div class="text">
    <h2 class="eslogan">¡CONVIÉRTEE EN UN PITALOVER!</h2>
    <h2 class="titulo1">Primer servicio de alquilerde pitas en España</h2>
  </div>
  <img class="img-banner" src={HERO} alt="Banner" />
</div>

<style>
  .banner {
    position: relative;
  }
  .img-banner {
    display: block;
    width: 100%;
  }
  .text {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: white;
    z-index: 1;
  }
  .eslogan {
    font-family: "Nunito", sans-serif;
    font-size: 15px;
    text-align: center;
  }
  .titulo1 {
    font-family: "Nunito", sans-serif;
    font-size: 40px;
    text-align: center;
  }
</style>
