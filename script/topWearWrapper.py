from source.user import grabcut, userPreprocess 
import cv2
import os
import sys
from source.catalogue import catPreprocess
from source.fit import userFit


# Debug folder provides historical models to be used and segmentation of the apparel
if not os.path.exists('debug/'):
	os.makedirs('debug/')

# Once a user creates the frame for her/himself grabcut is made and fitted to his/her dimensions therefor using the 3rd argument
if sys.argv[3] == "1":
	grabcutOutput = cv2.imread('debug/grabcutOutput.png') 
# If its first time a 3rd argument of 0 is entered to create a frame for pieces of apparel to be fitted to the person
else:
	img = cv2.imread(sys.argv[1])
	grabInst = grabcut(img)
	grabcutOutput = grabInst.grabcut()
	cv2.imwrite("debug/grabcutOutput.png/",grabcutOutput)


processInst = userPreprocess(grabcutOutput)
processInst.cropImg()
processOut = processInst.removeTurds()

processInst.segImage(processOut)
LU, RU = processInst.getSegLines()

leftArmUser = processInst.armSegment(processOut,'left')
rightArmUser = processInst.armSegment(processOut,'right')

catImg = cv2.imread(sys.argv[2])
catInst = catPreprocess(catImg)
floodOut = catInst.edgeDetect()

cropFlood = catInst.cropImg(floodOut)
catInst.segImage(cropFlood)

LC, RC = catInst.getSegLines()


rightArmCat = catInst.armSegment(cropFlood,'right')

leftArmCat = catInst.armSegment(cropFlood,'left')



fitInst = userFit(processOut,cropFlood)
fitInst.setSegLines(LC,RC,LU,RU)

colorUserOut = fitInst.colorUser()


fitInst.setUserArm(leftArmUser,rightArmUser)
fitInst.setCatArm(leftArmCat,rightArmCat)
fitLeft, fitRight = fitInst.sleeveFit()



bodyFitOut = fitInst.bodyFit(colorUserOut)


finalFit = fitInst.finalFit(bodyFitOut,fitLeft,fitRight)



fitInst.setUserBox(processInst.returnUserBox())
output = fitInst.fittingOntoUser(finalFit,cv2.imread(sys.argv[1]))
cv2.imwrite('onUser.jpg',output)
