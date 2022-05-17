# Sensors-Control
Fetch Robot control



Sean's updates. 

to run qr reader need usb cam package and visp_tracker

#to do
	get usb_cam package
		checkout repo https://github.com/ros-drivers/usb_cam.git
		link to catkin_ws/src	
		cd ..
		catkin_make

	install visp_tracker
		sudo apt-get install ros-melodic-vision-visp
	after install close and re-open teriminal
	
	run the tracker file - this opens the camera. if you have a qr code it will track it
		roslaunch visp_auto_tracker tracklive_usb.launch
	can view to pos data using the topic list or using qr_code_reader.py code
	in new terminal
		rostopic echo /visp_auto_tracker/object_position
	or
		rosrun fetch_follower qr_code_reader.py
	
	i have also intergrated the rossubscriber to tes_motion. But this is only very basic. It 
	should just check if x > 0.1 and if so move the robot. 	
	
	the rostopic echo has better info. the one i wrote was just for testing.
	
	
