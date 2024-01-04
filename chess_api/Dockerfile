FROM python:3.12

WORKDIR /chess_api

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn", "-w", "3", "--bind", "0.0.0.0:8000", "chess_api.wsgi:application"]
