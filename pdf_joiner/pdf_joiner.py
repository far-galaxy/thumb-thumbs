import os
from PIL import Image

dirs = [name for name in os.listdir(".") if os.path.isdir(name)]
print(dirs)

for d in dirs:
    files = [name for name in os.listdir(f"./{d}")]
    files.sort()
    print(d, files)
    image_list = []
    for file in files:
        p = os.path.abspath(f"./{d}/{file}")
        img = Image.open(p)
        img = img.convert('RGB')
        image_list.append(img)
        
    image_list[0].save(
        os.path.abspath(f"./{d}.pdf"),
        save_all=True,
        append_images=image_list[1:],
    )
