from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def contact_form():
   if request.method == "POST":
       form_data = {
           "name": request.form.get("name"),
           "email": request.form.get("email"),
           "phone": request.form.get("phone"),
           "message": request.form.get("message"),
           "subject": request.form.get("subject"),
           "preferred_contact": request.form.getlist("preferred_contact"),
           "agreement": "Yes" if request.form.get("agreement")else "No"
       }
       return redirect(url_for("confirmation", **form_data))
    return render_template("contact_form.html")

@app.route("/confirmation")
def confirmation():
    return render_template("confirmation.html", **request.args)

if __name__ == "__main__":
    app.run(debug=True)