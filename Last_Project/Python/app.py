from flask import Flask, request, jsonify
import pandas as pd
import numpy
import json
import test_model

app = Flask(__name__)


@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/test<br/>"
    )


@app.route('/test', methods=["POST"])
def test():
    print("Example of data received")
    rf=request.get_json()
    print(rf)
    df =pd.DataFrame(rf['data'])
    model=test_model.predict(df.transpose())
    resp_dic={'result':str(model[0])}
    print(resp_dic)
    resp = jsonify(resp_dic)
    return resp

if __name__ == "__main__":
    app.run(debug=True)