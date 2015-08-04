# Ruby on Rails

## Ruby

Install rbenv:

    $ git clone https://github.com/sstephenson/rbenv.git ~/.rbenv
    $ echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.zshrc
    $ echo 'eval "$(rbenv init -)"' >> ~/.zshrc
    $ git clone https://github.com/sstephenson/ruby-build.git ~/.rbenv/plugins/ruby-build

Add default `.gemrc` file:

    $ echo 'gem: --no-document' > ~/.gemrc

Install some dependencies:

    $ sudo apt-get install -y libssl-dev libreadline-dev

Restart your shell and start install ruby with `rbenv`:

    $ rbenv install 2.2.2

After successful instalation install [Bundler](http://bundler.io/):

    $ gem install bundler

**protip**: After every new ruby version install `bundler`.

## Rails

    $ gem install rails

If this fails its probably because of `nokogiri` gem:

    $ gem install nokogiri
    $ gem install rails

## Deploying Rails Application

On *RPI*:

    $ sudo mkdir -p /var/www/web
    $ sudo chown pi:pi /var/www/web
    $ ssh -T git@github.com
    $ mysql
    mysql> create database <name>;
    $ sudo apt-get install -y libmysql-ruby libmysqlclient-dev nodejs
    $ gem install mysql2

On your local machine:

    $ mina setup
    $ mina deploy

On *RPI*:

    $ gem install passenger
    $ sudo $(which passenger-install-nginx-module)
