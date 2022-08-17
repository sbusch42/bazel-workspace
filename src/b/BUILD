cc_library(
    name = "b-lib",
    srcs = ["b-lib.cc"],
    hdrs = ["b-lib.h"],
    includes = ["."],
    visibility = ["//visibility:public"]
)

cc_binary(
    name = "b",
    srcs = ["b.cc"],
    deps = [
        ":b-lib",
    ],
)
