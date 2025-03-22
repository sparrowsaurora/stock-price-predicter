from data.stock import Stock
from data.formating import Formatting

apl = Stock("apl", 10, 500)
print(apl.display_formatted())
print(Formatting.basic_stats("APL", 10.63, 500, 1.08))