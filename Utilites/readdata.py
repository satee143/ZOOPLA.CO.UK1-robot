

def Input_Segartion(data):
   
    l2 = data.replace(',', '')
    l3 = l2.split()
    print(l3)
    l1=(int(l3[0][1:]))
    print(l1)
    print("Price Of the Property  in Descending Order:")
    #print(sorted(l1,reverse=True))
    return l1
        
        

        