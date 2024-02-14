FROM amazon/aws-lambda-python:3.11

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src src
CMD ["src/main.lambda_handler"]