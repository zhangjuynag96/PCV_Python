from PIL import Image
import os

pil_im = Image.open('../img/1.jpg')
img_path = '../img'

def _convert(pil_im):
    '''
    灰度设置
    '''
    pil_im = pil_im.convert('L')
    pil_im.save('../img/1-1.jpg')

def get_imlist(path):
    '''
    遍历图片文件夹，将所有图片格式转换为jpg
    '''
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]

def _thumbnail(pil_im):
    '''
    缩略图
    '''
    pil_im.thumbnail((128, 128))
    pil_im.save('../img/1-2.jpg')

if __name__ == '__main__':
    pass
    #_convert(pil_im)
    #get_imlist(img_path)
    #_thumbnail(pil_im)
