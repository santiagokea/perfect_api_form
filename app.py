from bottle import default_app, delete, error, get, request, response, static_file, run


##############################
@get("/app.css")
def _():
  return static_file("app.css", root=".")

##############################
@get("/app.js")
def _():
  return static_file("app.js", root=".")

##############################
@get("/images/<image_name>")
def _(image_name):
  print(image_name)
  return static_file(image_name, root="./images")


##############################
# GET
import index
import items_get_by_id
import items_get_all

# POST
##############################
import items_post

# PUT
##############################
import items_put_by_id

# DELETE
##############################
import items_delete_by_id








##############################
##############################
##############################








##############################
try:
  import production
  application = default_app()
except Exception as ex:
  run(host="127.0.0.1", port=3333, debug=True, reloader=True, server="paste")




