FROM python:3.12-slim
WORKDIR /app

# Install into a venv at /venv (outside /app, safe from bind mount)
RUN python -m venv /venv
COPY requirements.txt .
RUN /venv/bin/pip install --upgrade pip && /venv/bin/pip install -r requirements.txt

COPY . .
ENV PYTHONUNBUFFERED=1
ENV PATH="/venv/bin:$PATH"

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]