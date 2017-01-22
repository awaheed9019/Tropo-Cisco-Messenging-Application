
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

