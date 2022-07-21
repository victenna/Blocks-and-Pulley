import pygame,sys,time
pygame.init()
screen = pygame.display.set_mode((1000,1000))
screen.fill(pygame.Color(255,0,255))
clock = pygame.time.Clock()
X, Y = 100, 100
X1,Y1=800,100
font1 = pygame.font.SysFont('Corbel',35)
font2 = pygame.font.SysFont('Time Roman',45)

text0= font1.render('Start2' , True , 'black')
text = font1.render('Start1' , True , 'black')
text1 = font1.render('Stop' , True , 'black')
text_m1=pygame.image.load('text_m1.png')
text_m2=pygame.image.load('text_m2.png')
Q=8

img=[0]*Q
rect=[0]*Q
images=['image0.png','image1.png','image2.png','image3.png',\
        'image4.png','image5.png','image6.png','image7.png']
def base(i,scalex,scaley,angle):
    global size
    global s
    img[i]=pygame.image.load(images[i])
    img[i]=pygame.transform.scale(img[i],(scalex,scaley))
    img[i]=pygame.transform.rotate(img[i],angle)
    if i==3 or i==5:s=1/2
    elif i==4 or i==6:s=-1
    elif i==7: s=1/2
    else:s=0
    rect[i]=img[i].get_rect(center=(x[i],y[i]-s*size))
    screen.blit(img[i],rect[i])
delta=0.1
t,i,a,angle=0,0,0,0
b,c=0,0
bg_surface=pygame.image.load('bground.png')
screen.blit(bg_surface,(-1,0))
pygame.display.update()

def functions():
    
    base(0,311,509,0)
    base(1,100,100,angle)
    base(2,614,308,0)
    base(3,50,95,0)
    base(4,50,95,0)
    base(5,50,50,0)
    base(6,50,50,0)
    base(7,100,100,angle)
    

while True:
    pygame.draw.rect(screen,'orange', (X, Y,100,50))
    screen.blit(text,(X+10,Y+5))
    screen.blit(text_m1,(X+10,Y+55))
    pygame.draw.rect(screen,'orange', (X1, Y1,100,50))
    screen.blit(text0,(X1,Y+5))
    screen.blit(text_m2,(X1+10,Y+55))
    mouse=pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()    
        if event.type == pygame.MOUSEBUTTONDOWN:
            if abs(mouse[0] - X)<50 and abs(mouse[1] - Y) <50:
                b=0
                a=a+1
            if  a==2:
                t,i,angle,a,b=0,0,0,0,0

        if event.type == pygame.MOUSEBUTTONDOWN:
            if abs(mouse[0] - X1)<50 and abs(mouse[1] - Y1) <50:
                a=0
                b=b+1
            if  b==2:
                t,i,angle,a,b=0,0,0,0,0

    print('a=',a)
    print('b=',b)
    if a==1:
        b=0
        x,y=[155,500,500,598,454,655,390,596],[699,232,205,880,390,880,390,700]
        screen.fill('violet')
        pygame.draw.rect(screen,'orange', (X, Y,100,50))
        pygame.draw.rect(screen,'orange', (X1, Y,100,50))
        screen.blit(text1,(X,Y+5))
        screen.blit(text0,(X1,Y+5))
        screen.blit(text_m1,(X+10,Y+55))
        t=t+delta
        size=10*(t*t)/2
        angle=angle+size*0.00628
       
        if size>550:
            t,i,angle=0,0,0
            time.sleep(2)
        functions()
        pygame.draw.line(screen,'black',(454,225),(454,350+size),3)
        pygame.draw.line(screen,'black',(548,225),(548,705-size/2),3)
        pygame.draw.line(screen,'black',(645,60),(645,710-size/2),3)
        pygame.draw.line(screen,'black',(597,700-size/2),(597,860-size/2),3)
        
    if b==1:
        a=0
        x,y=[155,500,500,598,454,655,390,596],[699,232,205,530,940,530,940,350]
        screen.fill('violet')
        pygame.draw.rect(screen,'orange', (X, Y,100,50))
        pygame.draw.rect(screen,'orange', (X1, Y,100,50))
        screen.blit(text1,(X1,Y+5))
        screen.blit(text,(X,Y+5))
        screen.blit(text_m2,(X1+10,Y+55))
        t=t+delta
        size=-10*(t*t)/2   
        angle=angle+size*0.00628
        functions()
        pygame.draw.line(screen,'black',(453,225),(453,900+size),3)
        pygame.draw.line(screen,'black',(548,225),(548,355-size/2),3)
        pygame.draw.line(screen,'black',(643,60),(643,360-size/2),3)
        pygame.draw.line(screen,'black',(597,350-size/2),(597,510-size/2),3)
        if size<-600:
            t,i,angle=0,0,0
            time.sleep(2)
    clock.tick(100)
    pygame.display.update()        
       