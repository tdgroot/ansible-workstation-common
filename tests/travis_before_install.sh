#!/bin/bash

if [ $TRAVIS_OS_NAME = "linux" ]; then
  sudo apt-get -qq update
fi

if [ $TRAVIS_OS_NAME = "osx" ]; then
  brew install pyenv-virtualenv
fi
