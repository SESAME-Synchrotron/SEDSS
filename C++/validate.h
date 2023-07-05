#include <string>
#include <regex>

#define REGEXFILENAME "^[a-zA-Z_][a-zA-Z0-9_]*$"

class validate{
    private: 
        std::regex regexFilename{REGEXFILENAME};
    public:
        std::string input; 
        bool valFileName(std::string); // A method to validate file name.
        validate (std::string inputValue = "SEDfileName");
};
