FROM python:3
COPY . .
RUN pip install requeriments.txt
CMD [ "python", "./echobot.py" ]