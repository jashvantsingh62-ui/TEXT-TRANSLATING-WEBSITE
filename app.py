from flask import Flask, request, render_template
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route("/", methods=["GET", "POST"])
def home():
    translated_text = ""

    if request.method == "POST":
        text = request.form["text"]
        target_lang = request.form["language"]
        
        result = translator.translate(text, dest=target_lang)
        translated_text = result.text

    return render_template("index.html", translated=translated_text)

if __name__ == "__main__":
    app.run(debug=True)