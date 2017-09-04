import time, os, keyboard
from SimpleCV import Image, Camera

captureRate = 0.25
threshold = 4.0
cam = Camera()

while True:
	if keyboard.is_pressed('esc'): 
		break
	else:
		if keyboard.is_pressed('space'):
			screenshot = cam.getImage()
			year = time.strftime("%Y")
			month = time.strftime("%m")
			day = time.strftime("%d")

			#Check for the Year directory
			if os.path.isdir(year) == False:
				os.mkdir(year)

			#Check for the Month directory
			if os.path.isdir("%s/%s" % (year,month)) == False:
				os.mkdir("%s/%s" % (year,month))

			#Check for the Day directory
			if os.path.isdir("%s/%s/%s" % (year,month,day)) == False:
				os.mkdir("%s/%s/%s" % (year,month,day))

			#Set save directory
			saveDir = "%s/%s/%s" % (year,month,day)

			timestr = time.strftime(str(mean))	
			print("Screenshot Taken: %s" % timestr)
			img = cam.getImage()
			timestr = time.strftime("%Y-%m-%d_%H-%M-%S")
			timestrlong = time.strftime("%A %B %d %Y %H:%M:%S")
			img.drawText(str(timestrlong),10,10,color=(255,0,0),fontsize=40)
			img.save("%s/%s.jpg" % (saveDir,timestr))
			f = open('capture.log', 'a')
			timestr = time.strftime("%A %B %d %Y at %H:%M:%S")
			f.write("%s \t Value:%s \t [screenshot] \r\n" % (timestr,mean))
			f.close()
		else:
			previous = cam.getImage()
			time.sleep(captureRate)
			current = cam.getImage()
			diff = current - previous
			matrix = diff.getNumpy()
			mean = matrix.mean()
			if mean >= threshold:
				year = time.strftime("%Y")
				month = time.strftime("%m")
				day = time.strftime("%d")

				#Check for the Year directory
				if os.path.isdir(year) == False:
					os.mkdir(year)

				#Check for the Month directory
				if os.path.isdir("%s/%s" % (year,month)) == False:
					os.mkdir("%s/%s" % (year,month))

				#Check for the Day directory
				if os.path.isdir("%s/%s/%s" % (year,month,day)) == False:
					os.mkdir("%s/%s/%s" % (year,month,day))

				#Set save directory
				saveDir = "%s/%s/%s" % (year,month,day)

				timestr = time.strftime(str(mean))	
				print("Motion Detected: %s" % timestr)
				img = cam.getImage()
				timestr = time.strftime("%Y-%m-%d_%H-%M-%S")
				timestrlong = time.strftime("%A %B %d %Y %H:%M:%S")
				img.drawText(str(timestrlong),10,10,color=(255,0,0),fontsize=40)
				img.save("%s/%s.jpg" % (saveDir,timestr))
				f = open('capture.log', 'a')
				timestr = time.strftime("%A %B %d %Y at %H:%M:%S")
				f.write("%s \t Value:%s \r\n" % (timestr,mean))
				f.close()
