# Overview
This is an artifical bazel workspace, containing a small number of C++ packages. Each package contains a library and an executable:

- `//src/a`
- `//src/b`
- `//src/c`

Dependencies:

- `b` depends on `a`
- `c` depends on an auto-generated package `d`

Code-Generation:

- Packages `d`, `e`, and `f` are autogenerated by a script located in `scripts/generator.py`.

- It reads its configuration from `config/config.yaml`, and needs to be integrated into the build process.


# Questions
- Setup a build environment using the Dockerfile and scripts.
- Make yourself familiar with the workspace, give a short overview of the bazel project.
- How do you build and run target `//src/a:a`?
- How do you figure out the actual compile (gcc) and link (ld) commands that bazel runs when building `//src/a:a`?
- Try to build `//src/b:b`. Why is the build failing? How can you fix it?
- How can you query for all dependencies of `//src/b:b`?
- Package "c" depends on a target that is auto-generated. What are the options to successfully model the dependency and run the target `//src/c:c`?
- How do you make sure that the auto-generation is triggered whenever the config file has been modified?
