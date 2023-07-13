#include "timeFunction.h"
#include <string>

class SEDFile{
    private:

    public:
        std::string fileBaseName; 
        std::string getName (std::string baseName = "defaultFullName");
        std::string checkBaseName (std::string baseName = "defultBaseName");
        SEDFile (std::string filebasename = "defultBaseName");
        void createFile(std::string baseName = "defaultFileName");
};
