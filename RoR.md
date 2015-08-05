# Ruby on Rails

## Ruby

  1. Install rbenv:

        $ git clone https://github.com/sstephenson/rbenv.git ~/.rbenv
        $ echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.zshrc
        $ echo 'eval "$(rbenv init -)"' >> ~/.zshrc
        $ git clone https://github.com/sstephenson/ruby-build.git ~/.rbenv/plugins/ruby-build

  2. Add default `.gemrc` file:

        $ echo 'gem: --no-document' > ~/.gemrc

  3. Install some dependencies:

        $ sudo apt-get install -y libssl-dev libreadline-dev ruby-dev

  4. Restart your shell and install ruby with `rbenv`:

        $ rbenv install 2.2.2

  5. After successful instalation install [Bundler](http://bundler.io/):

        $ gem install bundler

**protip**: After every new ruby version install `bundler`.

## Rails

  1. Install some dependencies:

        $ sudo apt-get install -y nodejs

  2. Install rails:

        $ gem install rails

If this fails its probably because of `nokogiri` gem:

    $ gem install nokogiri
    $ gem install rails

## Deploying Rails Application

### Install nginx and passenger

You will install nginx and passenger in `opt` folders. It is important that during installation owner of those folder is user who has `.rbenv` installed in his home folder.

  1. Install some dependencies:

        $ sudo apt-get install -y libcurl4-openssl-dev

  2. Download and extract passenger:

        $ cd /opt
        $ sudo wget http://s3.amazonaws.com/phusion-passenger/releases/passenger-5.0.15.tar.gz
        $ sudo tar xvf passenger-5.0.15.tar.gz
        $ sudo chown -R pi: passenger-5.0.15

  3. Create folder where `nginx` will be located:

        $ sudo mkdir nginx
        $ sudo chown -R pi: nginx

  4. Start installing passenger module and nginx:

        $ cd passenger-5.0.15/
        $ ./bin/passenger-install-nginx-module

  5. After instalation open `/opt/nginx/conf/nginx.conf` file and make sure you have these lines in `http` section:

        passenger_root /opt/passenger-5.0.15;
        passenger_ruby /home/pi/.rbenv/shims/ruby;

  6. Change owner to `root` after installation:

        $ sudo chown -R root: /opt/passenger-5.0.15 /opt/nginx

#### To make nginx start at system startup follow these instructions:

  1. Create custom script for starting and stoping nginx:

        $ sudo vim /etc/init.d/nginx

  2. Copy [this](https://github.com/JasonGiedymin/nginx-init-ubuntu/blob/master/nginx) content into `nginx` script, save and exit.

      * Make sure that `NGINXPATH` variable (line 87) points to correct location:

            NGINXPATH=${NGINXPATH:-/opt/nginx}      # root path where installed

  3. Change premissions:

        $ sudo chmod 755 /etc/init.d/nginx

  4. Test script:

          $ sudo /etc/init.d/nginx start
          $ sudo /etc/init.d/nginx stop

  5. Register script to be run at startup:

          $ sudo update-rc.d nginx defaults

  6. If you want to remove script from startup, run the following command:

          $ sudo update-rc.d -f nginx defaults

  7. Reboot *RPI*

### Prepare environment

#### On Server:

  1. Create folder where you want your app to be located:

        $ sudo mkdir -p /var/www/myapp

  2. Change owner to `pi`:

        $ sudo chown -R pi: /var/www/myapp

  3. Add `github.com` to list of known hosts. You just need to do this once:

        $ ssh -T git@github.com

  4. Create database and user for your application:

        $ mysql
        mysql> CREATE DATABASE myapp;
        mysql> CREATE USER 'myapp_p'@'localhost' IDENTIFIED BY 'generaterandompassword';
        mysql> GRANT ALL ON myapp.* TO 'myapp_p'@'localhost';

  5. Open `nginx.conf` and configure inside `http` section:

        server {
          listen 80;
          server_name myapp.com;
          root /var/www/myapp/current/public;
          passenger_enabled on;
        }

#### On your machine:

  1. Install `mina`

        $ gem install mina

  2. Setup your deploy script:

        $ mina setup

  3. Configure `config/deploy.rb`:

        set :repository, 'git@github.com:yourusername/myapp.git'
        set :branch, 'master'

        set :user, 'pi'
        set :domain, 'myapp.com'
        set :deploy_to, '/var/www/myapp'
        set :port, '22219'
        set :forward_agent, true

        set :shared_paths, ['log', 'public/system']

  4. Configure `config/database.yml`:

        default: &default
        adapter: mysql2
        encoding: utf8
        pool: 5
        username: root
        password:
        socket: /tmp/mysql.sock

        production:
          <<: *default
          database: myapp
          username: myapp_p
          password: generaterandompassword
          socket: /var/run/mysqld/mysqld.sock

        development:
          <<: *default
          database: myapp_development

        test:
          <<: *default
          database: myapp_test

  5. Commit and push your changes:

        $ git add .
        $ git commit -m "Configured deploy.rb and database.yml"
        $ git push

  6. Deploy your app:

        $ mina deploy
