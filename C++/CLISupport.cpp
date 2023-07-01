#include <iostream>
#include <ctime>
#include <string>
#include <chrono>
#include <iomanip>
#include <sstream>

#include "timeFunction.h"
#include "message.h"

using std::cout; 
using std::string;
using std::endl; 



class CLIMessage:public Message
{
public:
	CLIMessage(string message = "None", string type = "U"):Message(message, type){

	}
	// ~CLIMessage();

	void show(string message,  string type = "U"){
		Msg = message; 
		Type = type; 

		int interpretedMsg = msgInterpretation (); 

		switch (interpretedMsg){
		case 1:
			cout << "\033[0;32m" << Msg << "\033[0m" << endl;
			break;
		case 2: 
			cout << "\033[0;33m" << Msg << "\033[0m" << endl;
			break;
		case 3:
			cout << "\033[1;31m" << Msg << "\033[0m" << endl;
			break;
		case 4:
			cout << "\033[37;41m" << "Critical:: " << Msg << "\033[0m" << endl;
			break;
		case 5: 
			cout << "\033[1;34m" << Msg << "\033[0m" << endl;
			break;
		}
	}	
};

class LogMessage:public Message
{
public:
   timeFunction timeStamp = timeFunction(timeFunction::precision::mcs);
	LogMessage(string message = "None", string type = "U"):Message(message, type){

	}
	void show(string message,  string type = "U"){
		Msg = message; 
		Type = type; 
		
		int interpretedMsg = msgInterpretation (); 
		switch (interpretedMsg){
		case 1:
			cout << "\033[0;32m" << timeStamp.getTimeNow() <<": "<< Msg << "\033[0m" << endl;
			break;
		case 2: 
			cout << "\033[0;33m" << timeStamp.getTimeNow() <<": "<< Msg << "\033[0m" << endl;
			break;
		case 3:
			cout << "\033[1;31m" << timeStamp.getTimeNow() <<": "<< Msg << "\033[0m" << endl;
			break;
		case 4:
			cout << "\033[37;41m" << timeStamp.getTimeNow() <<": Critical:: " << Msg << "\033[0m" << endl;
			break;
		case 5: 
			cout << "\033[1;34m" << timeStamp.getTimeNow() <<": "<< Msg << "\033[0m" << endl;
			break;
		}
	}	
};


int main(int argc, char const *argv[])
{
	CLIMessage cliMsg;
	LogMessage logMsg; 

	logMsg.show("This is an information log message", "info");
	logMsg.show("This is a warning log message", "w");
	logMsg.show("This is an error log message", "e");
	logMsg.show("This is a critical log message", "c");

	return 0;
}
