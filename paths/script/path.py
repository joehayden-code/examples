# same folder
from api_key import apikey



# different folder
import sys
sys.path.append(r'C:\Users\harry\OneDrive\Scripts\examples\paths')
from paths.secret.api_key2 import apikey2

print (apikey)
print (apikey2)

