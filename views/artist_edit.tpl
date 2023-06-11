%include('header_footer.tpl')

<body>
  <h2>Edit Artista {{id}}</h2>
<form action="/artist/save" method="post">
    <input type="hidden" name="id" value="{{artista[0]}}"><br>
    <label for="name">Nombres:</label><br>
    <input type="text" id="names" name="name" value="{{artista[1]}}"><br>
    <button class="btn">Guardar Cambios</button>
  </form>
<a href="/"><button class="btn">Cancelar</button></a>
</body>
</html>