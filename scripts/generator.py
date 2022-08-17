#!/usr/bin/env python3

from jinja2 import Template
import logging
from pathlib import Path
from typing import Dict
import yaml

_BAZEL_BUILD = """
cc_library(
    name = "{{ name }}-lib",
    srcs = ["{{ name}}-lib.cc"],
    hdrs = ["{{ name}}-lib.h"],
    includes = ["."],
    visibility = ["//visibility:public"]
)

cc_binary(
    name = "{{ name }}",
    srcs = ["{{ name }}.cc"],
    deps = [
        ":{{ name }}-lib",
    ],
)
"""

_CPP_LIB = """
#include "{{ name }}-lib.h"
#include <string>

std::string {{ name }}::get_greet(const std::string& who) {
  return "{{ name }}: Hello " + who;
}
"""

_CPP_LIB_H = """
#ifndef MAIN_{{ name|upper }}_H_
#define MAIN_{{ name|upper }}_H_

#include <string>

namespace {{ name }} {
  std::string get_greet(const std::string &thing);
}
#endif
"""

_CPP_MAIN = """
#include "{{ name }}-lib.h"
#include <ctime>
#include <iostream>
#include <string>

void print_localtime() {
  std::time_t result = std::time(nullptr);
  std::cout << std::asctime(std::localtime(&result));
}

int main(int argc, char** argv) {
  std::string who = "{{ name }}";
  if (argc > 1) {
    who = argv[1];
  }
  std::cout << {{ name }}::get_greet(who) << std::endl;
  print_localtime();
  return 0;
}
"""


class BazelPackage:
    def __init__(self, name: str, location: Path):
        self.name = name
        self.location = location

    def generate(self) -> None:
        self.location.mkdir(parents=True, exist_ok=True)
        self._generate_build_file()
        self._generate_main_application()
        self._generate_library()

    def _generate_build_file(self) -> None:
        tm = Template(_BAZEL_BUILD)
        buildfile = tm.render(name=self.name)

        location = self.location / "BUILD"
        with location.open("w") as file:
            file.write(buildfile)

    def _generate_main_application(self) -> None:
        tm = Template(_CPP_MAIN)
        maincpp = tm.render(name=self.name)

        location = self.location / f"{self.name}.cc"
        with location.open("w") as file:
            file.write(maincpp)

    def _generate_library(self) -> None:
        tm = Template(_CPP_LIB)
        libcpp = tm.render(name=self.name)
        tm = Template(_CPP_LIB_H)
        libh = tm.render(name=self.name)

        libcpp_path = self.location / f"{self.name}-lib.cc"
        with libcpp_path.open("w") as file:
            file.write(libcpp)
        libh_path = self.location / f"{self.name}-lib.h"
        with libh_path.open("w") as file:
            file.write(libh)


def main(ws: Path, config: Dict) -> None:
    for pkg in config["packages"]:
        pkg_path = Path("src") / pkg
        logging.info("Generating package: %s -> %s", pkg, pkg_path.as_posix())
        pkg = BazelPackage(pkg, pkg_path)
        pkg.generate()


if __name__ == "__main__":
    logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.DEBUG)

    workspace = Path(__file__).parent.parent
    with (workspace / "config/config.yaml").open() as f:
        config = yaml.load(f, Loader=yaml.SafeLoader)

    main(workspace, config)
