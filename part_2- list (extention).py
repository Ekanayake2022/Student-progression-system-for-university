progress_list = []
progress_moduleTrailer_list = []
moduleRetriever_list = []
exclude_list = []


# Caculation function of the progression #

def progress_calculation(passmarks, defermarks, failmarks, choice, ):
    if choice == 'y':
        if passmarks == 120:
            print("Progress")
            progress_list.append(passmarks)
            progress_list.append(defermarks)
            progress_list.append(failmarks)
            return progress_list

        elif passmarks == 100:
            print("progress (module trailer)")
            progress_moduleTrailer_list.append(passmarks)
            progress_moduleTrailer_list.append(defermarks)
            progress_moduleTrailer_list.append(failmarks)
            return progress_moduleTrailer_list

        elif passmarks == 80:
            print("Do not progress - module retriever")
            moduleRetriever_list.append(passmarks)
            moduleRetriever_list.append(defermarks)
            moduleRetriever_list.append(failmarks)
            return moduleRetriever_list

        elif passmarks == 60:
            print("Do not progress - module retriever")
            moduleRetriever_list.append(passmarks)
            moduleRetriever_list.append(defermarks)
            moduleRetriever_list.append(failmarks)
            return moduleRetriever_list


        elif failmarks >= 80:
            print("Exclude")
            exclude_list.append(passmarks)
            exclude_list.append(defermarks)
            exclude_list.append(failmarks)
            return exclude_list


        elif passmarks == 40:
            print("Do not progress - module retriever")
            moduleRetriever_list.append(passmarks)
            moduleRetriever_list.append(defermarks)
            moduleRetriever_list.append(failmarks)
            return moduleRetriever_list


        elif passmarks == 20:
            print("Do not progress - module retriever")
            moduleRetriever_list.append(passmarks)
            moduleRetriever_list.append(defermarks)
            moduleRetriever_list.append(failmarks)
            return moduleRetriever_list


        elif passmarks == 0:
            print("Do not progress - module retriever")
            moduleRetriever_list.append(passmarks)
            moduleRetriever_list.append(defermarks)
            moduleRetriever_list.append(failmarks)
            return moduleRetriever_list


# _______________________________________ Histogram ______________________________________________#
# Function of the validation #
def validation(validPass, validDefer, validFail, choice):
    if choice == 'y':
        tot = validPass + validDefer + validFail
        if 0 <= (validPass or validDefer or validFail) <= 120:
            if tot == 120:
                (progress_calculation(validPass, validDefer, validFail, choice))
            else:
                print("Total incorrect")
        else:
            print("Out of range")
    elif choice == 'q':
        return False


# Starting the programme #
while True:

    while True:
        user_choice = str(input("Enter 'y' to continue programme and enter 'q' to quit the programme : "))
        if user_choice == 'y':
            try:  # Handling the errors of input #
                pass_input = int(input("Enter pass credits : "))
                defer_input = int(input("Enter defer credits : "))
                fail_input = int(input("Enter fail credits : "))
            except:
                print("Integer required")
                continue
            validation(pass_input, defer_input, fail_input, user_choice)
            print("Would you like to enter another set of data? ")
        elif user_choice == 'q':
            print("Progress", ' - ', progress_list)
            print("Progress (module trailer)", ' - ', progress_moduleTrailer_list)
            print("Module retriever - ", moduleRetriever_list)
            print("Exclude - ", exclude_list)
            break

    break
