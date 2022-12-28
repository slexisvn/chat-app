import grpc

from fastapi import FastAPI
from jose import jwt

from codegen import users_pb2_grpc, users_pb2

app = FastAPI()


@app.get('/')
async def root():
    with grpc.insecure_channel('localhost:24352') as channel:
        stub = users_pb2_grpc.UserServiceStub(channel)
        user = stub.GetUser(users_pb2.GetUserRequest(username='john'))
        print(user)
    return 'user'
