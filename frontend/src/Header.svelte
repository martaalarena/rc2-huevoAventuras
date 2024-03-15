<script>
  import LOGO from "./Logo.png";
  

  
</script>

  <div class="header">
    <img src={LOGO} alt="Logo" />
    <ul>
      <li><a href="/alquiler">Alquileres</a></li>
      <li><a href="/pitapaseo">Pita Paseo</a></li>
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
    
  }
 ul {
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
    background-color: #391e6f; 
    color: white; 
    border: none; 
    padding: 10px 20px;
    border-radius: 10px;
  }
  img {
    width: 100px; 
    height: auto; 
    margin-right: 10px;
    justify-content: start;
  }
</style>
