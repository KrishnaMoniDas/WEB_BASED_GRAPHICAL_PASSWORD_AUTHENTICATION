import math

def algorithm_implementation(selection):
  User_string = selection
  stringP1 = ""
  stringP2 = ""
  halflen = len(User_string) // 2 
  for i in range(len(User_string)):
      if User_string[i] != "" and i < halflen:
          stringP1 += User_string[i]
      elif User_string[i] != "" and i >= halflen:
          stringP2 += User_string[i]
        
  r1 = int(stringP1) * 1.5
  r2 = int(stringP2) * 0.8 #here the 0.8 and 1.5 are here just for example
                           #vendors can change the values here and the operand to
                           #their preference
  
  r1 -= 0.10
  r2 -= 1.5 
  r1 = math.ceil(r1)
  r2 = math.ceil(r2)
  Final_string = str(r1) + str(r2)
  return(Final_string)
