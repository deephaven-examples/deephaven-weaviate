FROM ghcr.io/deephaven/server:0.27.0
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
COPY /data/app.d /app.d
