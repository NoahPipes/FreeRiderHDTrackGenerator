import time, random, math
##from blink1.blink1 import Blink1
##pygame.init()

def b32e(numbera):
    alphabet = '0123456789abcdefghijklmnopqrstuv'
    number = abs(numbera)
    base32 = ''
    while number:
        number, i = divmod(number, 32)
        base32 = alphabet[int(i)] + base32
    if numbera < 0:
        base32 = '-'+base32
    return base32 or alphabet[0]

def encline(x1, y1, x2, y2):   
    return '%s %s %s %s,' % (b32e(x1),b32e(y1),b32e(x2),b32e(y2))

def encpup(x, y, pupcode):
    #encode powerup without rotation
    return '%s %s %s,' % (pupcode,b32e(x),b32e(y))



def encteleport(x1, y1, x2, y2):
    return 'W %s %s %s %s,' % (b32e(x1),b32e(y1),b32e(x2),b32e(y2))

def add_line(x1, y1, x2, y2):
    return encline(x1, y1, x2, y2)
    
def add_checkpoint(x, y):
    return encpup(x, y, "C")

def add_boost(x, y, rotation):
    return 'B %s %s %s, ' % (b32e(x),b32e(y),b32e(rotation))

##def add_square(x, y, size): 
##    for col in range(0, size):
##        string += add_line(x + col, y, x + col, y + size - 1, string)
##    return string
##
##def scale(image, max_size):
##    image_rect = pygame.Rect(image.get_rect())
##    
##    factor = 0
##    if image_rect.height > image_rect.width:
##        factor = max_size / image_rect.height
##    else:
##        factor = max_size / image_rect.width
##        
##    image = pygame.transform.scale(image, (round(factor*image_rect.width), round(factor*image_rect.height)))
##    return image
##
##def gray(pixel):
##    total = pixel[0] + pixel[1] + pixel[2]
##    return (total/3, total/3, total/3)
##
##def get_color(pixel_color):
##    pixel_gray = gray(pixel_color)[0]
##    if pixel_gray <= 85.33:
##        return "black"
##    elif pixel_gray >= 170.67:
##        return "white"
##    else:
##        return "gray"
##
##def add_image(x, y, max_size, image_name, phy_lines, gray_lines):
##    
##    image = pygame.image.load("Free Rider Images\\" + image_name)
##    image = scale(image, max_size)
##    image_rect = pygame.Rect(image.get_rect())
##
##    size = 5
##
##    for row in range(0, image_rect.height):
##        for col in range(0, image_rect.width):
##            color = get_color(image.get_at((col, row)))
##            x1 = x + col * size
##            y1 = y + row * size
####            x2 = x + col * size + size
####            y2 = y + row
##            if color == "black":
##                phy_lines = add_square(x1, y1, size, phy_lines)
##            elif color == "gray":
##                gray_lines = add_square(x1, y1, size, gray_lines)
##
##    return phy_lines, gray_lines
                
            
def test():
    phy_lines = ""
    gray_lines = "#"
    powerups = "#"
    phy_lines, gray_lines = add_image(100, 100, 200, "flower.jpg", phy_lines, gray_lines)
##    phy_lines = "".join([phy_lines, "\n"])
##    gray_lines = "".join([gray_lines, "\n"])
    filename = "Free Rider Tracks\\Free Rider track - " + str(time.time()) + ".txt"
    file = open(filename, 'w')
    file.writelines([phy_lines, gray_lines, powerups])
    file.close()

    
    

    
def make_track():
##    light = Blink1()

    #Track variables
    track_length = 1000

    #Physic line variables
    line_length = 100
    start = [-100, 100]
    end = [100, -100]

    #Angle variables
    old_angle = 45
    angle_variation = 4

    #Boost variables
    boost_probability = 10
    boost_pos = [0, 0]
    
    #Checkpoint variables
    checkpoint_frequency = 30
    checkpoint_pos = [0, 0]

    #Gray line variables
    density = 1
    distance = 0
    gray_start = [0, 0]
    gray_end = [0, 0]

    #Teleport variables
    teleport_start = [start[0], start[1] + 100000]

    rgb = [0, 0, 0]

    #Strings
    phy_lines = []
    gray_lines = ["#"]
    powerups = ["#"]

    #Angle limits
    upper_limit = 45 #-45
    lower_limit = 60 #22
    going_up = True
    
    counter = 0
    phy_lines.append(add_line(start[0], start[1], start[0] + 300, start[1]))
    start[0] += 300
    for x in range(0, track_length):
##        if random.randint(1, 100) <= 2 and abs(angle - 22) <= angle_variation:
##            going_up = not going_up
##            if going_up == True:
##                upper_limit = -45
##                lower_limit = 22
##            else:
##                upper_limit = 22
##                lower_limit = 90
        
##        if random.randint(1, 10) <= 1:
##            angle_variation = random.randint(1, 90)
        
##            if angle_variation <= 0 :
##                angle_variation = 1
##            elif angle_variation > 30:
##                angle_variation = 30
##            print(angle_variation)
                
        #Change angle of line
        angle = random.randint(-angle_variation, angle_variation) + old_angle
        while angle < upper_limit or angle > lower_limit:
            angle = random.randint(-angle_variation, angle_variation) + old_angle

##        print("Angle: " + str(angle))
    
        #Set old angle to current angle
        old_angle = angle
        
        #Calculate endpoint
        end[0] = start[0] + math.cos(math.radians(angle)) * line_length
        end[1] = start[1] + math.sin(math.radians(angle)) * line_length

        #Add line's code to list
        if random.randint(1, 100) <= 0:
            pass
        else:
            phy_lines.append(add_line(start[0], start[1], end[0], end[1]))
        
##        lines.append(encline(start[0], start[1], end[0], end[1]))

        #Add gray lines' codes to list
        for step in range(0, 1 + int(density * line_length)):
##        for step in range(0, 10):
            distance = step / density
            gray_start = [start[0] + math.cos(math.radians(angle)) * distance, start[1] + math.sin(math.radians(angle)) * distance]
##            gray_end = [gray_start[0], gray_start[1] + 3000]
            gray_end = [gray_start[0] + math.cos(math.radians(90)) * 10000, gray_start[1] + math.sin(math.radians(90)) * 10000]
            gray_lines.append(add_line(gray_start[0], gray_start[1], gray_end[0], gray_end[1]))

        #Move start point to endpoint
        start[0] = end[0]
        start[1] = end[1]
##
##        #Add boost to track randomly
##        if random.randint(0, 100) >= 10:
##            boost_pos[0] = end[0] + math.cos(math.radians(angle - 90)) * 50
##            boost_pos[1] = end[1] + math.sin(math.radians(angle - 90)) * 50
##            strength = random.randint(1, 10)
##            for x in range(0, strength):
##                powerups.append(add_boost(boost_pos[0], boost_pos[1], angle + random.randint(0, 90)))
        
        #Add one to counter
        counter += 1
        
        #Add checkpoints to file, if counter is divisible by checkpoint_frequency
        if counter % checkpoint_frequency == 0:
            #Calculate checkpoint endpoint
            checkpoint_pos[0] = end[0] + math.cos(math.radians(angle - 90)) * 50
            checkpoint_pos[1] = end[1] + math.sin(math.radians(angle - 90)) * 50
            #Add checkpoint
            powerups.append(add_checkpoint(checkpoint_pos[0], checkpoint_pos[1]))

        #Change light's state every 10%
##        if counter % math.floor(track_length / 10) == 0:
##            rgb = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
##            light.fade_to_rgb(0, rgb[0], rgb[1], rgb[2])
##            time.sleep(0.25)

##        if counter % (track_length / 100) == 0:
##            print(str((counter/track_length)*100) + "%")

    #Add star to end of track
    star_pos = [0, 0]
    star_pos[0] = end[0]
    star_pos[1] = end[1] - 50
    powerups.append(encpup(star_pos[0], star_pos[1], 'T'))

    #Add teleporter to beginning and end of track
    teleport_end = [end[0], end[1] - 100000]
    powerups.append(encteleport(teleport_start[0], teleport_start[1], teleport_end[0], teleport_end[1]))

    filename = "Free Rider Tracks\\Free Rider track - " + str(time.time()) + ".txt"
    file = open(filename, 'w')

    print("Creating file")

    for line in phy_lines:
        file.write(line)

    print("Physics lines done")

    for line in gray_lines:
        file.write(line)

    print("Gray lines done")

    for powerup in powerups:
        file.write(powerup)

    print("Powerups done")

##    light.fade_to_rgb(0, 0, 0, 0)
    file.close()

make_track()    
    
