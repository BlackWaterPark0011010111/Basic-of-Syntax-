books = {
  'Harry Potter And The Sorcerers Stone': 1241100000,
  'Harry Potter And The Chamber Of Secrets': 771300000,
  'Harry Potter And The Prisoner Of Azkaban': 65210000,
  'Harry Potter And The Goblet Of Fire': 645600000,
  'Harry Potter And The Order Of The Phoenix': 635600000,
  'Harry Potter And The Half Blood Prince': 661300000,
  'Harry Potter And The Deathly Hallows ': 652200000,
}
sales = []
book = []
for key,value in books.items():
    sales.append(value)
    book.append(key)
print(sales)
print(book)
booksList = zip(book,sales)
print(booksList)