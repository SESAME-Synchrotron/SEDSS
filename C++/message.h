#ifndef MESSAGE
#define MESSAGE 

#include "timeFunction.h"
#include <string>
#include <regex>

#define REGEXCOLORPATTERN "\033\\[[0-9;]*m"

class Message {
    private:
        virtual void show(std::string message, std::string type) = 0;
        std::string infoMsgOptions     [3];
        std::string errorMsgOptions    [3];
        std::string warningMsgOptions  [3];
        std::string criticalMsgOptions [2];

        void initMsgOptions ();        
        std::string toLowerCase (const std::string& str);

    protected: 
        enum messageID {
            I = 1, // information message
		    W = 2, // Warning Message 
		    E = 3, // Error message 
		    C = 4, // Critical	
		    U = 5  // Unknown
            };

        int msgInterpretation();

    public: 
        std::string Msg; 
        std::string Type; 
        Message(std::string Msg, std::string type);
};

class CLIMessage:public Message{
    public:
        CLIMessage(std::string message = "None", std::string type = "U");
        void show(std::string message, std::string type);

};

class LogMessage:public Message {
    private:
        std::regex regexColorPattern{REGEXCOLORPATTERN};
    public:
        timeFunction timeStamp = timeFunction(timeFunction::precision::mcs);
        LogMessage(std::string message = "None", std::string type = "U", bool usefile = false);
        void show(std::string message, std::string type);
        void writeLogs(std::string logFile, std::string messsage);
        std::string logFile{"SEDLogFile.log"};
};

#endif
