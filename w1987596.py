pro_count = 0
trail_count = 0
exclude_count = 0
donot_prog = 0

Progress_dis=[]

outcome_dictionary ={}

def validate_credit(credit_type):
    while True:
        try:
            credit = int(input("Enter the number of credits for {}: ".format(credit_type)))
            if credit not in[0,20,40,60,80,100,120]:
                print("Out of range")
                continue
            return credit
        except ValueError:
            print("Integer required")


while True:
    version_check = input("Select Staff (P) or Student (S) Version :")
    if version_check == "P":
        break
    elif version_check == "S":
        break
    else:
        continue


while True:
    student_id = input("Enter student id :")

    passmark = validate_credit("pass")
    deffer = validate_credit("deffer")
    failmark = validate_credit("fail")

    if passmark + deffer + failmark != 120:
        print("Total incorrect")
        continue

    if passmark == 120:
        pro_count = pro_count + 1
        print("Progress")
        temp_prodisplay = f"Progress - {passmark},{deffer},{failmark}"
        Progress_dis.append(temp_prodisplay)
        outcome_dictionary[student_id] = temp_prodisplay

    elif passmark == 100:
        trail_count = trail_count + 1
        print("Progress (module trailer)")
        temp_prodisplay = f"Progress (module trailer) - {passmark},{deffer},{failmark}"
        Progress_dis.append(temp_prodisplay)
        outcome_dictionary[student_id] = temp_prodisplay

    elif passmark <= 40 and deffer <= 40 and failmark >= 80 and failmark <= 120:
        exclude_count = exclude_count + 1
        print("Exclude")
        temp_prodisplay = f"Exclude - {passmark},{deffer},{failmark}"
        Progress_dis.append(temp_prodisplay)
        outcome_dictionary[student_id] = temp_prodisplay


    else:
        donot_prog = donot_prog + 1
        print("Do not progress – module retriever")
        temp_prodisplay = f"Do not progress – module retriever - {passmark},{deffer},{failmark}"
        Progress_dis.append(temp_prodisplay)
        outcome_dictionary[student_id] = temp_prodisplay

    if version_check == "P":
        choice = input("Would you like to enter another set of data? Enter 'y' for yes or 'q' to quit and view results: ")

        while choice not in ["y","q"]:
            print("Invalid input")
            choice = input(
                "Would you like to enter another set of data? Enter 'y' for yes or 'q' to quit and view results: ")


        if choice == 'y':
            continue
        elif choice == 'q':
            with open("progression_data.txt", "w") as file:
                for temp_prodisplay in Progress_dis:
                    file.write(temp_prodisplay + "\n")
            print("Histogram")
            print("Progress " + str(pro_count) + ":" + pro_count * " *")
            print("Trailer " + str(trail_count) + ":" + trail_count * " *")
            print("Retriever " + str(donot_prog) + ":" + donot_prog * " *")
            print("Excluded " + str(exclude_count) + ":" + exclude_count * " *")

            for temp_prodisplay in Progress_dis:
                print(temp_prodisplay)

            for key,value in outcome_dictionary.items():

                print(f"{key} : {value}")

            print(str(pro_count + trail_count + donot_prog + exclude_count) + " outcomes in total.")
            break


        continue
    else:
        break