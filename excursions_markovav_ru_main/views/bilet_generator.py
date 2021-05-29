import datetime
import qrcode

from PIL import Image, ImageDraw, ImageFont
from django.http import HttpResponse
from django.utils import formats


def generate(name, date, qr_data):
    im = Image.open('private/bilet_example.png')
    place_text(name, im, 1000, 316, 48, True)
    place_text(date, im, 1000, 416, 48, True)
    cur_date = formats.date_format(datetime.datetime.now(), "SHORT_DATETIME_FORMAT")
    place_text("Дата и время записи: " + cur_date, im, 10, 990, 24, False)
    place_qr(qr_data.replace('%reg_date%', cur_date), im)
    response = HttpResponse(content_type="image/png")
    im.save(response, "PNG")
    return response


def place_text(text, im, x, y, size, centered):
    font = ImageFont.truetype('private/OpenSans-Regular.ttf', size=size)
    draw_text = ImageDraw.Draw(im)
    w, h = draw_text.textsize(text, font=font)
    draw_text.text(
        (x - (w // 2 if centered else 0), y - (h // 2 if centered else 0)),
        text,
        font=font,
        fill='#1C0606'
    )


def place_qr(data, im):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1,
    )
    qr.add_data(data)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white")
    im.paste(qr_image, (im.width - qr_image.height - 10, im.height - qr_image.height - 10))
