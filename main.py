import pickle
from os import listdir
import random
import hashlib


class Idea:
    def __init__(self, name, desc, link):
        self.name = name
        self.desc = desc
        self.link = link
        self.picked = 0

    def idea_id(self):
        m = hashlib.sha256()
        m.update(bytes(self.name, "utf-8"))
        return m.hexdigest()

    def pick(self):
        self.picked += 1

    def __repr__(self):
        return (
            "name: "
            + self.name
            + "\ndesc: "
            + self.desc
            + "\nlink: "
            + self.link
            + "\npicked: "
            + str(self.picked)
        )


def add() -> Idea:
    name = input("Name: ")
    desc = input("Desc: ")
    link = input("Link: ")

    idea = Idea(name, desc, link)
    return idea


def save(idea: Idea):
    with open(f"new/{idea.idea_id()}", "wb") as f:
        pickle.dump(idea, f)


def open_one():
    files = list(listdir("new/"))
    file = random.choice(files)

    with open(f"new/{file}", "rb") as f:
        idea = pickle.load(f)
        print(idea)

    idea.pick()
    save(idea)


if __name__ == "__main__":
    mode = input("(A)dd or (P)ick: ")
    if mode.upper() == "A":
        i = add()
        save(i)

    elif mode.upper() == "P":
        open_one()
