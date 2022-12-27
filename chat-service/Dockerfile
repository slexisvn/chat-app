FROM python:3.10
WORKDIR /build
RUN pip install -r requirements.txt
EXPOSE 24351
COPY . .
CMD uvicorn src.main:app --reload