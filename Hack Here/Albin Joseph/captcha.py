<<<<<<< HEAD
from captcha.image import ImageCaptcha
image = ImageCaptcha(width = 280, height = 90)
captcha_text = 'HACKT0BER'
data = image.generate(captcha_text)
image.write(captcha_text, 'CAPTCHA.png')
=======
from captcha.image import ImageCaptcha
image = ImageCaptcha(width = 280, height = 90)
captcha_text = 'HACKT0BER'
data = image.generate(captcha_text)
image.write(captcha_text, 'CAPTCHA.png')
>>>>>>> a6ea09f761b78b37e6df9bf885426826324fbc6c
