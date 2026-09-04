def check_even_odd(number): 
#number = int(input("Enter a number:"))
  if number %2 ==0:
     return("Even Number")

  else:
    return("Odd number")
def main():
    num=int(input("Enter a number to check(or 'q' to quit):")) 
    result= check_even_odd(num)
    print(f"The number(num)is {result}.")
main()
                
    
 
