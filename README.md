# Project Description:
This project configures a Raspberry Pi + Raspberry Pi Camera Module to work as the input to a Groundlight detector. As a simple demo to build off of, this code configures the camera to take a picture of an office door periodically and use the Groundlight SDK to determine if the door is locked. If the door is unlocked outside of business hours, the Raspberry Pi will send a slack message to some slack channel to notify the relevant people.

## Materials used:
 - Raspberry Pi 4 Model B
 - Raspberry Pi Camera Module 2
 - USB-C power supply
 - Ethernet cable


 ## Step 1: Set up Headless Raspberry Pi


> Note: "Headless" means that you do not need to connect the Raspberry Pi a monitor, keyboard, or mouse. Instead you can access the Pi remotely from your computer via SSH.

1. Insert your Raspberry Pi SD card into your computer, then download and open the [Raspeberry Pi Imager](https://www.raspberrypi.com/software/).
2. Within the Imager, select the OS you want to install (we used Raspberry Pi OS (32-bit)) and select the SD card you want to install it on.
3. Click on the gear icon to open the advanced options and select the "Enable SSH" option. Set a username and password. Close the advanced settings.
4. Click on the "Write" button to start the installation process.
5. Once the installation is complete, eject the SD card from your computer and insert it into the Raspberry Pi.
6. Connect the Raspberry Pi to your network using the Ethernet cable and to power using the USB-C power supply.
7. Wait for the Raspberry Pi to boot up and connect to the network. This may take a few minutes.
8. Find the IP address of the Raspberry Pi. Open terminal on your computer connected to the same network as the Raspberry Pi and run:
```
ping -c 1 raspberrypi.local
```
You should see a response that looks like this. In our case the IP was `10.44.3.5`

```
PING raspberrypi.local (10.44.3.5): 56 data bytes
64 bytes from 10.44.3.5: icmp_seq=0 ttl=64 time=0.458 ms

--- raspberrypi.local ping statistics ---
1 packets transmitted, 1 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 0.458/0.458/0.458/0.000 ms
This will return the IP address of the Raspberry Pi. If this does not work, you can also find the IP address of the Raspberry Pi by logging into your router and looking at the list of connected devices.
```

9.  SSH into the Raspberry Pi using  `ssh <username>@<Raspberry Pi IP address>` where the username and password are the ones you set in step 3. 
10. Once you are logged into the Raspberry Pi, run the following command to update the Raspberry Pi: `sudo apt-get update && sudo apt-get upgrade`

## Step 2: Setup the Camera

1. Follow this [guide](https://www.youtube.com/watch?v=GImeVqHQzsE) to physically connect your Raspberry Pi Camera Module to your Raspberry Pi. 

2. Enable the camera by doing the following on your Raspberry Pi:

	a. `sudo raspi-config` opens a menu for configuring your Raspberry Pi. 

	b. Select `Interface Options`
	
	c. Select `Camera`
	
	d. Select `Yes`
	
	e. Reboot your Raspberry Pi
	

3. Test the camera by running `raspistill -o test.jpg` This will take a picture and save it to the file `test.jpg`. You can `scp` the file to your computer to view it: `scp <username>@<Raspberry Pi IP address>:~/test.jpg`.

## Step 3:  Run Demo
1. Clone this repository to your Raspberry Pi.
2. Install python libraries needed for running the code.
	a. Run `sudo apt-get install python3-picamera` to install the library necessary to interface with the camera.

	b. Run `pip install -r requirements.txt` to install everything else.
	

3. Set environment variables
	a. Set your Groundlight api token (replace `api_example_token` with your actual token):  `export GROUNDLIGHT_API_TOKEN=api_example_token` . You can generate a token by visiting [https://app.groundlight.ai/reef/my-account/api-tokens](https://app.groundlight.ai/reef/my-account/api-tokens).   

	b. (Optional) Set your Slack webhook URL, so the Raspberry Pi can post to Slack when it detects an issue:  `export SLACK_WEBHOOK_URL=https://hooks.slack.com/services/...` . Learn more about setting up a Slack webhook URL [here](https://api.slack.com/messaging/webhooks).
	
4. Run code: `python main.py`.
	