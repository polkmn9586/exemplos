import telepot
from pprint import pprint
bot = telepot.Bot("6218006765:AAF309hpXCmaU1r9P41zKiNK1L8gaqTMyqI")

from telepot.loop import MessageLoop
def handle(msg):
     pprint(msg)



