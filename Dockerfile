FROM python:3.9

WORKDIR /app
COPY . .

RUN python3 -m venv env \
    && /app/env/bin/python3 -m pip install --upgrade pip \
    && /app/env/bin/python3 -m pip install -U -r /app/requirements.txt
CMD [ "/app/env/bin/python3", "main.py" ]
