# Install MySQL

## MySQL

When installing mysql you don't have to set any password for `root` (not recomemended).

#### Install:

Basic:

    $ sudo apt-get install -y mysql-client mysql-server

If you are gonna use MySQL with Ruby on Rails applications install:

    $ sudo apt-get install -y libmysql-ruby libmysqlclient-dev

#### Connect:

Use `-p` flag if you set up some password for `root` user.

    $ mysql -u root -p

#### Create User:

Create user with password:

    mysql> CREATE USER 'pi'@'localhost' IDENTIFIED BY 'mypass';

or create user without password:

    mysql> CREATE USER 'pi'@'localhost';

Give user all privileges:

    mysql> GRANT ALL ON *.* TO 'pi'@'localhost' WITH GRANT OPTION;

Now you can connect just with `mysql -p` or `mysql`.

#### Enable remote access:

In `/etc/mysql/my.cnf` file comment following line:

    bind-address           = 127.0.0.1

Grant access from any IP address:

    mysql> GRANT ALL ON *.* TO 'pi'@'%' WITH GRANT OPTION;

Restart mysql service:

    $ sudo service mysql restart

#### Userful commands:

Show all users:

    mysql> SELECT user, host FROM mysql.user;

#### Documentation:

* [CREATE USER](https://dev.mysql.com/doc/refman/5.1/en/create-user.html)
* [DROP USER](https://dev.mysql.com/doc/refman/5.1/en/drop-user.html)
* [GRANT](https://dev.mysql.com/doc/refman/5.1/en/grant.html)
* [REVOKE](https://dev.mysql.com/doc/refman/5.1/en/revoke.html)
* [SHOW GRANTS](http://dev.mysql.com/doc/refman/5.6/en/show-grants.html)
