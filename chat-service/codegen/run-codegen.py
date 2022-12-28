from grpc_tools import protoc

protoc.main((
    '',
    '-I../protos',
    '--python_out=./codegen',
    '--pyi_out=./codegen',
    '--grpc_python_out=./codegen',
    '../protos/users.proto',
))
