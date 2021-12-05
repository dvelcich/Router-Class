Router Class:
        The router class is a class that takes in 3 arguments and creates a unique router object. This object has the attributes of download and upload speed as well as watts. The point of the class is to represent a router in numerical form allowing for comparisons between multiple router objects. It also contains methods which can be used to find how long a download/upload would take or how much a download would cost via your electric bill.


Class Variables
        cost_kwh : The cost of 1 kwh of electricity. Used to calculate the total cost of downloading/uploading.


Data Variables
        self.__upload : The rate in mb/s of which the router can upload data.


        self.__download : The rate in mb/s of which the router can download data.


        self.__watts : The wattage of the router. Used to find cost.
Methods
        get_upload() : Method takes no arguments; returns value of self.__upload.


        get_download() : Method takes no arguments; returns value of self.__downlaod.


        get_watts() : Method takes no arguments; returns value of self.__watts.


        set_upload() : Method takes one argument in number form and sets it to the value of self.__upload.


        set_download() : Method takes one argument in number form and sets it to the value of self.__download.


        set_watts() : Method takes one argument in number form and sets it to the value of self.__watts.


        get_upload_progress() : Method takes two arguments, the first is the size of the file being uploaded in gb. The second is the time in minutes of how long the upload has been happening. Method returns a rounded percentage of how complete the upload is.


        get_download_progress() : Method takes two arguments, the first is the size of the file being downloaded in gb. The second is the time in minutes of how long the download has been happening. Method returns a rounded percentage of how complete the download is.


get_upload_size() : Method takes one argument, time in minutes, and returns how much data the router uploads in that time in gb.


        get_download_size() : Method takes one argument, time in minutes, and returns how much data the router downloads in that time in gb.


        get_upload_time() : Method takes one numeric argument, size of a file in gb. The method then returns the amount of time in minutes it would take the router to upload said file.


        get_download_time() : Method takes one numeric argument, size of a file in gb. The method then returns the amount of time in minutes it would take the router to download said file.


        get_upload_cost() : Method takes one argument, the size of the file in gb. It returns the estimated cost of uploading the file in string format.


        get_download_cost() : Method takes one argument, the size of the file in gb. It returns the estimated cost of downloading the file in string format.




DEMO DESCRIPTION:


The demo program creates two objects xfinity and monkeybrains. These two objects are then placed against each other to see which can download a file the fastest. The progress of each router is periodically displayed until a winner is decided. Then the estimated cost of the winner's download is calculated and shown as well.


DEMO INSTRUCTIONS:


Download the routers.py file and place it in a location of your choice, then maneuver to said location in the terminal and type ‘python3 routers.py’. This will run the function and the results will be printed in the terminal.