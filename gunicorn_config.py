# gunicorn_config.py

bind = "0.0.0.0:8000"
module = "kernel.wsgi:application"

workers = 4  # Adjust based on your server's resources
worker_connections = 1000
threads = 4

certfile = "/etc/letsencrypt/live/www.istaacademy.com/fullchain.pem"
keyfile = "/etc/letsencrypt/live/www.istaacademy.com/privkey.pem"