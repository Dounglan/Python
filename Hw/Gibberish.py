#Doung Lan Cheung
#Assignment 5, problem B
#get a file, then encode it, then decode. Ending the message in all caps.
def e():
#get file
    n = input("Enter a file name with message to encode: ")
    file_name = n + ".txt"
    file = open(file_name, "r")
    contentfile = file.readline()
#create encoded file, separtes words and capitlize 1st char of each word
    outfile= open(n +"Encoded.txt","w")
    b = contentfile.split()
    for i in range(len(b)):
        b[i]=b[i].title()
        c = b[i]
        d = c[0:1]
        e = c[1:len(b)]
        f = "itheg"
        message = d + f + e
        print(message, end=" ",file=outfile)
    file.close()
    outfile.close()
#make decode file for the encoded file
def d():
    efile = input("Enter name of file with message to decode: ")
    encodefile = open(efile +".txt", "r")
    outfile1= open(efile+"Decoded.txt","w")
    print(efile +"Decoded.txt", file=outfile1)    
    content = encodefile.readline()
    g = content.split()
    for j in range(len(g)):
        g[j]=g[j].upper()
        x = g[j]
        y = x[0:1]
        z = x[1:len(g)]
        a = x[len(g):]
        message = y + a
        print(message, end=" ",file=outfile1)
    encodefile.close()
    outfile1.close()

def main():
    e()
    d()
main()