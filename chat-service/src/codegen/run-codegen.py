from grpc_tools import protoc

protoc.main((
    '',
    '-I../protos',
    '--python_out=./src/codegen',
    '--pyi_out=./src/codegen',
    '--grpc_python_out=./src/codegen',
    '../protos/users.proto',
))
