#include <string>
#include <regex>

#define REGEXFILENAME "^[a-zA-Z_][a-zA-Z0-9_]*$"

class Validate{
    private: 
        std::regex regexFilename{REGEXFILENAME};
    public:
        std::string input; 
        bool valFileName(std::string); // A method to Validate file name.
        Validate (std::string inputValue = "SEDfileName");
};
