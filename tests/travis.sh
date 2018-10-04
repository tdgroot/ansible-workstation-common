#!/bin/bash
source .venv/bin/activate

if [ $TRAVIS_OS_NAME = "linux" ]; then
  molecule test -s default
elif [ $TRAVIS_OS_NAME = "osx" ]; then
  molecule test -s macos
fi
