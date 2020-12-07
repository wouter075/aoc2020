from PIL import Image
import glob


with open('day3.txt') as f:
    lines = [line.rstrip() for line in f]

tree = 0
right = 0
down = 0
counter = 0

image_list = []
image_lines = []
for line in lines:
    line = list(line)
    # print(right)
    if counter is not 0:
        if line[right] == "#":
            line[right] = "X"
            tree += 1
        else:
            line[right] = "O"

    down += 1
    right += 3
    if right >= len(line):
        right = right % len(line)

    # print("".join(line))
    image_lines.append(line)
    # print(line)
    counter += 1

# convert to images:
c = 0

for line in image_lines:
    # print(set(line))
    tmp = []
    for l in line:

        if l == ".":
            tmp.append("images/set/snow.png")
        if l == "#":
            tmp.append("images/set/tree.png")
        if l == "O":
            tmp.append("images/set/ski.png")
        if l == "X":
            tmp.append("images/set/ginger.png")

    images = [Image.open(x) for x in tmp]
    widths, heights = zip(*(i.size for i in images))
    total_width = sum(widths)
    max_height = max(heights)

    new_im = Image.new('RGB', (total_width, max_height))

    x_offset = 0
    for im in images:
        new_im.paste(im, (x_offset, 0))
        x_offset += im.size[0]

    new_im.save(f'images/day3a/test{c}.png')
    c += 1

# filepaths
fp_in = "images/day3a/test*.png"
fp_out = "images/day3a.gif"

# https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#gif
img, *imgs = [Image.open(f) for f in sorted(glob.glob(fp_in))]
img.save(fp=fp_out, format='GIF', append_images=imgs,
         save_all=True, duration=500, loop=0)

print(f"Argghhh we just hit {tree} trees!")