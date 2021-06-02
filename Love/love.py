from PIL import Image, ImageDraw, ImageFont
font_size = 15
text = "我真的好喜欢你"
img_path = "D:/python_Program/Love/photos//Asuka1.jpg" #待处理的图片路径

#用pillow.Image读取图像，并使用load函数获取到每一个像素值
img_raw = Image.open(img_path)
img_array = img_raw.load()

#新建一张画布，并选择字体样式与大小
img_new = Image.new("RGB", img_raw.size, (0,0,0))
draw = ImageDraw.Draw(img_new)
font = ImageFont.truetype('D:/python_Program/Love/HanyiSentyDiary.ttf', font_size) #字体存在的路径

#循环复制字体
def character_generator(text):
    while True:
        for i in range(len(text)):
            yield text[i]

ch_gen = character_generator(text)

#将字体上色，并铺满整个画布构成新图像
for y in range(0, img_raw.size[1], font_size):
    for x in range(0, img_raw.size[0], font_size):
        draw.text((x, y), next(ch_gen), font=font, fill=img_array[x, y], direction=None)

img_new.convert('RGB').save("D:/python_Program/Love/photos//Asuka1_convert.jpg") #转换后的图片存放地址
