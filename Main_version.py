progress_count = 0
progress_moduleTrailer_count = 0
moduleRetriever_count = 0
exclude_count = 0


# Caculation function of the progression #

def progress_calculation(passmarks, failmarks, choice):
    global progress_count
    global progress_moduleTrailer_count
    global moduleRetriever_count
    global exclude_count
    if choice == 'y':
        if passmarks == 120:
            print("Progress")
            progress_count += 1
            return progress_count

        elif passmarks == 100:
            print("progress (module trailer)")
            progress_moduleTrailer_count += 1
            return progress_moduleTrailer_count

        elif passmarks == 80:
            print("Do not progress - module retriever")
            moduleRetriever_count += 1
            return moduleRetriever_count

        elif passmarks == 60:
            print("Do not progress - module retriever")
            moduleRetriever_count += 1
            return moduleRetriever_count

        elif failmarks >= 80:
            print("Exclude")
            exclude_count += 1
            return exclude_count

        elif passmarks == 40:
            print("Do not progress - module retriever")
            moduleRetriever_count += 1
            return moduleRetriever_count

        elif passmarks == 20:
            print("Do not progress - module retriever")
            moduleRetriever_count += 1
            return moduleRetriever_count

        elif passmarks == 0:
            print("Do not progress - module retriever")
            moduleRetriever_count += 1
            return moduleRetriever_count

    # //////////////////////////////////////// Histogram /////////////////////////////////////////////// #
    if choice == 'q':
        print('________________________________________________________________________________')
        print('Histogram')
        print('Progress ', progress_count, ' : ', end=' ')
        for i in range(progress_count):
            print('*', end='')
        print('Trailer ', progress_moduleTrailer_count, ' : ', end='')
        for j in range(progress_moduleTrailer_count):
            print('*', end='')
        print('Retriever ', moduleRetriever_count, ' : ')
        for k in range(moduleRetriever_count):
            print('*', end='')
        print('Excluded ', exclude_count, ' : ')
        for l in range(exclude_count):
            print('*', end='')
        print('________________________________________________________________________________')


# Function of the validation #
def validation(validPass, validDefer, validFail, choice):
    if choice == 'y':
        tot = validPass + validDefer + validFail
        if 0 <= (validPass or validDefer or validFail) <= 120:
            if tot == 120:
                (progress_calculation(validPass, validFail, choice))
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
                pass_input: int = int(input("Enter pass credits : "))
                defer_input = int(input("Enter defer credits : "))
                fail_input = int(input("Enter fail credits : "))
            except:
                print("Integer required")
                continue
            validation(pass_input, defer_input, fail_input, user_choice)
            print("Would you like to enter another set of data? ")
        elif user_choice == 'q':
            progress_calculation(pass_input, fail_input, user_choice)
            break

    break
