import sys
import pygame
import pygame.camera

# vcgencmd get_camera
print("run: sudo modprobe bcm2835-v4l2")

pygame.init()
pygame.camera.init()

screen = pygame.display.set_mode((640,480),0)
cam_list = pygame.camera.list_cameras()
print(cam_list)
cam_left = pygame.camera.Camera(cam_list[1],(320,480))
cam_right= pygame.camera.Camera(cam_list[0],(320,480))

cam_left.start()
cam_right.start()

while True:
   image_left = cam_left.get_image()
   image_left = pygame.transform.scale(image_left,(320,480))
   screen.blit(image_left,(0,0))

   image_right = cam_right.get_image()
   image_right = pygame.transform.scale(image_right,(320,480))
   screen.blit(image_right,(320,0))

	
   pygame.display.update()

   for event in pygame.event.get():
          if event.type == pygame.QUIT:
                  cam.stop()
                  pygame.quit()
                  sys.exit()
               
