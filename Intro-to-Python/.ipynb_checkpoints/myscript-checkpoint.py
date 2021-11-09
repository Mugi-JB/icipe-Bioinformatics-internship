#07.ipynb Exercise (a)
import urllib.request
import time
from pathlib import Path

def read_write(filein,fileout):
    path = Path(filein)
    #checks if the given file is present
    #if not present, downloads a default and saves it under the given name
    #waits for 5 seconds for file to download
    if not path.is_file():
        url = "https://www.uniprot.org/docs/humchrx.txt"
        destination_filename = filein
        urllib.request.urlretrieve(url, destination_filename)
        time.sleep(5)
    
        
    gene_list=[]
    with open(filein, "r") as filein:
        flag=False
        for line in filein:
            if line.startswith("name"):
                flag=True
                pass
            if flag:
                line=line.split()
                
                if len(line) > 0:
                    gene_list.append(line[0])
    
    gene_list=gene_list[1:-7]
    with open(fileout, 'w') as outputfile:
        for i in gene_list:
            outputfile.write(i+"\n")
                
