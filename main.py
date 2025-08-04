from Museo import Museo
from api import api

def main(): 
    museo = Museo(api)
    museo.start()

main()