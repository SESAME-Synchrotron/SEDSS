#include "timeFunction.h"
#include <string>

class SEDFile{
    private:
        
    public:
        std::string fileBaseName; 
        std::string getName ();
        SEDFile (std::string filebasename = "logFile");  
};
