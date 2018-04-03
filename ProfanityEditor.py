from urllib.request import urlopen,Request
from urllib.parse import quote
def readText() :
    quote=open(r"C:\Users\andidwan\Desktop\images\textFile.txt")
    content=quote.read()
    quote.close()
    profanity(content)

def profanity(text) :
    safe_text = quote(text)
    connection=urlopen(Request("http://www.wdylike.appspot.com/?q="+safe_text))
    output=connection.read()
    print(output)
    connection.close()
readText()
