string = "sin(cos((3+x)^(8^(3+x)+2)) * (sin(tan(ln((x+2)^(x+3))))))"

import re

print(re.findall(r"(", string))
