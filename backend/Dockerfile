FROM python:3.12-alpine
LABEL authors="Edon Fetaji"
WORKDIR /backend
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]