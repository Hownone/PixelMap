# PixelMap

将喜欢的文字藏在图片里面发给喜欢的人吧^_^
一个关于像素构图的小玩法！

## 原理

事实上，每一张图片都是由一个一个的像素点所组成的。而每个像素点，都有自己的颜色，其颜色可以用一个数组来表示：(a,b,c)，其中每位数的取值范围都是 0-255。
比如(0,0,0)代表白色，(255,255,255)代表黑色。
当像素点足够多的时候，这张照片就是我们所说的高清照片。
而如果当像素点太少，我们的肉眼就能感知到明显的锯齿感。

我只要每个像素取出一个像素值，并使用这个像素做为该字的颜色即可，在像素量够多的情况下，从远处看，是能看到我们原来图像的轮廓的。

## import PIL

### 小白函数解释：

ImageDraw.Draw.text()在给定位置绘制字符串。
* 用法 * ：
ImageDraw.Draw.text(xy, text, fill=None, font=None, anchor=None, spacing=0, align=”left”)    
*参数*
xy-文字的左上角。
text-要绘制的文本。如果包含任何换行符，则文本将传递到multiline_text()
fill-用于文本的颜色。
font-一个ImageFont实例。
spacing-如果文本传递到multiline_text()，则行之间的像素数。
align-如果文本已传递到multiline_text()，“left”，“center”或“right”。
*返回类型*：返回带有文本的图像。

### image类中的函数

new : 这个函数创建一幅给定模式（mode）和尺寸（size）的图片。如果省略 color 参数，则创建的图片被黑色填充满，如果 color 参数是 None 值，则图片还没初始化。
open : 打开并识别所提供的图像文件。不过，使用这函数的时候，真正的图像数据在你进行数据处理之前并没有被读取出来。可使用 load 函数进行强制加载。 mode 参数可以省略，但它只能是 "r" 值。
convert : 返回一个转换后的图像的副本。

PIL.ImageFont.truetype(font=None, size=10, index=0, encoding=”)  
参数：
font-TrueType字体文件。在Windows下，如果在该文件名中找不到该文件，则加载程序还会在Windows fonts /目录中查找。
size-请求的大小(以磅为单位)。
index-要加载的字体(默认为第一个可用的字体)。
encoding-使用哪种字体编码(默认为Unicode)。
返回：字体对象。
异常：IOError-如果无法读取文件。



