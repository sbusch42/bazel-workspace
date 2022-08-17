#include "a-lib.h"
#include <string>

std::string a::get_greet(const std::string& who) {
  return "a: Hello " + who;
}
