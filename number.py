def get_number() :
       number=str(input("Please enter your phone number : "))
       if number[:1] == '0' :
              number=number[1:]
       else : 
              number=number
       return number

       

