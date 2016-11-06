
from pushbullet import PushBullet

pb = PushBullet('YOUR API_TOKEN')
import datetime

def take_picture(path_):
    import pygame.camera

    pygame.camera.init()
    cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
    cam.start()
    img = cam.get_image()
    pygame.image.save(img, path_)
    pygame.camera.quit()


time = datetime.datetime.now()
import os
acc = os.getlogin()

phone = pb.devices[0]
take_picture('C:\\Users\\' + acc + '\\Desktop\\photo.bmp')

with open('C:\\Users\\' + acc + '\\Desktop\\photo.bmp', "rb") as pic:
    file_data = pb.upload_file(pic, "picture.jpg")

pb.push_note("Log in to account " + acc + " at " + str(time), "", device=phone)

push = pb.push_file(**file_data)
