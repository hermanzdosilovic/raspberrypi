# Zsh and Prezto

## Zsh

    $ sudo apt-get install zsh
    $ chsh -s /bin/zsh

## [Prezto](https://github.com/sorin-ionescu/prezto)

    $ git clone --recursive https://github.com/sorin-ionescu/prezto.git "${ZDOTDIR:-$HOME}/.zprezto"
    $ setopt EXTENDED_GLOB; for rcfile in "${ZDOTDIR:-$HOME}"/.zprezto/runcoms/^README.md(.N); do ln -s "$rcfile" "${ZDOTDIR:-$HOME}/.${rcfile:t}"; done

## [Punkt](https://github.com/hermanzdosilovic/dotfiles) (optional)

For me, my dotfiles.

    $ git clone https://github.com/hermanzdosilovic/dotfiles.git ~/.dotfiles
    $ cd ~/.dotfiles
    $ sudo ln -s ~/.dotfiles/punkt.sh /usr/local/bin/punkt
    $ punkt link zsh
