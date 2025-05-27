FROM registry.access.redhat.com/ubi9/ubi:9.4

RUN dnf install -y python3-pip python3-devel

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip3 install -r /app/requirements.txt

COPY validate.py /app

COPY wsgi.py /app

CMD gunicorn --certfile=/certs/tls.crt --keyfile=/certs/tls.key --bind 0.0.0.0:9443 wsgi:webhook
