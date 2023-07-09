#include "message.h"
#include <iostream>
#include <algorithm>
#include <cctype>
#include <fstream>
#include <stdexcept>
#include <unistd.h>
#include <regex>

void Message::initMsgOptions()
{
    infoMsgOptions[0]     = "i";
    infoMsgOptions[1]     = "info";
    infoMsgOptions[2]     = "information";
    errorMsgOptions[0]    = "e";
    errorMsgOptions[1]    = "err";
    errorMsgOptions[2]    = "error";
    warningMsgOptions[0]  = "w";
    warningMsgOptions[1]  = "war";
    warningMsgOptions[2]  = "warning";
    criticalMsgOptions[0] = "c";
    criticalMsgOptions[1] = "critical";
}

std::string Message::toLowerCase(const std::string& str)
{
    std::string lowercase_str = str;
    // Create a copy of the string and convert all characters to lowercase
    std::transform(lowercase_str.begin(), lowercase_str.end(), lowercase_str.begin(), ::tolower);
    return lowercase_str;
}

int Message::msgInterpretation()
{
    bool found = false;
    messageID var_messageID;
    if (std::find(std::begin(infoMsgOptions), std::end(infoMsgOptions), toLowerCase(Type)) != std::end(infoMsgOptions)){
        found = true;
        var_messageID = I;
        }
    else if (std::find(std::begin(warningMsgOptions), std::end(warningMsgOptions), toLowerCase(Type)) != std::end(warningMsgOptions)){
        found = true;
        var_messageID = W;
    }
    else if (std::find(std::begin(errorMsgOptions), std::end(errorMsgOptions), toLowerCase(Type)) != std::end(errorMsgOptions)){
        found = true;
        var_messageID = E;
    }
    else if (std::find(std::begin(criticalMsgOptions), std::end(criticalMsgOptions), toLowerCase(Type)) != std::end(criticalMsgOptions)){
        found = true;
        var_messageID = C;
    }
    else{
        var_messageID = U;
    }

    return var_messageID;
}

//Message Constructor
Message::Message(std::string message, std::string type)
{
    Msg = message;
    Type = type;
    initMsgOptions();
    msgInterpretation();
}

CLIMessage::CLIMessage(std::string message, std::string type):Message(message, type){};

void CLIMessage::show(std::string message, std::string type = "U"){
    Message::Msg = message; 
    Message::Type = type; 

    int interpretedMsg = Message::msgInterpretation (); 
    switch (interpretedMsg){
		case 1:
			std::cout << "\033[0;32m" << Message::Msg << "\033[0m" << std::endl;
			break;
		case 2: 
			std::cout << "\033[0;33m" << Message::Msg << "\033[0m" << std::endl;
			break;
		case 3:
			std::cout << "\033[1;31m" << Message::Msg << "\033[0m" << std::endl;
			break;
		case 4:
			std::cout << "\033[37;41m" << "Critical:: " << Message::Msg << "\033[0m" << std::endl;
			break;
		case 5: 
			std::cout << "\033[1;34m" << Message::Msg << "\033[0m" << std::endl;
			break;
		}
}

LogMessage::LogMessage(std::string message, std::string type, bool usefile):Message(message, type){
    // bool useFile = usefile;
};

void LogMessage::show(std::string message, std::string type = "U"){
    Message::Msg = message;
    Message::Type = type; 

    std::string logMsg;
    
    int interpretedMsg = msgInterpretation (); 
		switch (interpretedMsg){
		case 1:
            logMsg = timeStamp.getTimeNow() + ": Information:: " + Msg;
			std::cout << "\033[0;32m" <<  logMsg << "\033[0m" << std::endl;
			break;
		case 2: 
            logMsg = timeStamp.getTimeNow() + ": Warning:: " + Msg;
			std::cout << "\033[0;33m" << logMsg << "\033[0m" << std::endl;
			break;
		case 3:
            logMsg = timeStamp.getTimeNow() + ": Error:: " + Msg;
			std::cout << "\033[1;31m" << logMsg << "\033[0m" << std::endl;
			break;
		case 4:
            logMsg = timeStamp.getTimeNow() + ": Critical:: " + Msg;
			std::cout << "\033[37;41m" << logMsg << "\033[0m" << std::endl;
			break;
		case 5: 
            logMsg = timeStamp.getTimeNow() + ": " + Msg;
			std::cout << "\033[1;34m" << logMsg << "\033[0m" << std::endl;
			break;
		}
        writeLogs(logMsg);
}

void LogMessage::setupLogFile(){

    // Check if the file exists or not
    if (!access(logFileName.c_str(), F_OK) == 0){

        std::ofstream logFile(logFileName);
        // Check if the file can be opened successfully
        if (logFile.is_open()){
            logFile.close();
        } else{
            throw std::runtime_error("Unable to create log file.");   // raise error
        }
    } else{
        std::cout << "The log file is already exists." << std::endl;
    }
}

void LogMessage::writeLogs(std::string message){

    std::string Msg = message;
    std::regex colorPattern("\033\\[[0-9;]*m");     // regex to remove the color pattern
    std::string logWithoutColor = std::regex_replace(Msg, colorPattern, "");

    std::ofstream logFile(logFileName, std::ios::app);  // Open the file in append mode
    logFile << logWithoutColor << "\n";
    logFile.close();
}
