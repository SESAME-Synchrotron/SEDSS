#include "validate.h"
#include <string>
#include <regex>

validate::validate(std::string inputValue){
    validate::input = inputValue;
}

bool validate::valFileName(std::string filename){
    /*
    A method to validate the file name.
    */
   validate::input = filename;
    return regex_match(validate::input, validate::regexFilename);
}
