from rembg import remove
from PIL import Image
input_path = 'resource/whatever.jpeg'
output_path = 'output/whatever.png'
inp = Image.open(input_path)
output = remove(inp)
output.save(output_path)
