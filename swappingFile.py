def swapFileData() : 
    file1= input("Enter the name of file to be swapped: ")
    file2= input("Enter the name of the file to be swapped with: ")
    with open(file2,'r') as a:
       data_a= a.read()
       
    with open(file1,'r') as b:
       data_b= b.read()

    with open(file1,'w') as b:
       b.write(data_a)

    with open(file2,'w') as a:
       a.write(data_b)     

swapFileData()
    
