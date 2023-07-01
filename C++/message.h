#ifndef MESSAGE
#define MESSAGE 

#include <string>

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
		    W = 2, // Worning Message 
		    E = 3, // Error message 
		    C = 4, // Critical	
		    U = 5  // Unknown
            };

        int msgInterpretation();

    public: 
        std::string Msg; 
        std::string Type; 
        Message(std::string, std::string type);
};
#endif 
