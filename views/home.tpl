%include('header_footer.tpl')

<body>
  <ul>
    <li><a class="active" href="/">Home</a></li>
    <li><a href="/albums">Albums</a></li>
  </ul>
  <h1>List of Artists</h1>

  <!--<a href="/artist/new"><button class="btn">Agregar Registro</button></a>-->
  <table class="center">
    <thead>
      <th>Id</th>
      <th>Artists</th>
      <th>Actions</th>
      
    </thead>
    <tbody>
      % for s in artistas:
      <tr>
        <td style="text-align: center">{{s[0]}}</td>
        <td style="text-align: center">{{s[1]}}</td>

        <td style="text-align: center">
          <a href="/artist/edit?id={{s[0]}}">Edit</a>
          <a href="/artist/delete?id={{s[0]}}">Eliminar</a>
        </td>
      </tr>
      % end
    </tbody>
  </table>
  <footer>
    <p>&copy; 2023 Ing. de Datos. All rights reserved.</p>
    <p>Designed by Nathaly Ingol</p>
  </footer>
</body>
</html>