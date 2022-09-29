FROM python:3.8

COPY /app/requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

ADD /app /app/

ENV FLASK_APP /app/main.py
WORKDIR /app

RUN chmod +x ./entrypoint.sh
EXPOSE 5000
ENTRYPOINT ["sh", "entrypoint.sh"]

