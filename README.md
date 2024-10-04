# bangkit-ss-hands-on

Bangkit Sharing Session ML Hands On

## Installation:

- Clone the repository:
```bash
git clone https://github.com/putuwaw/bangkit-ss-hands-on.git
```
- Install dependencies:
```bash
pip install -r requirements.txt
```
- [Optional] Train the model:
```bash
python training.py
```
- Run the Flask web server:
```bash
flask run --debug --port 8000
```
- Try it out:

```
Imagine you're observing an iris flower with the following characteristics:

Sepal length: 5 cm
Sepal width: 3 cm
Petal length: 1 cm
Petal width: 0.5 cm
Curious about which species this might be?
```

You can easily predict the species using cURL. Simply run the following command in your terminal (Linux, Mac, or WSL):

```bash
curl --location 'http://localhost:8000/predict' --header 'Content-Type: application/json' --data '[[5,3,1,0.5]]'
```

Or using Command Propt (CMD) & PowerShell:
```bash
curl.exe --location "http://localhost:8000/predict" --header "Content-Type: application/json" --data "[[5,3,1,0.5]]"
```

Then you can see the result:
```json
{
  "code": 200,
  "data": {
    "prediction": "setosa",
    "probabilty": 0.9401243925094604
  },
  "message": "OK",
  "status": true
}
```