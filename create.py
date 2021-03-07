import os
import sys
from dotenv import load_dotenv

load_dotenv()

path = os.getenv("FILEPATH")


def create():
    folderName = str(sys.argv[1])
    os.makedirs(path + str(folderName))


if __name__ == "__main__":
    create()
