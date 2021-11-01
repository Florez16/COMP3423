# NG NG Kwan Lam 19056505d
# COMP3423 Assignment 3

class Camera:

    def __init__(self):
        self.playback_mode_on = False
        self.shooting_mode_on = True
        self.camera_on = False
        self.sleep_mode_on = False
        self.photos_taken = 0
        self.current_playback_display_id = 0

        # For playback mode cycling through photos
        self.previous_mode_shooting = False     # False = Playback, True = Shooting

        # For filter mode
        self.filter_list = ["No filter", "Monochromatic", "Vintage", "Starry"]
        self.current_filter_code = 0



    def get_no_of_photos_taken(self):
        """
        This method returns the number of photos taken.

        Input: None
        Output: Number of photos taken 
        """

        print(f"\nNumber of photos taken: {self.photos_taken}\n")


    def get_current_mode(self): # DONE
        """
        This method returns the current mode of the camera (on shooting mode or playback mode).

        Input: None
        Output: 
            1) The camera is on playback or shooting mode
            2) The camera is now awake or in sleep mode
        """
        if self.playback_mode_on:
            print("Now on playback mode.")
        else:
            print("Now on shooting mode.")

        
        if self.sleep_mode_on:
            print("Now on sleep mode.\n")
        else:
            print("Now awake.\n")


    def take_photo(self):   
        """
        This method simulates the user taking a photograph

        Input: None
        Output: None
        """

        
        print("\tTaking a photo now.")
        self.photos_taken += 1



    def switch_from_playback_to_shooting(self):     
        """
        This method switches the camera mode from playback mode to shooting mode

        Input: None
        Output: None
        """
        self.playback_mode_on = False
        self.shooting_mode_on = True
        
        self.previous_mode_shooting = False     # Indicate that the previous mode is playback mode

        print("Playback mode OFF, Shooting mode ON.")


    def switch_from_shooting_to_playback(self):     # DONE
        """
        This method switches the camera mode from shooting mode to playback mode

        Input: None
        Output: None
        """
        self.shooting_mode_on = False
        self.playback_mode_on = True

        self.previous_mode_shooting = True      # Indicate that the previous mode is shooting mode
        self.current_playback_display_id = 0    # reset the playback photo ID to 0 (such that the user will start viewing the photo from ID 1 when they press the playback button)

        print("Shooting mode OFF, Playback mode ON.")


    def display_most_recent_photo(self):
        """
        This method displays the most recent photo.
        Input: None
        Output: The most recent photo and its ID
        """

        print(f"\tDisplaying the most recent photo (ID: {self.photos_taken})")


    def display_photo(self, ID):    
        """
        This method displays a particular photo.

        Input ID: the ID of the photo to be displayed
        Output: The photo with the given ID
        """

        print(f"\tDisplaying photo ID: {ID}")




    def press_shutter_button(self):     #DONE
        """
        This method simulates the user pressing the shutter button

        Input: None
        Output: None
        """

        if self.camera_on:                              # If the camera is turned ON
            print("\nShutter button pressed.")
            if self.sleep_mode_on:  # if the camera is on sleep mode
                self.camera_wake()  # wake up the camera
                return              # do not execute the lines below


            if self.shooting_mode_on:                   # If the user is currently on shooting mode
                self.take_photo()                       # Take a photo
            else:                                       # If the user is currently on playback mode 
                self.switch_from_playback_to_shooting() # Switch the camera to shooting mode


    def press_playback_button(self):
        """
        This method simulates the user pressing the playback button

        Input: None
        Output: None
        """

        if self.camera_on:  # if the camera is turned on

            print("\nPlayback button pressed.")

            if self.sleep_mode_on:  # if the camera is on sleep mode
                self.camera_wake()  # wake up the camera
                return              # do not execute the lines below


            if self.shooting_mode_on:   # if the user is currently on shooting mode
                self.switch_from_shooting_to_playback() # enter playback mode

                if self.photos_taken == 0:  # if there is no photos being taken yet
                    print("\tNo picture")     # show notification saying "No picture"
                else:                       # if at least one picture is already being taken
                    self.display_most_recent_photo()    # display the most recent photo

            else:                       # if the user is currently on playback mode
                
                self.current_playback_display_id += 1
                self.display_photo(self.current_playback_display_id)

                #self.display_next_photo()    # display the next photo (NEED CURRENT PHOTO ID OR NOT?)


    def slide_power_switch_to_on(self):
        """
        This method simulates the user sliding the power switch to ON

        Input: None
        Output: None
        """
        self.camera_on = True   # turn the camera on
        self.switch_from_playback_to_shooting() # enter shooting mode while disabling playback mode
        print("The camera is now turned on.")


    def slide_power_switch_to_off(self):
        """
        This method simulates the user sliding the power switch to OFF

        Input: None
        Output: None
        """
        self.camera_on = False
        print("The camera is now turned off.")


    def camera_sleep(self):
        """
        This method sets the camera to SLEEP mode

        Input: None
        Output: None
        """
        self.sleep_mode_on = True


    def camera_wake(self):
        """
        This method wakes the camera up

        Input: None
        Output: None
        """
        self.sleep_mode_on = False


    def check_camera_idle(self):
        """
        This method simulates that no operations has been done to the camera for 3 minutes

        Input: None
        Outout: None
        """

        # Note that here the idle status is not automatically detected but manually set for testing purposes

        idle_status = input("Set idle status (T/F): ")  # Input either "T" or "F"
        if idle_status == "T":
            self.camera_sleep()
        else:
            pass
        


    def press_filter_button(self):  # DONE
        """
        This method simulates the user pressing the filter button

        Input: None
        Output: None
        """


        if self.camera_on:  # The camera is turned ON
            print("\nFilter button pressed.")
            if self.sleep_mode_on:  # if the camera is on sleep mode
                self.camera_wake()  # wake up the camera
                return              # do not execute the lines below
            
            if self.shooting_mode_on:   # The camera is now on shooting mode
                # Switch to the next mode (No filter -> Monochromatic, Monochromatic -> Vintage, Vintage -> Starry, Starry -> None)
                self.current_filter_code += 1
                if self.current_filter_code == 4:  
                    self.current_filter_code = 0

                print(f"\tCurrent Filter Mode: {self.filter_list[self.current_filter_code]}\n") # Displays the current filter mode

            else:   # The camera is now on playback mode
                return    # No effect at all



# The lines below are for testing

cam = Camera()

cam.slide_power_switch_to_on()  # turn on the camera


"""Test shutter button"""
# now on shooting mode
cam.press_shutter_button()  # take 1 photo
cam.press_shutter_button()  # take 1 photo
cam.press_shutter_button()  # take 1 photo


cam.press_playback_button() # go to playback mode
cam.press_shutter_button()  # go back to shooting mode
cam.press_shutter_button()  # take 1 photo

cam.get_no_of_photos_taken()    # 4 photos have been taken


"""Test playback button"""
cam.press_playback_button() # go to playback mode, should display photo ID: 4
cam.press_playback_button() # display photo ID: 1
cam.press_playback_button() # display photo ID: 2
cam.press_playback_button() # display photo ID: 3

cam.press_shutter_button()  # go to shooting mode
cam.press_playback_button() # go to playback mode, should display photo ID: 4

cam.press_playback_button() # display photo ID: 1
cam.press_playback_button() # display photo ID: 2
cam.press_playback_button() # display photo ID: 3
cam.press_playback_button() # display photo ID: 4



"""Test Sleep mode"""
cam.check_camera_idle() # indicate the camera is idle for 3 minutes (input "T")
cam.press_shutter_button()  # press the shutter button to wake the camera up

cam.get_current_mode()      # camera is now awake and on playback mode
cam.press_shutter_button()  # go to shooting mode (this proves that the camera is awake now and can function normally)


"""Test filter button"""
cam.press_filter_button()   # now on Monochromatic
cam.press_filter_button()   # now on Vintage
cam.press_filter_button()   # now on Starry
cam.press_filter_button()   # now on No filter



"""Test power switch"""
cam.slide_power_switch_to_off()
print(f"\nCamera ON? {cam.camera_on}")
