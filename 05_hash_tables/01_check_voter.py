def check_voter(voted_, voter):
    if voter in voted_:
        print(voter + " already voted!")
        return

    voted_.add(voter)
    print(voter + " voting for the first time")


voted = set()
check_voter(voted, "jim")
check_voter(voted, "tom")
check_voter(voted, "mike")
check_voter(voted, "jim")
