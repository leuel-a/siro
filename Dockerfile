# base image -> has python pre-installed
# no need to install python
FROM python:3.12-slim

# it will check if the directory exists, if not create it
# it will change into that directory(context switch)
WORKDIR /app

# is like the package.json file for python
COPY requirements.txt .

# install the required packages
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python3", "./src/main.py"]
