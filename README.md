# WebCamSnapShot
A simple security script that catches whoever logs into your computer, written in Python
# Requirements
   * An Android/iOS phone with Pushbullet installed on it
   * A Pushbullet account(You will get API access token from here https://www.pushbullet.com/#settings/account)
   * A working web-cam on you computer
   * A computer with an OS that supports task schedulers (cron, Task Scheduler on Windows, etc...)
   * Python 3.4 or lower (pygame does not support Python 3.5 unfortunately)
   * pygame
   * pushbullet python module
   
   
# How does it work?
Unfortunately, you will have to do some manual work. After setting up the script you will have to set up the script run conditions in your preferred scheduler (cron or Task Scheduler)
# Setup
You will have to grab your API key from Pushbullet website and paste it in designated field. Also, currently the picture that is taken is saved on your desktop in C:\\ partition, following Windows' standard partition naming. Everything from there can be changed to your preference. For now the script sends picture to your first device on pushbullet (most commonly your phone), and that will be changed soon to a more flexible option. Furhter, when you are done with this setup and confirmed that the script is working you have to setup the schedules.
In Task scheduler for Windows, the script General tab should look like this:
![alt tag](http://i.imgur.com/Wkikr90.png)

And your trigger tab should look like this:
![alt tag](http://i.imgur.com/GGagWab.png)

Actions tab:
![alt tag](http://i.imgur.com/7l7zs72.png)

After you save everything, this script should take a picture of whoever logs into your computer
