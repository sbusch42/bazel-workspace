#include "b-lib.h"
#include <string>

std::string b::get_greet(const std::string& who) {
  return "b: Hello " + who;
}
