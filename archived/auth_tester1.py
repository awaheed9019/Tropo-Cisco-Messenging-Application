from tropo import Tropo
import random

TO_NUMBER = "+13477209741"
t = Tropo()
t.message("Your one time token is" + str(random.randint(1000,9999)),TO_NUMBER,channel="TEXT",network="SMS",timeout="5")
json = t.RenderJson()








