import sys


if __name__ == '__main__':
    query = str()
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            query += arg + ' '
    if query == '':
        query = 'Introduce yourself by only using tool named "find_information_about_the_assistant".'
    print(query)