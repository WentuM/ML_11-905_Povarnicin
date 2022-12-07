import random
import pygame as pg
from PIL import Image
import pytesseract

pg.init()
sc = pg.display.set_mode((400, 300))
WHITE = (255, 255, 255)
BLACK = (0,0,0)
sc.fill(WHITE)
pg.display.update()
f1 = pg.font.Font(None, 36)

play = True
while play:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            pg.quit()
            play = False
        if i.type == pg.MOUSEBUTTONDOWN:
            if i.button == 3:
                pg.image.save(sc, 'picture.jpg')
                image = Image.open('picture.jpg')
                print(pytesseract.image_to_string(image, lang='eng',config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789'))
                # dog_surf = pg.image.load('picture.png')
                # img = mpimg.imread('picture.png')[..., 1]
                # img = cv2.resize(img, dsize=(28, 28))
                # img = np.array(img).reshape(1, 28,28,1)
                #
                # pred = model.predict(img)
                # pred = np.argmax(pred, axis=1)[0]
                # text1 = f1.render('Предсказанная цифра: {0}'.format(pred), True, BLACK)
                # sc.blit(text1, (10, 10))
                # pg.display.update()
            if i.button == 2:
                sc.fill(WHITE)
                pg.display.update()
    if play:
        airbrush = True
        cur = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        if click[0] == True:
            pg.draw.circle(sc, BLACK, (cur[0] + random.randrange(2), cur[1] + random.randrange(2)), random.randrange(1, 5))
        pg.display.update()