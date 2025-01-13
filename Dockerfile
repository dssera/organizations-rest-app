FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DATABASE_URL=sqlite:///./database1.db
ENV API_SECRET_KEY=secret

EXPOSE 8000

RUN python mock_data.py

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]


