#!/bin/sh
docker run --rm -it -v $PWD:/bazel bazel-workspace
