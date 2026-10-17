from flask import Flask, render_template_string, request

app = Flask(__name__)

PAGE = "<h1>Hello {{ name }}</h1>"


@app.get("/")
def index() -> str:
    return render_template_string(PAGE, name=request.args.get("name", "world"))
