from flask import Flask, jsonify, request
import numpy as np
import keras

app = Flask(__name__)


@app.route("/")
def hello_world():
    return jsonify(
        {"status": True, "code": 200, "message": "OK", "data": "Hello, World!"}
    )


@app.route("/predict", methods=["POST"])
def predict():
    # get post data
    data = request.get_json()

    # do something with data
    data = np.array(data)

    # load model
    model = keras.models.load_model("model/iris.keras")

    class_name = ["setosa", "versicolor", "virginica"]
    prediction = model.predict(data)
    proba = float(np.max(prediction))
    prediction = class_name[np.argmax(prediction)]

    return jsonify(
        {
            "status": True,
            "code": 200,
            "message": "OK",
            "data": {"prediction": prediction, "probabilty": proba},
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0")
