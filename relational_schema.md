# Relational Schema

##### Users(**user_id**, username, createTime)

##### Passwords(**password_id, user_id**, createTime)

please put a blank line here, i tried a bunch of stuff
#### Description:

#### This schema describes a relational database in which users keep their passwords.

* Each user in **Users** describes a user of the password manager and is given a unique id (user_id) and can choose to create a nickname. The time their userid is generated is stored as well.

* Each password in **Passwords** is a password created by a user. Each password is given a unique id **password_id** belonging to its owner. 