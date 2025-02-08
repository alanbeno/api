from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/get-user/<value>")
def home(value):
    user_data = {
        "user_id" : value,
        "name" : "alan",
        "place" : "kerala"
          }
    
    '''
    It checks for a query parameter named extra using request.args.get("extra").
    If the extra query parameter is present in the URL, it adds it to the user_data dictionary under the keyy "extra".

    '''

    extra = request.args.get("extra")
    if extra:
        #if the query parameter is a digit then converting it to int from default string
        if extra.isdigit():
            user_data["extra"] = int(extra)
        else:
            user_data["extra"] = extra

    return jsonify(user_data),200

@app.route("/post-user",methods = ["POST"])

def post():
    data = request.get_json()

    return jsonify(data), 201


if __name__ == "__main__":
    app.run(debug = True)