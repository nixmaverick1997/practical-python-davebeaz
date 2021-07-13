symbols='AAPL,IBM,MSFT,YHOO,SCO'
symbols="HPQ,"+symbols+",GOOG"
text="It's my birthday on 08/07/2022. Let us meet on 09/07/2022"
import re
print(re.findall(r'\d+/\d+/\d+',text))
print(re.sub(r'(\d+)/(\d+)/(\d+)',r'\3-\1-\2',text))