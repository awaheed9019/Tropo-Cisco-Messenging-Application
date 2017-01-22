

phone_numbers = ["+13477209741", "+19292253456"]
for number in phone_numbers:
    call(number, { "network":"SMS" })
    say("Heyo4!")
    hangup()
    wait(3000)
