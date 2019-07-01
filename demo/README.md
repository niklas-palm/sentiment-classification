# Twitter sentiment classifier for Swedish tweets.

This is a simple Flask API that uses a fast linear SVM to classify Swedish un-preprocessed tweets.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Installation guide

To install all dependencies, run

```
pip install -r requirements.txt
```

To run the Flask application, run

```
python app.py
```

which starts up a development server on port 5000. Visit localhost:5000 to verify the server is running properly.

### Example usage

```
curl -d '{ "data": "Det här är en ganska bra tweet" }' -H 'Content-Type: application/json' http://localhost:5000/api
```

Replace data value with desired tweet to classify.

### Responses

- 1 - Positive
- 0 - Neutral
- -1 - Negative
