cc_library(
    name = "a-lib",
    srcs = ["a-lib.cc"],
    hdrs = ["a-lib.h"],
    includes = ["."],
    visibility = ["//visibility:public"]
)

cc_binary(
    name = "a",
    srcs = ["a.cc"],
    deps = [
        ":a-lib",
    ],
)
