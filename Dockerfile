FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirment.txt
EXPOSE 80
ENTRYPOINT ["python", "app.py"]