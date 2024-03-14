<script>
  import CardAve from "./CardAve.svelte";

</script>
<div class="menus">
  <div class="titulo">
  <h2>Escoge tu COMPAÑERX DE huevoaventura:</h2>
  </div>
  <ul class="aves">
    <li><a href="#"></a>Gallina</li>
    <li><a href="#">Gallos</a></li>
    <li><a href="#">Pollitos</a></li>
  </ul>
  <CardAve />
  
</div>

<style>
  .menus {
    display: flex;
    flex-direction: column; 
  
  }
  .aves {
    display: flex;
    list-style: none;
    align-items: center;
    justify-content: flex-end;

  }
  .aves li {
    padding: 10px;
  }
  
  .titulo {
  text-align: left; 
  margin-bottom: 10px;
  justify-content: flex-start;
  }
</style>
