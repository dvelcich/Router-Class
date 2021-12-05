#create a router class

#kwh = (W * H)/1000

import time


class Router:
    # actual price is much much lower but due to such a short download time price was increased to give a visible cost value
    cost_kwh = 1000
   
   #initialize class, take 3 arguments and set them to private variables
    def __init__(self,upload_mb,download_mb,watts):
            try:
                self.__upload = float(upload_mb)
            #make sure argument is a number
            except ValueError:
                print("Upload Speed Error: Please enter a number")
            try:
                self.__download = float(download_mb)
            #make sure argument is a number
            except ValueError:
                print("Download Speed Error: Please enter a number")
            try:
                self.__watts = float(watts)
            #make sure argument is a number
            except ValueError:
                print("Router Watts Error: Please enter a number")

    #returns the upload speed of object
    def get_upload(self):
        return self.__upload

    #retuns download speef of objects
    def get_download(self):
        return self.__download

    #returns wattage of object
    def get_watts(self):
        return self.__watts

    #set upload speed of object
    def set_upload(self,value):
        while True:
            try:
                self.__upload = float(value)
                break
            #make sure argument is a number
            except ValueError:
                print("Error: Please enter a number")

    #set download speed of object
    def set_download(self,value):
        while True:
            try:
                self.__download = float(value)
                break
            #make sure argument is a number
            except ValueError:
                print("Error: Please enter a number")

    #set wattage of object
    def set_watts(self,value):
        while True:
            try:
                self.__watts = float(value)
                break
            #make sure argument is a number
            except ValueError:
                print("Error: Please enter a number")

    #get a rounded percentage of how complete a download is at a given time
    def get_download_progress(self,size_gb,time_min):
        #convert min into sec and multiply by mb/s to get mb downloaded
        progress = 60 * float(time_min) * self.__download
        #convert mb to gb
        progress = progress/1000
        #compare progress to the goal
        percent = (progress/float(size_gb))*100
        #return rounded percent
        return int(percent)
    
    #get a rounded percentage of how complete a download is at a given time
    def get_upload_progress(self,size_gb,time_min):
        #convert min into sec and multiply by mb/s to get mb downloaded
        progress = 60 * float(time_min) * self.__upload
        #convert mb to gb
        progress = progress/1000
        #compare progress to the goal
        percent = (progress/float(size_gb))*100
        #return rounded percent
        return int(percent)

    #get the size of what has been downloaded in a given time
    def get_download_size(self,time_min):
        #multiply minutes to get seconds and convert mb/s to mb
        progress = 60 * float(time_min) * self.__download
        #convert mb t0 gb
        progress = progress/1000
        #return the size of whats been downloaded so far
        return progress

    #get size of current download at a specific time
    def get_upload_size(self,time_min):
        #min to sec and then mb/s to mb
        progress = 60 * float(time_min) * self.__upload
        #convert mb to gb
        progress = progress/1000
        #return current download
        return progress

    #returns the time it would take in min to download a file of said size
    def get_download_time(self,size_gb):
        #convert mb/s to gb/m and divide the size of file by rate of download
        return float(size_gb)/((self.__download/1000)*60)

    #returns the time it would take in min to download a file of said size
    def get_upload_time(self,size_gb):
        #convert mb/s to gb/m and divide the size of file by rate of upload
        return float(size_gb)/((self.__upload/1000)*60)

    #returns the estimated cost of downloading a file of said size
    def get_download_cost(self,size_gb):
        #find how long it would take to download file in hours and then using watts find kwh and multiply by the cost per kwh
        cost = ((self.get_download_time(size_gb) / 60) * self.get_watts()) / 1000 * Router.cost_kwh
        #add $ and round down to 2 decimal points
        cost = f"${float(cost):.2f}"
        return cost

    #returns the estimated cost of uploading a file of said size
    def get_upload_cost(self,size_gb):
        #find how long it would take to upload file in hours and then using watts find kwh and multiply by the cost per kwh
        cost = ((self.get_upload_time(size_gb) / 60) * self.get_watts())/ 1000 * Router.cost_kwh
        #add $ and round down to 2 decimal points
        cost = f"${float(cost):.2f}"
        return cost

def main():
    #create objects
    xfinity = Router(13,34,90)
    monkeybrains = Router(18,42,100)
    #designate size of file
    size_gb = 65
    #to start counter
    n = 1
    #starting message
    print("Lets begin the race. Xfinty (Hari's Wifi) vs MonkeyBrains (Diego's Wifi).")
    print(f"They'll be racing to download a {size_gb} Gigabyte app. We'll check in on their progress every 5 minutes.")
    #make a loop
    while True:
        #gives it pause
        time.sleep(1.5)
        #if the download progress is past 100%  instead print the time it takes to download the file and its estimated cost
        if xfinity.get_download_progress(size_gb,(5*n)) >= 100:
            print(f"\nXfinity completed the download first! It downloaded in {xfinity.get_download_time(size_gb)} min.")
            print(f"This download would cost roughly {xfinity.get_download_cost(size_gb)}.")
            #exit loop
            break
        #if the download progress is past 100%  instead print the time it takes to download the file and its estimated cost
        elif monkeybrains.get_download_progress(size_gb,(5*n)) >= 100:
            print(f"\nMonkeyBrains completed the download first! It downloaded in {monkeybrains.get_download_time(size_gb)} min.")
            print(f"This download would cost roughly {monkeybrains.get_download_cost(size_gb)}.")
            #exit loop
            break
        else:
            #print the progress of both objects and add 1 to the counter to increase the time
            print("\nTime to check in lets look at the progress")
            print(f"Xfinity progress: {xfinity.get_download_size(5*n)} gb out of {size_gb} gb. Download {xfinity.get_download_progress(size_gb,(5*n))}% complete.")
            print(f"MonkeyBrains progress: {monkeybrains.get_download_size(5*n)} gb out of {size_gb} gb. Download {monkeybrains.get_download_progress(size_gb,(5*n))}% complete.")
            n += 1

if __name__ == "__main__":
    main()
