from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
# Nur für Tests: Default secret key. Setze in Prod per ENV var.
app.secret_key = "dev-secret-key-change-me"

# Test-Benutzer (nur für Demo). In echt: Datenbank / Hashing verwenden.
TEST_USER = "tester"
TEST_PASS = "secret123"

@app.route("/")
def index():
    if session.get("logged_in"):
        return redirect(url_for("dashboard"))
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "")
    password = request.form.get("password", "")
    if username == TEST_USER and password == TEST_PASS:
        session["logged_in"] = True
        session["username"] = username
        return redirect(url_for("dashboard"))
    flash("Ungültige Zugangsdaten. Versuch: tester / secret123")
    return redirect(url_for("index"))

@app.route("/dashboard")
def dashboard():
    if not session.get("logged_in"):
        return redirect(url_for("index"))
    return render_template("dashboard.html", user=session.get("username"))

@app.route("/logout")
def logout():
	session.clear()
	return redirect(url_for("index"))

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    print("🚀 Flask server starting on port 8080...", flush=True)
    app.run(host="0.0.0.0", port=8080, debug=False)

