// header guard
#ifndef TIMEFUNCTION_H 
#define TIMEFUNCTION_H 

#include <string>

/*
timeFunction is a calss that retrieves the current time as a string in 
the same fomrat "%Y-%m-%d %H:%m:%S" with different precisions: 
	- Seconds 
	- Milliseconds 
	- Microseconds 
	- Nanoseconds
*/ 

// Forward declaration of the timeFunction class

class timeFunction {
private:
    const char timeFormat[18]= "%Y-%m-%d %H:%M:%S";
public:
    /* precision is to retrive time with seconds(s), milliseconds(mls), 
      microseconds (mcs) and nanoseconds (ns) 
    */
    enum class precision {
        s, mls, mcs, ns
    };
    
    precision timePrecision;
    timeFunction(precision prec = precision::s); //constructor declaration 
    std::string getTimeNow();
};

#endif
