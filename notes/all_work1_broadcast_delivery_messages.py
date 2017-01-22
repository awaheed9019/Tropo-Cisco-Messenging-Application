
phone_numbers = ["+13477209741", "+19176033714"]

for number in phone_numbers:
    print number
    #call(number, { "network":"SMS" })
    #say("Gimme yo money!")

N/A
----------------------------------------------------------

call("+13477209741", { "network":"SMS" })
say("Gimme yo money1!")
hangup()
call("+19176033714", { "network":"SMS" })
say("Gimme yo money2!")

Yes
----------------------------------------------------------

phone_numbers = ["+13477209741", "+19176033714"]

for number in phone_numbers:
    call("+13477209741", { "network":"SMS" })
    say("Gimme yo money3!")
    hangup()

No
----------------------------------------------------------

phone_numbers = ["+13477209741", "+19176033714"]

for number in phone_numbers:
    call("+13477209741", { "network":"SMS" })
    say("Gimme yo money3!")
    if number == phone_numbers[0]:
        hangup()

No
----------------------------------------------------------

phone_numbers = ["+13477209741", "+19176033714"]
call(phone_numbers[0], { "network":"SMS" })
say("Gimme yo money4!")
hangup()
call(phone_numbers[1], { "network":"SMS" })
say("Gimme yo money5!")

No
----------------------------------------------------------

call("+13477209741", { "network":"SMS" })
say("Gimme yo money1!")
call("+19176033714", { "network":"SMS" })
say("Gimme yo money2!")

----------------------------------------------------------

call("+13477209741", { "network":"SMS" })
say("Gimme yo money1!")
wait(3000)
call("+19176033714", { "network":"SMS" })
say("Gimme yo money2!")

No
----------------------------------------------------------

call("+13477209741", { "network":"SMS" })
say("Gimme yo money1!")
hangup()
wait(3000)
call("+19176033714", { "network":"SMS" })
say("Gimme yo money2!")

Maybe
----------------------------------------------------------

call("+13477209741", { "network":"SMS" })
say("Gimme yo money10!")
hangup()
wait(3000)
call("+19176033714", { "network":"SMS" })
say("Gimme yo money11!")
hangup()
wait(3000)

Yes
----------------------------------------------------------

call("+13477209741", { "network":"SMS" })
say("Heyo3!")
hangup()
wait(3000)
call("+19292253456", { "network":"SMS" })
say("Heyo2!")
hangup()
wait(3000)

----------------------------------------------------------

phone_numbers = ["+13477209741", "+19292253456"]
for number in phone_numbers:
    call(number, { "network":"SMS" })
    say("Heyo4!")
    hangup()
    wait(3000)

----------------------------------------------------------

def format_phone_num(input_num):
    ASCII_0 = 48
    ASCII_9 = ASCII_0 + 9
    result = ""
    for ch in input_num:
        if ord(ch) >= ASCII_0 and ord(ch) <= ASCII_9:
            result += ch
    if len(result) == 10:
        return "+1" + result
    if len(result) == 11 and result[0] == '1':
        return "+" + result
    return ""

pNums = ["1282567892", "3456788765434", "%^&*(UHGF", "h(*&^D^%&65678", "8468446498", "1111111111", "22222***22222", "347-720-9741", "+1-848-989-1452", "16584957823"]

for p in range(len(pNums)):
    print pNums[p], format_phone_num(pNums[p])

#phone_numbers = ["+13477209741", "+19292253456"]
for number in phone_numbers:
    call(number, { "network":"SMS" })
    say("Heyo4!")
    hangup()
    wait(3000)

----------------------------------------------------------

def sep_phone_num(input_str_all_num):
    all_unformatted = input_str_all_num.split(" ")
    result = []
    for i in range(len(all_unformatted)):
        formatted = format_phone_num(all_unformatted[i])
        if formatted != "":
            result.append(formatted)
    return result

def format_phone_num(input_num):
    ASCII_0 = 48
    ASCII_9 = ASCII_0 + 9
    result = ""
    for ch in input_num:
        if ord(ch) >= ASCII_0 and ord(ch) <= ASCII_9:
            result += ch
    if len(result) == 10:
        return "+1" + result
    if len(result) == 11 and result[0] == '1':
        return "+" + result
    return ""

print sep_phone_num("1282567892 3456788765434 %^&*(UHGF h(*&^D^%&65678 8468446498 1111111111 22222***22222 347-720-9741 +1-848-989-1452 16584957823")

----------------------------------------------------------

def sep_phone_num(input_str_all_num):
    all_unformatted = input_str_all_num.split(" ")
    result = []
    for i in range(len(all_unformatted)):
        formatted = format_phone_num(all_unformatted[i])
        if formatted != "":
            result.append(formatted)
    return result

def format_phone_num(input_num):
    ASCII_0 = 48
    ASCII_9 = ASCII_0 + 9
    result = ""
    for ch in input_num:
        if ord(ch) >= ASCII_0 and ord(ch) <= ASCII_9:
            result += ch
    if len(result) == 10:
        return "+1" + result
    if len(result) == 11 and result[0] == '1':
        return "+" + result
    return ""

#phone_numbers = sep_phone_num("347-720-9741 929-225-3456 %^&*(UHGF h(*&^D^%&65678 8468446498 1111111111 22222***22222 347-720-9741 +1-848-989-1452 16584957823")
phone_numbers = sep_phone_num("347-720-9741 929-225-3456 %^&*(UHGF h(*&^D^%&65678")

for number in phone_numbers:
    call(number, { "network":"SMS" })
    say("Heyo4!")
    hangup()
    wait(3000)

----------------------------------------------------------

def sep_phone_num(input_str_all_num):
    all_unformatted = input_str_all_num.split(" ")
    result = []
    for i in range(len(all_unformatted)):
        formatted = format_phone_num(all_unformatted[i])
        if formatted != "":
            result.append(formatted)
    return result

def format_phone_num(input_num):
    ASCII_0 = 48
    ASCII_9 = ASCII_0 + 9
    result = ""
    for ch in input_num:
        if ord(ch) >= ASCII_0 and ord(ch) <= ASCII_9:
            result += ch
    if len(result) == 10:
        return "+1" + result
    if len(result) == 11 and result[0] == '1':
        return "+" + result
    return ""

#phone_numbers = sep_phone_num("347-720-9741 929-225-3456 %^&*(UHGF h(*&^D^%&65678 8468446498 1111111111 22222***22222 347-720-9741 +1-848-989-1452 16584957823")
phone_numbers = sep_phone_num("347-720-9741 929-225-3456 %^&*(UHGF h(*&^D^%&65678")

for number in phone_numbers:
    call(number, { "network":"SMS" })
    say("Heyo25!")
    hangup()
    wait(5000)
    
----------------------------------------------------------

def sep_phone_num(input_str_all_num):
    all_unformatted = input_str_all_num.split(" ")
    result = []
    for i in range(len(all_unformatted)):
        formatted = format_phone_num(all_unformatted[i])
        if formatted != "":
            result.append(formatted)
    return result

def format_phone_num(input_num):
    ASCII_0 = 48
    ASCII_9 = ASCII_0 + 9
    result = ""
    for ch in input_num:
        if ord(ch) >= ASCII_0 and ord(ch) <= ASCII_9:
            result += ch
    if len(result) == 10:
        return "+1" + result
    if len(result) == 11 and result[0] == '1':
        return "+" + result
    return ""

#phone_numbers = sep_phone_num("347-720-9741 929-225-3456 %^&*(UHGF h(*&^D^%&65678 8468446498 1111111111 22222***22222 347-720-9741 +1-848-989-1452 16584957823")
phone_numbers = sep_phone_num("347-720-9741 929-225-3456 %^&*(UHGF h(*&^D^%&65678 9739007783 9738564910 8625962048" )

for number in phone_numbers:
    call(number, { "network":"SMS" })
    say("Heyo30!")
    hangup()
    wait(5000)
    
----------------------------------------------------------

def sep_phone_num(input_str_all_num):
    all_unformatted = input_str_all_num.split(" ")
    result = []
    for i in range(len(all_unformatted)):
        formatted = format_phone_num(all_unformatted[i])
        if formatted != "":
            result.append(formatted)
    return result

def format_phone_num(input_num):
    ASCII_0 = 48
    ASCII_9 = ASCII_0 + 9
    result = ""
    for ch in input_num:
        if ord(ch) >= ASCII_0 and ord(ch) <= ASCII_9:
            result += ch
    if len(result) == 10:
        return "+1" + result
    if len(result) == 11 and result[0] == '1':
        return "+" + result
    return ""

#phone_numbers = sep_phone_num("347-720-9741 929-225-3456 %^&*(UHGF h(*&^D^%&65678 8468446498 1111111111 22222***22222 347-720-9741 +1-848-989-1452 16584957823")
phone_numbers = sep_phone_num("347-720-9741 929-225-3456 %^&*(UHGF h(*&^D^%&65678" )

for number in phone_numbers:
    call(number, { "network":"SMS" })
    say("Heyo30!")
    hangup()
    wait(5000)
    
----------------------------------------------------------

def sep_phone_num(input_str_all_num):
    all_unformatted = input_str_all_num.split(" ")
    result = []
    for i in range(len(all_unformatted)):
        formatted = format_phone_num(all_unformatted[i])
        if formatted != "":
            result.append(formatted)
    return result

def format_phone_num(input_num):
    ASCII_0 = 48
    ASCII_9 = ASCII_0 + 9
    result = ""
    for ch in input_num:
        if ord(ch) >= ASCII_0 and ord(ch) <= ASCII_9:
            result += ch
    if len(result) == 10:
        return "+1" + result
    if len(result) == 11 and result[0] == '1':
        return "+" + result
    return ""

for number in phone_numbers:
    call(number, { "network":"SMS" })
    say("Heyo30!")
    hangup()
    wait(5000)
    
----------------------------------------------------------

#https://api.tropo.com/1.0/sessions?action=create&token=4c6e5658457074684162456e464f5a476d55654361477a5753677373584952694e79786568776f4f676e6162&phone_numbers="347-720-9741  9176033714 9176965027"

----------------------------------------------------------

def sep_phone_num(input_str_all_num):
    all_unformatted = input_str_all_num.split(" ")
    result = []
    for i in range(len(all_unformatted)):
        formatted = format_phone_num(all_unformatted[i])
        if formatted != "":
            result.append(formatted)
    return result

def format_phone_num(input_num):
    ASCII_0 = 48
    ASCII_9 = ASCII_0 + 9
    result = ""
    for ch in input_num:
        if ord(ch) >= ASCII_0 and ord(ch) <= ASCII_9:
            result += ch
    if len(result) == 10:
        return "+1" + result
    if len(result) == 11 and result[0] == '1':
        return "+" + result
    return ""

message = "Heyo50"

try:
    all_phones_str
except NameError:
    message = "Heyo100"
    all_phones_str="347-720-9741 9176033714 9176965027"

phone_numbers = sep_phone_num(all_phones_str)

for number in phone_numbers:
    call(number, { "network":"SMS" })
    say(message)
    hangup()
    wait(5000)
    
----------------------------------------------------------    
----------------------------------------------------------    
----------------------------------------------------------    
----------------------------------------------------------    
----------------------------------------------------------    
----------------------------------------------------------    
----------------------------------------------------------    
----------------------------------------------------------    
----------------------------------------------------------



