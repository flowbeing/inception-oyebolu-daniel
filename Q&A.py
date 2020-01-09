questions = [
    "1. ___ For the team for six years, he decided to join another"
    "\na. When he played "
    "\nb. Playing "
    "\nc. Having played "
    "\nd. In playing "
    "\ne. When he was playing"
    "\n",

    "2. The bridge connecting the two cities was ___ by the enemy"
    "\na. blown up"
    "\nb. blown down"
    "\nc. blown off "
    "\nd. blown over"
    "\ne. blown away"
    "\n",

    "3. The little boy is duffering ____ jaundice"
    "\na. from"
    "\nb. of"
    "\nc. for"
    "\nd. with"
    "\ne. by"
    "\n",

    "4. They went to the market and bought a suitcase and ___ bag"
    "\na. a big leather brown"
    "\nb. a leather brown big"
    "\nc. a big brown leather"
    "\nd. a brown big leather"
    "\ne. a leather big brown"
    "\n",

    "5. By the end of this year ___ in this town for eleven years"
    "\na. I'm living"
    "\nb. I'd be living"
    "\nc. I'll live"
    "\nd. Ill have lived"
    "\ne. I have lived"
    "\n"
]

Answers = [
    "c",
    "a",
    "a",
    "c",
    "d",
]


def initiator():
    score = 0;
    for question in questions:
        answer = input(question + "\nEnter answer: ")

        if answer == Answers[questions.index(question)]:
            print("Correct!")
            print("")
            score += 1

        else:
            print("Not Correct")
            print("")

    print("You scored " + str(score) + " out of " + str(len(questions)))


initiator()
