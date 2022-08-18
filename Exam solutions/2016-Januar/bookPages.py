import numpy as np
import math
def bookPages(pagesContent):
    pagesBooklet=0
    while pagesContent > pagesBooklet:
        pagesBooklet=pagesBooklet+4
    return pagesBooklet

print(bookPages(17))
print(bookPages(35))
print(bookPages(105))
