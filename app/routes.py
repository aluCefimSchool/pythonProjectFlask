from app import app

@app.route("/")
def r_index():
    return "Hello blah world !"

@app.route("/test")
def r_test():
    return "Coucou c'est un test !"
