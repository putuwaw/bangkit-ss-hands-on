run-dev: 
	flask run --debug --port 8000

run-prod:
	gunicorn --bind 0.0.0.0:8000 --workers 4 app:app