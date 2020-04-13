# Clothing Companion

Online shopping is a stressful and time-consuming task. Buying the right size and clothing item
requires a lot of judgment and adjustments. The current online shopping experience is amazing,
but often leads to several unsatisfied customers.

Clothing Companion is an innovative approach to online shopping. It allows the user to see
how they look in a certain clothing item, make sure they have the right size and are satisfied with
the final product when received.

Users can pick a few clothing items they would like to purchase, with the augmented reality
technology integrated into the system, visually see how they look in the chosen item and improve
their online shopping experience. Leading to more satisfied customers. The solution uses image
processing and augmented reality to map a piece of clothing onto a user. We were able to get an
image mapped onto a photo taken by a user. This has the practical use of helping ecommerce
clothing websites show their user’s how the clothing item would fit on them.

This is the source code for the project we built. Due to lack of time and unfortunate circumstances we were not able to connect our back end and front end. However, here are both the components of our project and how we would want it to look and function.

## Front End

We tested a lot of designs of our front end before we started developing the actual website. Most of our front end focuses more on the aspect of uploading an image and mapping a piece of clothing onto that image. We also created a front end that mimics a e-commerce website to show how it would integrate.

Here are the final designs we had come up with:

#### Proposed Front End Design Images

1. Single item page

![user image](/03_item_page.png)

2. Upload an image

![user image](/04_Upload_Image.png)

![user image](/06_Upload_Image%20Complete.png)

3. Shown image

![user image](/07_Shown_image.png)

This is how we wanted out frontend to look. Due to the shortage of time and unfortunate occurance of events we were not able to complete it.

## Script

This is the script for clothing companion. Due to schedule and coronavirus the script there has been heavily modified many times and inspirations have been taken from other sources. We truly believe that this project has great potential and future and given enough resources and time, a well-crafted product can be achieved. As the project requires us to make a final deliverable, this is our take at the project given the situation we are faced with.

1. A user uploads an image like so,

![user image](/script/input.jpg)

An item of clothing like below,

![apparel image](/script/apparel.jpg)

2. The output would look like below,

![output image](/script/onUser.jpg)

#### Requirements

The code requires `python 2.7`, `opencv` and `numpy` to run.

#### Usage

There are limitations and presumptions that are made before using this project, therefore it is recommended to use the example pictures as a guideline until further refineries are made to the code.

For extracting the outline of the topwear worn by the user from the user image, we used grabcut foreground segmentation, specifically the code sample provided by opencv.

To fit a tshirt on a user image, use the `topWearWrapper.py` script. To execute 

```
$ python topWearWrapper.py [path to user image] [path to apparel image] 1
```

Follow the easy steps on the terminal to achieve your desired outcome. The image below represents the mask generated for the input image above. 

![grabcut output](/script/debug/grabcutOutput.png)

Once the user has achieved masking through the script, a grabcut will be saved as a reference in the debug folder and now the user can run the script with the third argument being 0 and not having to go through the entire process again.










