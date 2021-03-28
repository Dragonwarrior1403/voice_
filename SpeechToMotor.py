import Motor as move
import voice
import time

def FollowCommand():
    command = voice.text_from_audio(dur=2, lang='en-US', off=0)
    firstLetter = command[0].lower()
    if firstLetter == "f":
        move.move_forward(60)
        time.sleep(1.5)
    elif firstLetter == "b":
        move.move_backward(60)
        time.sleep(1.5)
    elif firstLetter == "l":
        move.turn_on_spot(45, 'left')
        time.sleep(0.5)
    elif firstLetter == "r":
        move.turn_on_spot(45, 'right')
        time.sleep(0.5)
    else:
        voice.text_to_audio("Say that again you muppet", 'male', 150)

if __name__ == '__main__':
    for x in range(0,5):
        FollowCommand()

