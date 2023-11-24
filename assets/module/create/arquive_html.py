from assets.biblioteca import *

def generate_html_with_images(a):
    html = '<!DOCTYPE html><html><head><title>PDF para HTML</title></head><body>'

    for idx, image in enumerate(a):
        image_base64 = base64.b64encode(image.tobytes()).decode('utf-8')
        html += f'<img src="data:image/png;base64,{image_base64}" alt="Image {idx+1}">'

    html += '</body></html>'
    return html