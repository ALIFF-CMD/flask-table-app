from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    df = pd.read_csv("Table_Input.csv")
    df.set_index("Index #", inplace=True)

    # Table 2 calculations
    alpha = int(df.loc["A5", "Value"] + df.loc["A20", "Value"])
    beta = round(df.loc["A15", "Value"] / df.loc["A7", "Value"], 2)
    charlie = int(df.loc["A13", "Value"] * df.loc["A12", "Value"])

    table1 = df.reset_index().to_html(index=False, classes="table table-striped")

    table2 = {
        "Alpha": alpha,
        "Beta": beta,
        "Charlie": charlie
    }

    return render_template("index.html", table1=table1, table2=table2)

if __name__ == "__main__":
    app.run(debug=True)
