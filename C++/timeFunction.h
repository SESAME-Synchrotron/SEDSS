#ifndef TIMEFUNCTION_H
#define TIMEFUNCTION_H

#include <string>

// Forward declaration of the timeFunction class

/*
timeFunction is a calss that retrieves the current time as a string in 
the same fomrat "%Y-%m-%d %H:%m:%S" with different precisions: 
	- Seconds 
	- Milliseconds 
	- Microseconds 
	- Nanoseconds
*/ 

class timeFunction {
public:
    /* precision is to retrive time with seconds(s), milliseconds(mls), 
      microseconds (mcs) and nanoseconds (ns) 
    */
    enum class precision {
        s, mls, mcs, ns
    };
    
    precision timePrecision;
    timeFunction(precision prec = precision::s);
    std::string getTimeNow();
};

#endif
