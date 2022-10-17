# Lab 7

Here is how you can run the script I created.

```
virtualenv ~/venv/pillow
virtuaenv ~venv/webscraping/Scripts/activate.ps1
pip install pillow

```

Then I saved an image to my computer. Make sure you know the path to this image.

```

from PIL import Image,ImageFilter
from PIL.ImageFilter import (EMBOSS) 
myImg = Image.open('C:/it3080-scripts/pics/luffy.jpeg') (this should be the path to your file)
myImgEmboss = img.filter(EMBOSS)
myImgEmboss.save('C:/it3080-scripts/pics/luffy_emboss.jpeg')
myImgEmboss.show()

```

Note: The myImg should be saved as that variable and will be used in the next examples without redeclaring it.

```
from PIL.ImageFilter import (FIND_EDGES)
myImgFindEdges = img.filter(FIND_EDGES)
myImgFindEdges.save('C:/it3080-scripts/pics/luffy_findEdges.jpeg')
myImgFindEdges.show()

```
from PIL.ImageFilter import (SHARPEN)
myImgSharpen = img.filter(SHARPEN)
myImgSharpen.save('C:/it3080-scripts/pics/luffy_sharpen.jpeg')
myImgSharpen.show()
quit()
deactivate
```




