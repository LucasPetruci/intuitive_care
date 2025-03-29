FROM python:3.10.11

WORKDIR /app/api/backend

COPY requirements.txt /app 

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY api/backend /app/api/backend

COPY data_base /app/data_base

EXPOSE 8000

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
