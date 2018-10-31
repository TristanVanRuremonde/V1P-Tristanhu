from PIL import Image, ImageDraw
import random
import string


def createCaptcha():
    'maakt een nieuw captcha plaatje aan'
    img = Image.new('RGB', (300, 90), color=(0,0,0))
    captchaText = ''
    captchaText = captchaText.join(
        random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(6))
    captchaKleur = random.sample(range(258), 3)
    captchaPositieX = random.randrange(0, 265)
    captchaPositieY = random.randrange(0, 60)
    captchaPositie = (captchaPositieX, captchaPositieY)
    d = ImageDraw.Draw(img)
    d.text(tuple(captchaPositie), captchaText, fill=tuple(captchaKleur))
    img.save('pil_text_font.png')

    return captchaText
