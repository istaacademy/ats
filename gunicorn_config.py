# gunicorn_config.py

bind = "0.0.0.0:8000"
module = "aurigaone.wsgi:application"

workers = 4  # Adjust based on your server's resources
worker_connections = 1000
threads = 4

certfile = "/etc/letsencrypt/live/istaacademy.com/fullchain.pem"
keyfile = "/etc/letsencrypt/live/istaacademy.com/privkey.pem"