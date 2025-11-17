from flask import Flask, request, render_template_string
from query_data import run_query

app = Flask(__name__)

HTML = """
<form method="POST">
  <input name="q" style="width:400px;" placeholder="Ask...">
  <button type="submit">Ask</button>
</form>
<p>{{answer}}</p>
"""

@app.route("/", methods=["GET","POST"])
def home():
    answer = ""
    if request.method == "POST":
        answer = run_query(request.form["q"])
    return render_template_string(HTML, answer=answer)

app.run(port=5000)
