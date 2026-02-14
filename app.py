from flask import Flask, request, render_template
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    translated_text = ""

    if request.method == "POST":
        text = request.form.get("text", "")
        target_lang = request.form.get("language", "")

        try:
            # Translate using deep_translator
            translated_text = GoogleTranslator(source="auto", target=target_lang).translate(text)
        except Exception as e:
            translated_text = f"Error: {str(e)}"

    return render_template("index.html", translated=translated_text)


if __name__ == "__main__":
    app.run(debug=True)
