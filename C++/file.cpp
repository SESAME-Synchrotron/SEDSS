# include "file.h"
#include "timeFunction.h"
#include <string>


SEDFile::SEDFile(std::string filebasename){
    SEDFile::fileBaseName = filebasename;
};

std::string SEDFile::getName(){
    timeFunction timeFunc;
    std::string conciseTime {timeFunc.getConciseTimeFormat()};
    std::string fileName = SEDFile::fileBaseName.append("_"+conciseTime);
    return fileName; 
}
