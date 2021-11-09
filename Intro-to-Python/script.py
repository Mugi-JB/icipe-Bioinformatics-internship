import urllib.request
import time
from pathlib import Path

def read_write(filein,fileout):
    path = Path(filein)
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