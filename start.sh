echo 'Start NGINX'
servise nginx start

echo 'Start supervisor'
poetry run ./main.py start-super
