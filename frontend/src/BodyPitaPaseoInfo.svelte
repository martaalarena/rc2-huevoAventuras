<script>
    import GALLINAS from "./Mask group.png";
  </script>
  
  <div class="content-info">
    <div class="info">
      <h2>Pitapaseos</h2>
      <p>
        Durante unas horas podrás a sacar a pasear a una de 
        nuestras aves por nuestra finca, disfrutando de un
        entorno natural incomparable.
      </p>
    </div>
    <img src={GALLINAS} alt="" />
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
  