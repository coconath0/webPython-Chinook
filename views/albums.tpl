%include('header_footer.tpl')

<body>
  <ul>
    <li><a class="active" href="/">Home</a></li>
    <li><a href="/albums">Albums</a></li>
  </ul>
  <h1>List of Albums</h1>
  <h3>{{mensaje}}</h3>
    <a href="/albums/new"><button class="btn">Agregar Registro</button></a>
  <table class="center">
    <thead>
      <th>Album ID</th>
      <th>Tittle</th>
      <th>Artists</th>
      <th>Operations</th>
    </thead>
    <tbody>
      % for s in albums:
      <tr>
        <td>{{s[0]}}</td>
        <td>{{s[1]}}</td>
        <td>{{s[2]}}</td>

        <td style="text-align: center">
          <a href="/albums/edit?id={{s[0]}}">Edit</a>
          <a href="/albums/delete?id={{s[0]}}">Eliminar</a>
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