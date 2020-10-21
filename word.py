from urllib.request import urlopen


def fetch_word():

    story = urlopen('http://sixty-north.com/c/t.txt')
    story_works = []
    for line in story:
        line_works = line.decode('utf-8').split()
        for word in line_works:
            story_works.append(word)
    story.close()

    for word in story_works:
        print(word)

if __name__ == '__main__':
    fetch_word()
