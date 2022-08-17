cc_library(
    name = "c-lib",
    srcs = ["c-lib.cc"],
    hdrs = ["c-lib.h"],
    includes = ["."],
    visibility = ["//visibility:public"]
)

cc_binary(
    name = "c",
    srcs = ["c.cc"],
    deps = [
        ":c-lib",
    ],
)
