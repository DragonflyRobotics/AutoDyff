from pylatexenc.latex2text import LatexNodes2Text
from TexSoup import TexSoup
print(LatexNodes2Text().latex_to_text(r"""$x^{2x^{2}+1}-2x+1$"""))
#same equation converted by texsoup
soup = TexSoup(r"""$x^{2x^{2}+1}-2x+1$""")
print(soup)
exit()
from CalCoolUs.preprocess import ShuntingYard

myshunt = ShuntingYard()
print(myshunt.getPostfix("x^2x^2+1-2x+1"))
