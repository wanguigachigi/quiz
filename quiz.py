print('WELCOME TO ONLINE QUIZ  ')
print("")

begin = input('Would you like to proceed? yes/no:  ')
if begin == 'yes':
    print('')
    print('Get Ready...  ')
    print("")
    print('The questions below are multiple quiz.\n  Good Luck! ')
    print("")
    print('a. Mt. Kenya')
    print('b. Mt. Kilimanjaro')
    print('c. Mt. Longonot')
    print('d. Mt. Elgon')
    print("")
    result = 0
    q1 = input('Which is the highest mountain in East Africa? :')
    if q1 == 'b':
        result = result + 1
    q2 = input('Which mountain has a crater lake? :')
    if q2 == 'a':
        result = result + 1
    q3 = input('Which mountain is a dormant volcano? :')
    if q3 == 'c':
        result = result + 1

    q4 = input('Which mountain is the pride of Western Kenya? :')
    if q4 == 'd':
        result = result + 1
        print('')
    print('Your score is {} out of 4 questions'.format(result))
    print('')
    if result != 4:
        q = input('Would you like to retake the quiz? Yes/No : ')
        if q == 'No' or q == 'no':
            print('')
            print('Your score is saved. Goodbye.')
        else:
            if q == 'Yes' or q == 'yes':
                print('')
            print('Get ready to redo the whole test again...')


elif begin == 'no':
    print('Goodbye..')


else:
    print('')
    print('invalid choice.. Kindly input yes or no ')


