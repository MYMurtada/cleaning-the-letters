text = input("Enter a string: ")


# -----------------------------------------------------
# ----[the  main function should print the result]-----
# -----------------------------------------------------

def main(result):
    if result == "":  # if the input has no letters in it the result should be empty.
        print("The entered string does not contain any letter")

    else:  # otherwise, the result will be printed here.
        print(result)


def getLetters(letter):
    answer = ""  # here the function should return a single value that has all the characters.
    for i in letter:
        if i.isalpha():  # if the index in the input is letter then we assign it.
            answer = answer + i
    return answer


# DO NOT FORGET TO CALL THE FUNCTION.
main(getLetters(text))

# ---------------------------------------------------
# ----------------------[DONE]-----------------------
# ---------------------------------------------------


