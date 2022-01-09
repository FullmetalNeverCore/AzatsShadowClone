import pyautogui as pt 
import time 

class Azats_Vision:
    def locate_image_on_screen(image_name):
        imgloc = pt.locateOnScreen(image_name,grayscale=True,confidence=0.7)
        print("Seraching for pokemon...")
        if imgloc is None:
            print("Pokemon not found")
            return False
        else:
            print(type(imgloc)) if imgloc != None else None 
            Azats_Vision.screenshot_a_window(imgloc) if imgloc != None else print("No image found")
            return True

    def screenshot_a_window(screens_coords):
        pt.screenshot('leg.png',region=(screens_coords.left,screens_coords.top,screens_coords.width + 680,screens_coords.height+100))
        return True

    def test_location():
        imgloc = pt.locateOnScreen('zdn.png',grayscale=True,confidence=0.8)
        print(type(imgloc)) if imgloc != None else None 
        print(imgloc.left) if imgloc != None else None 
        Azats_Vision.screenshot_a_window(imgloc) if imgloc != None else print("No image found")

if __name__ == "__main__":
    while True:
        time.sleep(1)
        Azats_Vision.test_location()
