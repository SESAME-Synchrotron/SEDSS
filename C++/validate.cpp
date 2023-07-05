#include "validate.h"
#include <string>
#include <regex>

Validate::Validate(std::string inputValue){
    Validate::input = inputValue;
}

bool Validate::valFileName(std::string filename){
    /*
    A method to Validate the file name.
    */
   Validate::input = filename;
    return regex_match(Validate::input, Validate::regexFilename);
}
