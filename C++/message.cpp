#include "message.h"

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
