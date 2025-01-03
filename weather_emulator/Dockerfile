FROM python:3.9-slim

WORKDIR /app

# Install uv
RUN pip install uv

# Copy project files
COPY pyproject.toml .
COPY weather_emulator.py .

# Install dependencies using uv
RUN uv pip install --system .

CMD ["python", "weather_emulator.py"]
