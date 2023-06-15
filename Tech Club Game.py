import time
print("""Welcome to
TECH CLUB
The game of three children who find a superpower at school!""")
ingame=True
while ingame==True:
    Level=input("""





Choose the number of level you are up to, then press enter or return.
0 - Orientaion/Backstory
1 - Golden Gaming

OR type exit to finish the game.
>>> """)
    if Level == "0":
        print("""Three kids walked down the hallway. Their names were Charlie, Luna and Ashton.
You are Charlie.
You and your tech-savvy friends walked into the tech room, just like Chi, the tech man, asked.
He showed you to the back of the room and you saw a staircase.
"I've been waiting to show you this. The most high-tech area in the country. I hope you like it."
As you walk downstairs, you see a empty room.
"WHAT!?" you and your friends say. But Chi corrects you as he presses the power button...

Seats pop up from the floor. Hologram screens come up in front of you when you sit in the seat with... your name on it!!!
"You can choose a piece of tech to use - more specifically, the OS - from the supercomputer. Also, there's another way to get in and out so you can use it whenever you want!
Just make sure that you turn off the supercomputer when you are finished because this is runnung off the school's electricity.
I hope you like it, but you can't use it right now! I have to configure it! You'll be able to do it after I do that. Hopefully I can configure it before tommorrow."
And from that moment, Tech Club had started.

END ADVENTURE""")





    
    elif Level == "1":
        print("""You, Luna and Ashton turn on the supercomputer.
You really want to go home and play on your PS5 with your younger brother in Grade 2.
But you and your Year 8 friends got this supercomputer yesterday.
"My liitle brother is probably waiting for me at home. So we can play on my PS5" you say.
Little do you know, the supercomputer is so powerful, it can manipulate time.
Your friends do, though, and they tell you about it.
You agree to the plan.

"Let's go back to the past!" suggested Ashton.""")










    elif Level == "exit":
        print("""You turn off the supercomputer and walk home together.
You had a good day today.""")
        break
    else:
        print("ERROR MEM01: No adventures of index", Level,"exist in the C: drive. Try again.")
