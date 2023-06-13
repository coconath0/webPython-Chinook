from bottle import Bottle, run, template, request, redirect
from sqlalchemy import text
from database import engine

app = Bottle()

@app.route('/', method='GET')
@app.route('/', method='GET')
def home():
  # mensaje
  mensaje = request.params.mensaje
  # acceso a db
  conn = engine.connect()
  stmt = text(("SELECT * FROM artists").format())
  rows = conn.execute(stmt)
  conn.close()
  locals = {'artistas': rows, 'mensaje': mensaje}
  # respuesta
  return template('home', locals)

@app.route('/artist/edit', method='GET')
def artist_edit():
  artist_id = int(request.params.id)
  # acceso a db
  conn = engine.connect()
  stmt = text(("SELECT * FROM artists WHERE ArtistId = {}").format(artist_id))
  artista = conn.execute(stmt).fetchone()
  conn.close()
  locals = {'artista': artista, 'id': artist_id}
  # respuesta
  return template('artist_edit', locals)

@app.route('/artist/delete', method='GET')
def artist_delete():
  artist_id = int(request.params.id)
  # acceso a db
  conn = engine.connect()
  stmt = text(("DELETE FROM artists WHERE ArtistId = {}").format(artist_id))

  conn.execute(stmt)
  conn.commit()
  conn.close()

  # respuesta
  return redirect("/?mensaje=Se ha eliminado un artista")

@app.route('/artist/new', method='GET')
def artist_new():
  # acceso a db
  artista = (0, "")
  locals = {'artista': artista, 'id': 0}
  # respuesta
  return template('artist_new', locals)

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

  #if commit doesn't work -> AttributeError("'Connection' object has no attribute 'commit'") then enter in cmd: pip install --upgrade sqlalchemy
  conn.commit()
  conn.close()
  return redirect("/?mensaje=" + mensaje)
  
@app.route('/albums', method='GET')
def albums():
  # mensaje
  mensaje = request.params.mensaje
  # acceso a db
  conn = engine.connect()
  stmt = text(("""SELECT A.AlbumId, A.Title, AR.Name FROM
albums A INNER JOIN artists AR ON A.ArtistId = AR.ArtistId""").format())
  rows = conn.execute(stmt)
  conn.close()
  locals = {'albums': rows, 'mensaje':mensaje}
  # respuesta
  return template('albums', locals)


@app.route('/albums/edit', method='GET')
def albums_edit():
  album_id = int(request.params.id)
  # acceso a db
  conn = engine.connect()
  stmt = text(("SELECT * FROM albums WHERE AlbumId = {}").format(album_id))
  
  album = conn.execute(stmt).fetchone()
  
  stmt = text(("SELECT * FROM artists").format())
  artistas = conn.execute(stmt)
  conn.close()
  locals = {'album': album, 'id': album_id, 'artistas':artistas}
  # respuesta
  return template('album_edit', locals)

@app.route('/albums/delete', method='GET')
def album_delete():
  album_id = int(request.params.id)
  # acceso a db
  conn = engine.connect()
  stmt = text(("DELETE FROM albums WHERE AlbumId = {}").format(album_id))

  conn.execute(stmt)
  conn.commit()
  conn.close()

  # respuesta
  return redirect("/albums?mensaje=Se ha eliminado un album")

@app.route('/albums/new', method='GET')
def albums_new():
  # acceso a db
  conn = engine.connect()
  stmt = text(("SELECT * FROM artists").format())
  artistas = conn.execute(stmt)
  conn.close()
  album = (0, "", 0) # id, title, fk_artist
  locals = {'album': album, 'id': 0, 'artistas': artistas}
  # respuesta
  return template('album_new', locals)


@app.route('/albums/save', method='POST')
def albums_save():
  name = request.forms.get('name')
  id = int(request.forms.get('id'))
  artist_id = int(request.forms.get('artist_id'))
  # acceso a db
  conn = engine.connect()
  mensaje = ""
  if id == 0:
    # crear
    stmt = text(
      ("INSERT INTO albums (Title, ArtistId) VALUES ('{}', {})").format(
        name, artist_id))
    mensaje = "Album creado con éxito"
  else:
    stmt = text(
      ("UPDATE albums SET Title = '{}', ArtistId = {} WHERE AlbumId = {}"
       ).format(name, artist_id, id))
    mensaje = "Album editado con éxito"
  conn.execute(stmt)
  conn.commit()
  conn.close()
  return redirect("/albums?mensaje=" + mensaje)

if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True, reloader=True)

