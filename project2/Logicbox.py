#welcome message

print("=====================================")
print("PATTERN GENERAATOR AND NUMBER ANALYZER")
print("======================================")
print("WELCOME!")
print("THIS PROGRAM CAN GENERATE A PATTERN")
print("AND ANALYZE A RANGE OF NUMBER.")

while True:
    print("\n == Menu ==")
    print("1. Pattern Generator")
    print("2. Number Analyzer")
    print("3.Exit")
    

    choice = int(input("Enter your choice:"))

    #patter generator

    if choice == 1:
        print("\n --pattern generation--")
        print("1. right-angled triangle")

        pattern=int(input("Enter pattern choice:"))
        if pattern == 1:
            rows = int(input("Enter number of rows: "))

        #validate row counts
            if rows <= 0:
                print("Invalid row count!")
                print("Row count must be positive")
                continue
            print("\n right angled triangles")

            #outer loop controls rows

            for i in range (1, rows+1):
              for j in range(i):
                    print("*", end="")
              print()
            else:
                        print("Invalid pattern choice")
                       

            #number analyzer
    elif choice == 2:
                        
                        print("\n--Number Analyzer--")
                        start = int(input("Enter start number:"))
                        end = int(input("Enter end number:"))

                        #validate range
                        if end < start:
                            print("Invalid range")
                            print("End number must be greater than start number")
                            continue
                        print("\n odd and even numbers:")
                        total = 0

                        #loop through the range
                        for number in range (start,end + 1):
                            if number %2 == 0:
                                print(number,"is even")
                            else:
                                print(number,"is odd")

                                    #add number of total

                        total=total+ number
                        print("/n sum of all numbers:",total)

                                    #exit
    elif choice==3:
            print("\n   THANK YOU FOR USING PATTERN GENERATOR AND NUMBER ANALAYZER!")
            print("PROGRAM ENDED")
            break

            #invalid menu choice
    else:
        print("invalid choice!")
        print("please select 1,2 or 3")
        continue

                                    
                                    
                        
                                    



