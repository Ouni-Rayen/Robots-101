from flask import Flask, render_template, Response
import os

app = Flask(__name__)

FLAG = "Securinets{r0b0ts_txt_h1dd3n_p4ths}"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/robots.txt")
def robots():
    content = """User-agent: *
Disallow: /admin
Disallow: /dashboard
Disallow: /api
Disallow: /backup
Disallow: /private

# TODO: remove before production
# temporary flag location: /dev/tmp-flag-9f2a
"""
    return Response(content, mimetype="text/plain")


@app.route("/admin")
@app.route("/dashboard")
@app.route("/api")
@app.route("/backup")
@app.route("/private")
def blocked():
    return render_template("blocked.html"), 403


@app.route("/dev/tmp-flag-9f2a")
def secret():
    return render_template("flag.html", flag=FLAG)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
