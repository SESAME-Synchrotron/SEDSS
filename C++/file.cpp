#include "file.h"
#include "timeFunction.h"
#include "validate.h"
#include "message.h"
#include <string>
#include <iostream>
#include <stdexcept>
#include <unistd.h>
#include <fstream>

SEDFile::SEDFile(std::string filebasename){
    SEDFile::fileBaseName = filebasename;
}

std::string SEDFile::getName(std::string baseName){
    /*
    A method used to return full file name with concise time stamp
    that is in compliance with the SED name convention.
    This method: 
    - validate if the base name is in valid syntax by calling checkBaseName. 
    - returns file name, e.g. SEDFileName_20230705T113326
     
    */
   SEDFile::fileBaseName = baseName;
    timeFunction timeFunc;
    SEDFile::checkBaseName(SEDFile::fileBaseName);
    std::string conciseTime {timeFunc.getConciseTimeFormat()};
    std::string fileName = SEDFile::fileBaseName.append("_"+conciseTime);
    return fileName; 
}

std::string SEDFile::checkBaseName(std::string baseName){
    /*
    A method to check whether base name is correct or not. 
    if it is not correct, you will be asked to enter a correct name 
    this method relys on valFileName of validate class which returns 
    whether the base name is in compliance with file name policy or not

    this method returns a compliance file name 
    */
    SEDFile::fileBaseName = baseName;
    std::string checkedFileName = baseName;
    std::string newName; 
    CLIMessage cliMsg; 
    Validate valObj;
    
    if (!valObj.valFileName(baseName)){
        cliMsg.show("Invalid file name, please enter a correct file name", "E");
        std::cin>>newName;
        checkedFileName = SEDFile::checkBaseName(newName);
    }
    return checkedFileName; 
}

void SEDFile::createFile(std::string baseName){
    /*
    A method to create various types of files, e.g. log file, exp. file, etc.
    for DAQ Systems, in order to create the file,The base name must be in 
    compliance with the file name policy
    */

    std::string fileName = baseName;
    CLIMessage cliMsg; 

        // Check if the file exists or not
    if (!access(fileName.c_str(), F_OK) == 0){

        std::ofstream file(fileName);
        // Check if the file can be opened successfully
        if (file.is_open()){
            file.close();
        } else{
            throw std::runtime_error("Unable to create " + fileName + " file.");   // raise error
        }
    } else{
        cliMsg.show("The " + fileName + " is already exists", "I");
    }
}
