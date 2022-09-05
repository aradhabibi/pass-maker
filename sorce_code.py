import random 
def password():
    pass_length=int(input("length of your password?"))

    result_list = []

    result = ""

    wrong = 0

    while wrong < 10:


        for i in range(pass_length):

            my_char = ['q','w','e','r','t','y','u','i','o','p','a','s','d',

            'f','g','h','j','k','l','z','x','c','v','b','n','m','1','2','3',

            '4','5','6','7','8','9','!','@','#','$','%','^','&','*','Q','W','E',

            'R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X',

            'C','V','B','N','M','+','-','/','=','_']
            x = random.choice(my_char)

            result_list.append(x)

            random.shuffle(result_list)

        for y in result_list:
            result += y

            wrong += 1

        print(result)


password()
