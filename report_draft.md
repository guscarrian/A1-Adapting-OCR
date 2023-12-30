# Part 1 – Basic Implementation

Initially, I experienced some issues with the *trdg* package and I also needed to add some minor changes regarding the import statements (*torch.six*) and the original code (https://github.com/Deepayan137/Adapting-OCR) to avoid some errors (RuntimeError: cuDNN version incompatibility, TypeError: can't convert cuda:0 device type tensor to numpy, etc). Those changes are marked with *#added* on the notebook (notebooks/ocr.ipynb). After running the code successfully, the model performed quite well with a character accuracy of over 96% and a word accuracy above 0.85%.

![Alt text](./notebooks/part1.png)


