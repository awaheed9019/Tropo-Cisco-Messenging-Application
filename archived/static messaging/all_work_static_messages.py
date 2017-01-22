
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
----------------------------------------------------------
----------------------------------------------------------
----------------------------------------------------------
----------------------------------------------------------
----------------------------------------------------------
----------------------------------------------------------

