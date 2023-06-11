from bottle import Bottle, run, template, route, request, redirect
from sqlalchemy import text
from database import engine

app = Bottle()

@app.route('/', method='GET')
def home():
  # acceso a db
  conn = engine.connect()
  stmt = text(("SELECT * FROM artists").format())
  rows = conn.execute(stmt)

  locals = {'artistas': rows}
  # respuesta
  return template('home', locals)

@app.route('/artist/edit', method='GET')
def artist_edit():
  artist_id=int(request.params.id)
  # acceso a db
  conn = engine.connect()
  stmt = text(("SELECT * FROM artists WHERE ArtistId = {}").format(artist_id))
  artista = conn.execute(stmt).fetchone()

  locals = {'artista': artista, 'id': artist_id}
  # respuesta
  return template('artist_edit', locals)


@app.route('/artist/save', method='POST')
def artist_save():
  name = request.forms.get('name')
  id = int(request.forms.get('id'))
  # acceso a db
  conn = engine.connect()
  mensaje = ""
  if id == 0:
    # crear
    stmt = text(("INSERT INTO artists (Name) VALUES ('{}')").format(name))
    mensaje = "Artista creado con éxito"
  else:
    stmt = text(
      ("UPDATE artists SET Name = '{}' WHERE ArtistId = {}").format(name, id))
    mensaje = "Artista editado con éxito"
  conn.execute(stmt)
  conn.commit()
  conn.close()
  return redirect("/?mensaje=" + mensaje)





@app.route('/albums', method='GET')
def albums():
  # acceso a db
  conn = engine.connect()
  stmt = text(("""SELECT A.AlbumId, A.Title, AR.Name FROM
albums A INNER JOIN artists AR ON A.ArtistId = AR.ArtistId""").format())
  rows = conn.execute(stmt)
  print(rows)
  locals = {'albums': rows}
  
  # respuesta
  return template('albums', locals)

if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True, reloader=True)

