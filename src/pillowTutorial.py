import os, sys
from PIL import Image

# try :
#     im = Image.open('wife.png')
#     # print(im.format, im.size, im.mode)
#     im.show()
#
# finally:
#     print("Processing Done")

# Saving Image

# for infile in sys.argv[1:]:
#     f, e = os.path.splitext(infile)
#     outfile = f + ".jpg"
#     if infile != outfile:
#         try :
#             with Image.open(infile) as im:
#                 im.save(outfile)
#         except OSError:
#             print("Cannot convert file")

# Create Thumbnail
# size = (128, 128)
# for infine in sys.argv[1:]:
#     outfile = os.path.splitext(infine)[0] + ".thumbnail"
#     if infine != outfile:
#         try:
#             with Image.open(infine) as im:
#                 im.thumbnail(size)
#                 im.save(outfile, "JPEG")
#         except OSError:
#             print("cannot create thumbnail for", infine)

