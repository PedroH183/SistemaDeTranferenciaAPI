FROM python:3.12-alpine

WORKDIR /API/Transferencia

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000
COPY . .

ENTRYPOINT [ "python3", "run.py" ]