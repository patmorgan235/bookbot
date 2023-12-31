

def main():

    path_to_file = "books/frankenstein.txt"

    with open(path_to_file) as f:
        file_contents = f.read()

    print(f"Number of Words: {countwords(file_contents)}")

    print("Occurance of each charater\n")
    
    book_charaters = countcharaters(file_contents)
    book_letters= list(book_charaters)
    book_letters.sort()

    for i in book_letters:
        if i.isalpha():
            print(f"The '{i[0]}' character was found {book_charaters[i]} times")

def countwords(book):
    book = book.split()
    return len(book)

def countcharaters(book):
    results = dict()
    for b in book.lower():
        if b not in results.keys():
            results[b] = 1
        else:
            results[b] += 1
    return results


main()