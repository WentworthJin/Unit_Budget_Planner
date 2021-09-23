The table page is able to get data from the database uinsg flask.
The part:
@app.route("/upload",methods=["GET"])

in the route.py is the method to load this page.
Pass unit name from uploaded file to the function, and then the data list will pass the unit details to the table page.
