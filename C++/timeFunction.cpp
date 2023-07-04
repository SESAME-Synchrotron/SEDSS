#include "timeFunction.h"
#include <chrono>
#include <ctime>
#include <iomanip>
#include <sstream>

// timeFunction class constructor definition 
timeFunction::timeFunction(precision prec):timePrecision(prec) {
  // timeFunction::timePrecision = prec; --> reblaced by the above initializer 
} 

std::string timeFunction::getTimeNow() {
    /* chrono::system_clock::now() is a function returns time as a 
        chrono::system_clock::time_point object since epoch start couting 
        time. 
        chrono::system_clock::to_time_t is used to convert time_point to 
        a calendar time. 
        std::stringstream is a func allows you reading and writing from a 
        string. It helps a lot converting between diffrent formats. 
        std::localtime: Converts given time since epoch as std::time_t value
         into calendar time, expressed in local time.
         std::put_time: inserts formated time value to an output stream. 
        */
    auto currentTime = std::chrono::system_clock::now();
    auto calTime = std::chrono::system_clock::to_time_t(currentTime);
    std::stringstream ss;

    switch (timePrecision) {
        case precision::s: {
            ss << std::put_time(std::localtime(&calTime), timeFormat);
            break;
        }
        case precision::mls: {
            auto highResTimeMls = std::chrono::duration_cast<std::chrono::milliseconds>(currentTime.time_since_epoch()) % 1000;
            ss << std::put_time(std::localtime(&calTime), timeFormat) << "." << highResTimeMls.count();
            break;
        }
        case precision::mcs: {
            auto highResTimeMcs = std::chrono::duration_cast<std::chrono::microseconds>(currentTime.time_since_epoch()) % 1000000;
            ss << std::put_time(std::localtime(&calTime), timeFormat) << "." << highResTimeMcs.count();
            break;
        }
        case precision::ns: {
            auto highResTimeNs = std::chrono::duration_cast<std::chrono::nanoseconds>(currentTime.time_since_epoch()) % 1000000000;
            ss << std::put_time(std::localtime(&calTime), timeFormat) << "." << highResTimeNs.count();
            break;
        }
    }

    return ss.str();
}

std::string timeFunction::getConciseTimeFormat(){
    /*
    This is a method to return the current time in compliance with 
    IOS 8601 (concise and unambiguous) that can be used as a part of the 
    file name.
    */
    auto currentTime = std::chrono::system_clock::now();
    auto calTime = std::chrono::system_clock::to_time_t(currentTime);
    std::stringstream ss;
    ss << std::put_time(std::localtime(&calTime), conciseTimeFormat);
    return ss.str();
}
