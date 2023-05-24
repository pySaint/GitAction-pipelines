FROM python:3.9-slim-buster

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["pytest -m 'debug' app/tests/sample-tests/step_defs"]

#ENTRYPOINT ["bash"]
