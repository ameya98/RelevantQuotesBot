def search(iden):
    quotes = []
    with open("quotes.txt", "r") as f:
        searchlines = f.readlines()
        
    for i, line in enumerate(searchlines):
        if str(iden) == line.strip("\n"):
            for l in searchlines[i + 1 : ]:
                if (str(iden + 1) == l.strip("\n")):
                    return quotes
                else:
                    if(l != "\n"):
                        quotes.append(l)


        

                
            
