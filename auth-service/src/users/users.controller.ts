import { Controller } from '@nestjs/common';
import { GrpcMethod } from '@nestjs/microservices';
import { UsersService, User } from './users.service';
import { GetUserRequest } from '../codegen/users';

@Controller()
export class UsersController {
  constructor(private readonly usersService: UsersService) {}

  @GrpcMethod('UserService')
  async getUser(request: GetUserRequest): Promise<User | undefined> {
    return this.usersService.getUser(request.username);
  }
}
