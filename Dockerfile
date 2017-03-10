# Partially based on https://github.com/docker-library/celery/blob/master/4.0/Dockerfile
# And https://github.com/dib-lab/soursigs/blob/6c6acf6429cec2e2e4a076dfc32adbf27fab1eed/Dockerfile
FROM python:3.5-slim

RUN groupadd user && useradd --create-home --home-dir /home/user -g user user
WORKDIR /home/user

ENV CELERY_VERSION 4.0.2

COPY requirements.in .

RUN pip install pip-tools && \
    pip-compile requirements.in && \
    pip install -r requirements.txt

RUN { \
	echo 'import os'; \
	echo "BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'amqp://')"; \
} > celeryconfig.py

# --link some-rabbit:rabbit "just works"
ENV CELERY_BROKER_URL amqp://guest@rabbit

USER user

COPY downloader.py downloader.py

CMD ["celery", "-A", "downloader", "-c", "1", "worker"]
