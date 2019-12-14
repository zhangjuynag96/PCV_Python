from PIL import Image
import os

class PIL_Test():
    def __init__(self):
        self.pil_im = Image.open('../img/1.jpg')
        self.path = '../img'

    def _convert(self):
        '''
        灰度设置
        '''
        pil_im = self.pil_im.convert('L')
        pil_im.save('../img/1-1.jpg')

    def get_imlist(self):
        '''
        遍历图片文件夹，将所有图片格式转换为jpg
        '''
        return [os.path.join(self.path, f) for f in os.listdir(self.path) if f.endswith('.jpg')]

    def _thumbnail(self):
        '''
        缩略图
        '''
        self.pil_im.thumbnail((128, 128))
        self.pil_im.save('../img/1-2.jpg')

    def _crop(self):
        '''
        裁剪与反转
        '''
        box = (100, 100, 400, 400)
        region = self.pil_im.crop(box)
        region = region.transpose(Image.ROTATE_180)
        region = self.pil_im.paste(region, box)
        region.save('../img/1-3.jpg')

    def _resize(self):
        '''
        调整尺寸和旋转
        '''
        out = self.pil_im.resize((128,128))
        out = out.rotate(45)
        out.save('../img/1-4.jpg')


if __name__ == '__main__':
    test = PIL_Test()
    #test._convert()
    #test.get_imlist()
    #test._thumbnail()
    #test._crop()
    test._resize()
