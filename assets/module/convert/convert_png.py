from assets.biblioteca import *


def converter_pdf_para_images(a):
    images = convert_from_path(a, fmt='png')
    return images