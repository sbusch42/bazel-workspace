#!/bin/sh
docker run --rm --user $(id -u):$(id -g) -e USER="$(id -u)" -it -v $HOME/.cache:/.cache -v $PWD:/bazel ghcr.io/sbusch42/bazel-workspace
