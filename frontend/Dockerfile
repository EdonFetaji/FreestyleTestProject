FROM python:3.12-slim
LABEL authors="Edon Fetaji"
WORKDIR /frontend
COPY . .
RUN pip install -r requirements.txt
CMD ["streamlit","run", "app.py"]