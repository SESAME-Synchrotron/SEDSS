#include "timeFunction.h"
#include "message.h"
#include "file.h"
#include "validate.h"

#include <iostream>

int main(int argc, char const *argv[])
{
	
	CLIMessage cliMsg;
	LogMessage logMsg; 
	SEDFile expFile; 
	validate val; 

	std::cout<<std::endl;
	std::cout<<"################## Log Messages Examples ##################"<<std::endl;

	logMsg.show("This is an information log message", "info");
	logMsg.show("This is a warning log message", "w");
	logMsg.show("This is an error log message", "e");
	logMsg.show("This is a critical log message ", "c");
	
	std::cout<<std::endl;
	std::cout<<"################## CLI Messages Examples ##################"<<std::endl;

	cliMsg.show("This is info CLI Message", "I");
	cliMsg.show("This is worning CLI Message", "W");
	cliMsg.show("This is error CLI Message", "E");
	cliMsg.show("This is critical CLI Message", "C");
	cliMsg.show("This is undefined CLI Message", "U");

	std::cout<<std::endl;
	std::cout<<"################## Time Function Examples ##################"<<std::endl;
	
	std::string timenow {timeFunction(timeFunction::precision::s).getTimeNow()};
	std::cout << "Time now in seconds precistion: " << timenow <<std::endl;
	timenow = timeFunction(timeFunction::precision::mls).getTimeNow();
	std::cout << "Time now in milliseconds: " << timenow <<std::endl;
	timenow = timeFunction(timeFunction::precision::mcs).getTimeNow();
	std::cout << "Time now in microseconds: " << timenow <<std::endl;
	timenow = timeFunction(timeFunction::precision::ns).getTimeNow();
	std::cout << "Time now in nanoseconds: " << timenow <<std::endl;
	timenow = timeFunction(timeFunction::precision::s).getConciseTimeFormat();
	std::cout << "Concise time format: " << timenow <<std::endl;

	std::cout<<std::endl;
	std::cout<<"################## SEDFile ##################"<<std::endl;

	std::string fileName {expFile.getName()};
	std::cout <<fileName<<std::endl;

	std::cout<<std::endl;
	std::cout<<"################## validate ##################"<<std::endl;
	
	std::string filename {"SESAME"};
	bool validFileName {val.valFileName(filename)};
	if (validFileName){
		std::cout<<filename<<" is a valid file name "<<std::endl;
	}
	else{
		std::cout <<filename<< " is not a vilid file name" <<std::endl;
	}
	

	return 0;
}
