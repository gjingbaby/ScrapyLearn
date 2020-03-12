
'''
PIL年久失修，pillow基于PIL，支持3.x
安装pillow，引用时引用PIL
以下内容为生成验证码
'''

from PIL import Image,ImageFilter,ImageDraw,ImageFont

#测试
im = Image.open(r"E:\pyworkspace\ScrapyLearn\spring.jpg")
w,h = im.size

im2 = im.filter(ImageFilter.BLUR)
im2.save("blur.jpg",'jpeg')

#以下内容为生成验证码
import random,string
#生成随机code
def rndChar():
    return random.sample(string.ascii_letters+string.digits,1)[0]
#随机颜色
def rndColor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

def rndColor2():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

width = 100*4
height = 100
#定义图像，色彩模式，长宽，颜色
image = Image.new('RGB',(width,height),(255,255,255))
# image.save('hahah.jpg','jpeg')

#定义code字体，大小
font = ImageFont.truetype(r"C:\Windows\Fonts\arial.ttf",80)

#定义draw对象
draw = ImageDraw.Draw(image)

for x in range(width):
    for y in range(height):
        #draw像素点,点上色
        draw.point((x,y),fill=rndColor())


for t in range(4):
    #draw  code ,设置code位置，内容，字体大小，颜色
    draw.text((100*t+20,10),rndChar(),font=font,fill=rndColor2())
#加模糊效果
image2 =image.filter(ImageFilter.BLUR)
image2.save('code.jpg','jpeg')