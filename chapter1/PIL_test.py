from PIL import Image

pil_im = Image.open('../img/1.jpg')

pil_im = pil_im.convert('L')

pil_im.save('../img/1-1.jpg')
