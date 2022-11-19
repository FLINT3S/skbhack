import {User} from "../data/User";

enum Role {
  ADMIN = "Admin",
  USER = "User"
}

export class AdminPanelUser extends User {
  role!: Role;
  blocked!: boolean;
  verified!: boolean;
}
