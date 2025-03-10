def showcards():
    flashcards = {
        'Python': 'a programming language',
        'Function': 'a block of code that rurn when called',
        'Loop': 'the way to repeat actions in a program',
        'Variable': 'a place to store data',
    }

    for term, definition in flashcards.items():
        print(f"{term}: {definition}")
        print("PRESS ENTER TO SEE THE NEXT TERM.....")
