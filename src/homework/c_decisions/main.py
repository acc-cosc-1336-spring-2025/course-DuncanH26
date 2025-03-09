import decisions 

def main():
    options = int(input("Enter Options "))
    total = int(input("Enter Total "))

    Ratio = decisions.get_options_ratio(options, total)
    Result = decisions.get_faculty_rating(Ratio)

    print(options/total, Result)

main()




    
    