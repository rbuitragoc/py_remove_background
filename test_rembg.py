from rembg import remove
from PIL import Image
input_path = 'whatever.jpeg'
output_path = 'whatever.png'
inp = Image.open(input_path)
output = remove(inp)
output.save(output_path)
