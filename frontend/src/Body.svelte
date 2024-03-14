<script>
  import CardAve from "./CardAve.svelte";
</script>

<div class="menus">
  <div class="titulo">
    <h2>Escoge tu COMPAÑERX DE huevoaventura:</h2>
    <ul class="aves">
      <li><a href="#"></a>Gallina</li>
      <li><a href="#">Gallos</a></li>
      <li><a href="#">Pollitos</a></li>
    </ul>
  </div>
  <div class="pitas">
    <CardAve />
    <CardAve />
    <CardAve />
    <CardAve />
    <CardAve />
    <CardAve />
    <CardAve />
    <CardAve />
  </div>
</div>


<style>
 .pitas {
 justify-items: center;
  display: grid; 
  grid-template-columns: repeat(4, 1fr); 
  grid-template-rows: repeat(2, 1fr); 
  grid-column-gap: 10px;
  grid-row-gap: 50px; 
 }
  .menus {
    margin: 30px;
    margin-bottom: 60px;
  }
  .aves {
    display:flex;
    list-style: none;

    
  }
  .aves li {
    padding: 10px;
  }

  .titulo {
    text-align: left;
    margin-bottom: 10px;
    display: flex;
    
  }
  
  
</style>
