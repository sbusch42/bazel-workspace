cmake_minimum_required(VERSION 3.15.5)
project(a)

add_library(${PROJECT_NAME}-lib
    a-lib.cc
    a-lib.h
)

add_executable(${PROJECT_NAME}
   a.cc
)

target_link_libraries (${PROJECT_NAME}
    LINK_PUBLIC ${PROJECT_NAME}-lib
)
