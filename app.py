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
    try:
        # get post data
        data = request.get_json()

        # do something with data
        data = np.array(data)

        # load model
        model = keras.models.load_model("model/iris.keras")

        # get class names from iris.target_names
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
    except Exception as e:
        return jsonify(
            {
                "status": False,
                "code": 500,
                "message": str(e),
                "data": None,
            }
        ), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0")
