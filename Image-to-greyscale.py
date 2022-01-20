import cv2
import os

#Variables

dir_list = os.listdir(os.getcwd())
img_list = [] #Holds a list of images in dir_list.


def menu_draw():
    img_counter = 0 #Could have used len(img_list) to get the length of the array instead of using this
    
    for object in dir_list: #Iterate to find all files with .jpg extension, append to img_list variable.
        filename, extension = os.path.splitext(object)
          
        if extension == ".jpg":
           img_list.append(object)
    
    for picture in img_list: #Iterate over img_list and create numbered menu.
        img_counter += 1
        menu_num = str(img_counter) + '. '
        print(menu_num + picture)
        
    if img_counter == 0: #Show message and exit if no images present in CWD.
        print("No image files present in CWD") 
        return
    
    menu_select(img_counter) #Call menu_select function, passing the img_counter variable.
    
    
def menu_select(img_count):
                   
    print('*********************************************')

    while True: #While loop that only allows valid input from the user.
        try:
            selection = int(input("Select which image to convert to greyscale: "))
            if selection > img_count or selection <= 0:
                raise ValueError #Purposefully raise an error if the extra conditions are not met.
            break
        except:
            print("That is not a valid option!")
        
            
    img_indexed = img_list[selection - 1] #[selection - 1] to match the index of the list
    new_filename = "greyscale-" + img_indexed 
    
    colour_image = cv2.imread(img_indexed, 0) #Read old colour image
    cv2.imwrite(new_filename, colour_image)   #Write new greyscale  image
    print(f"{new_filename} successfully created!")
    return
        
menu_draw()




