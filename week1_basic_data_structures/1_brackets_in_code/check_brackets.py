# python3

# from collections import namedtuple

# Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    pos = 0
    for i, next in enumerate(text):
        pos = i + 1
        if next in "([{":
            opening_brackets_stack.append((pos, next))
        if next in ")]}":
            if len(opening_brackets_stack) == 0:
                opening_brackets_stack.append((pos, next))
                break
            if are_matching(opening_brackets_stack[-1][1],  next):
                opening_brackets_stack.pop()
            else:
                opening_brackets_stack.append((pos, next))
                break

    if len(opening_brackets_stack) > 0:
        return opening_brackets_stack[-1][0]
    else:
        return "Success"

def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()