import time, random, math, datetime
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
            
def test():
    phy_lines = ""
    gray_lines = "#"
    powerups = "#"
    phy_lines, gray_lines = add_image(100, 100, 200, "flower.jpg", phy_lines, gray_lines)
##    phy_lines = "".join([phy_lines, "\n"])
##    gray_lines = "".join([gray_lines, "\n"])
    filename = "Free Rider Tracks/Free Rider track - " + str(time.time()) + ".txt"
    file = open(filename, 'w')
    file.writelines([phy_lines, gray_lines, powerups])
    file.close()

def graphical_function(x):
    return -(400 * math.sin(math.radians(0.1 * x)) - 0.9 * x)
	
def sinusoid():
    #Track variables
    track_length = 10000
    
    #Physic line variables
    trace_length = 30
    start = [-100, 100]
    end = [0, 0]
    
    #Checkpoint variables
    checkpoint_frequency = 3000
    checkpoint_pos = [0, 0]
    
    #Teleport variables
    teleport_start = [start[0], start[1] + 100000]
    
    #Strings
    phy_lines = []
    gray_lines = ["#"]
    powerups = ["#"]
    
    counter = 0
    phy_lines.append(add_line(start[0], start[1], start[0] + 300, start[1]))
    start[0] += 300
    x_pos = 0

    for x in range(0, track_length):
        #Calculate endpoint
        end[0] = x_pos + 200
        end[1] = graphical_function(x_pos) + 100

        #Add line's code to list
        if random.randint(1, 100) <= 0:
            pass
        else:
            phy_lines.append(add_line(start[0], start[1], end[0], end[1]))       

        #Move start point to endpoint
        start[0] = end[0]
        start[1] = end[1]
        
        #Add one to counter
        counter += 1

        #Increase x_pos by trace_length
        x_pos += trace_length
        
        #Add checkpoints to file, if counter is divisible by checkpoint_frequency
        if x_pos % checkpoint_frequency == 0:
            #Calculate checkpoint endpoint
            checkpoint_pos[0] = end[0]
            checkpoint_pos[1] = end[1] - 50
            #Add checkpoint
            powerups.append(add_checkpoint(checkpoint_pos[0], checkpoint_pos[1]))

    #Add star to end of track
    star_pos = [0, 0]
    star_pos[0] = end[0]
    star_pos[1] = end[1] - 50
    powerups.append(encpup(star_pos[0], star_pos[1], 'T'))
    
    #Add teleporter to beginning and end of track
    teleport_end = [end[0], end[1] - 100000]
    powerups.append(encteleport(teleport_start[0], teleport_start[1], teleport_end[0], teleport_end[1]))

    filename = "Free Rider Tracks/Free Rider Track " + str(datetime.datetime.now())[0:19].replace(":", "꞉") + ".txt"
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
    
    file.close()
	
sinusoid()    
    
