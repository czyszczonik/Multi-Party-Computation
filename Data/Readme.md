# DATABASE
## Database users:
Credentials: `user:password`
## Collections:
1. Application user database - `auth`
    Created users:     `user:password` and `user2:password2`
    Schema: `` { username: "user", password: "pass", salt: "salt" } ``
    Password stored in DB is creatd in following way: SHA256(salt+password). "+" mean concatenation.
