FROM python:3.12-slim
WORKDIR /app

# Upgrade underlying Debian OS packages to patch system CVEs
RUN apt-get update && apt-get upgrade -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# Upgrade pip itself before installing requirements
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 5000
CMD ["python", "main.py"]