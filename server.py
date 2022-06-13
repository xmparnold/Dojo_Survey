from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "secret"



@app.route( "/" )
@app.route( "/home" )
def show_8_by_8_checkerboard():
    return render_template( "index.html" )

# @app.route( "/home", methods = [ 'POST' ] )
# def submit_form():
#         user_name = request.form[ "name" ],
#         user_location = request.form[ "location" ],
#         user_language = request.form[ "language" ],
#         user_cormment = request.form[ "comment" ]
#         return render_template( "result.html", form_name = user_name, form_location = user_location, form_language = user_language, form_comment = user_comment )

@app.route( "/home", methods = [ 'POST' ] )
def submit_form():
        session["user_name"] = request.form[ "name" ],
        session["user_location"] = request.form[ "location" ],
        session["user_language"] = request.form[ "language" ],
        session["user_comment"] = request.form[ "comment" ]
        return render_template( "result.html" )

@app.route( "/result" )
def show_result():
    return render_template("result.html" )


if __name__ == "__main__":
    app.run(debug = True)