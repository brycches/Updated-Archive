

chapters = 0
largeB=''
chapters1 = 0
largeB1 = ''

desiredS = input('which volume of scriptures would you like to learn about? (for example, Old Testament, New Testament, Book of Mormon, Doctrine and Covenants, Pearl of Great Price)')

with open("CSE110/week12/books_and_chapters.txt") as variable:
    for line in variable:
        parts = line.split(':')
        book = parts[0]
        chapter = parts[1]
        scripture = parts[2]
        chapter = int(chapter)
        if scripture.strip() == 'Book of Mormon':
            print (f'Scripture: {scripture.strip()}, Book: {book}, Chapters: {chapter}')
        if chapter > chapters and scripture.strip() == 'Book of Mormon':
            chapters = chapter
            largeB = book
        if chapter > chapters and scripture.strip() == desiredS:
            chapters1 = chapter
            largeB1 = book

print(f'The book of {largeB} contains {chapters} chapters, the largest of any book in the book of mormon.')
print(f'The book of {largeB1} contains {chapters} chapters, the largest in The {desiredS}, the book of scripture you wanted to learn more about.')


        