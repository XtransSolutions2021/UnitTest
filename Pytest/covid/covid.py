# import time library
import time

# intialize employee ids
id_database = ["001", "002", "007", "009", "117", "229"]

while True:
    # read the id value
    id_num = input("Enter your Id Number : ")

    if id_num in id_database:  # verify id in database
        body_temp = int(input("Enter your Body Temperature : "))  # Read Temperature and convert it to integer
        pulse = int(input("Enter your pulse value : "))  # Read Pulse and convert it to integer

        # verify the body temp and pulse in the range or not
        if (body_temp > 98 and pulse > 120):
            print("High Temperature and Pulse Alert ....")
            time.sleep(3)
            print("Notification sent to Higher Authorities")

        else:  # If temp and pulse are normal
            print("Your Body Temperature is Normal")
            # read the mask status
            mask_status = input("Please Enter your mask status 0-no mask 1-mask : ")
            # verify the mask status
            if (mask_status == '1'):
                print("Thanks for wearing the mask ")
                # sanitization process
                print("Please wait for sanitization ..... ")
                time.sleep(3)
                print("Sanitization Done")

                # Door Open and close process
                print("Door Open ")
                for i in range(3):
                    print(".........")
                    time.sleep(3)
                print("Door Close ")
            else:  # if mask is not there
                print("Alert! please wear the mask")
    else:  # if no proper id
        print("Please use Proper id otherwise register as Guest")

