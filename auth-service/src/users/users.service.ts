import { Injectable } from '@nestjs/common';

export type User = any;

@Injectable()
export class UsersService {
  private readonly users: User[];

  constructor() {
    this.users = [
      {
        _id: '1',
        username: 'john',
        password: 'changeme',
      },
      {
        _id: '2',
        username: 'chris',
        password: 'secret',
      },
      {
        _id: '3',
        username: 'maria',
        password: 'guess',
      },
    ];
  }

  async getUser(username: string): Promise<User | undefined> {
    return this.users.find((user) => user.username === username);
  }
}
