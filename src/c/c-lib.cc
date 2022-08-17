#include "c-lib.h"
#include <string>

std::string c::get_greet(const std::string& who) {
  return "c: Hello " + who;
}
