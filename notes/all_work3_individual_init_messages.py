
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

message = "Your Package is Ready for Pickup. Thank you for using LCL Enterprise!"

try:
    all_phones_str
except NameError:
    message = "Problem with HTTP request"
    all_phones_str="347-720-9741 9176033714 9176965027"

phone_numbers = sep_phone_num(all_phones_str)

for number in phone_numbers:
    call(number, { "network":"SMS" })
    say(message)
    hangup()
    wait(5000)

-------------------------------------------------------------------------

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

message = ""

try:
    phone_number
    cargo_id
except NameError:
    message = "Problem with HTTP request"
    phone_number = format_phone_num("347-720-9741")
else:
    message = "Hi, your package is shipped with ID: " + cargo_id + ". You will recieve a text when it has arrived. -LCL Enterprise Team"

call(phone_number, { "network":"SMS" })
say(message)
hangup()
wait(500)

-------------------------------------------------------------------------

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

message = ""

try:
    phone_number
    cargo_id
except NameError:
    message = "Problem with HTTP request"
    phone_number = format_phone_num("347-720-9741")
else:
    message = "Hi, your package has been put in cargo container: " + cargo_id + ". You will recieve a text when it has arrived. -LCL Enterprise Team"

call(phone_number, { "network":"SMS" })
say(message)
hangup()
wait(500)





