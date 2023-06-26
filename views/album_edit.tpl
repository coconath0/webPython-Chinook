%include('header_footer.tpl')

<body>
  <h2>Edit Album {{id}} </h2>
<form action="/albums/save" method="post">
    <input type="hidden" name="id" value="{{album[0]}}"><br>
    <label for="name">Nombres:</label><br>
    <input type="text" id="names" name="name" value="{{album[1]}}"><br>
    <label for="">Artists:</label><br>
    <select name="artist_id">
      % for s in artistas:
        % if album[2] == s[0]:
          <option selected value="{{s[0]}}">{{s[1]}}</option>
        % else:
          <option value="{{s[0]}}">{{s[1]}}</option>
        % end
      % end
    </select><br>
    <button class="btn">Guardar Cambios</button>
  </form>
<a href="/albums"><button class="btn">Cancelar</button></a>
</body>
</html>