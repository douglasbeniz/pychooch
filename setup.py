from distutils.core import setup
from distutils.extension import Extension
import os

SRC_PATH = os.path.join(os.path.dirname(__file__))
CHOOCH_SOURCE_FILES = ["printbanner.c", "minmax.c", "spline.c", "mucal.c", "fdprime.c",
 "smooth.c", "fits.c", "normalize.c", "checks.c", "integrate.c", "selwavel.c",
 "toplot.c", "savwin.c"]
for i in range(len(CHOOCH_SOURCE_FILES)):
  CHOOCH_SOURCE_FILES[i]=os.path.join(SRC_PATH, CHOOCH_SOURCE_FILES[i])  
PYCHOOCH_SOURCE_FILES=["PyChooch.c"]+CHOOCH_SOURCE_FILES

setup(name="PyChooch",
      version="0.0",
      author="Chooch: Gywndalf Evans, Diamond Light Source ; Python binding: Matias Guijarro, ESRF",
      ext_modules = [Extension('PyChooch', PYCHOOCH_SOURCE_FILES, 
                               libraries=['gsl', 'gslcblas'])],
) 
