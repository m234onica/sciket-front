from flask import render_template
from src import create_app
app = create_app()

@app.route("/")
def main():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()
