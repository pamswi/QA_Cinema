FROM python:3.11
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
RUN python3 create.py 
ENTRYPOINT ["python3", "app.py"]



