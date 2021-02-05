from flask import Flask, render_template, request

app = Flask(__name__, template_folder="./src/views")


@app.route("/", methods=["GET", "POST"])
def home():
    if(request.method == "GET"):
        return render_template("index.html")
    if(request.form["num1"] != "" and request.form["escolha"] == "soma"):
        soma = int(request.form["num1"]) + int(request.form["num2"])
        return str(soma)
    if(request.form["num1"] != "" and request.form["num2"] != "" and request.form["escolha"] == "sub"):
        sub = int(request.form["num1"]) - int(request.form["num2"])
        return str(sub)
    if(request.form["num1"] != "" and request.form["num2"] != "" and request.form["escolha"] == "mult"):
        sub = int(request.form["num1"]) * int(request.form["num2"])
        return str(sub)
    if(request.form["num1"] != "" and request.form["num2"] != "" and request.form["escolha"] == "div"):
        sub = int(request.form["num1"]) / int(request.form["num2"])
        return str(sub)
    else:
        return "Informe um valor válido!"


@app.errorhandler(404)
def not_found(error):
    return render_template("error.html")


app.run(debug=True)
