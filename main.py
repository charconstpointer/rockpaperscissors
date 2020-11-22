from rps import RPS


def translate(throw: int):
    trans = {
        0: 'rock',
        1: 'paper',
        2: 'scissors'
    }
    return trans[throw]


def main():
    rps = RPS()
    while True:
        print("rock", 0, "paper", 1, "scissors", 2)
        i = input()
        ans = rps.answer(i)
        print("you : ", translate(int(i)), "me : ", translate(ans))
        print(rps.get_ratio())


def parse_answer(answer: int):
    answers = [0, 1, 2]
    return answers.__contains__(answer)


if __name__ == '__main__':
    main()
