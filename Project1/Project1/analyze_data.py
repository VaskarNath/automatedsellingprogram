import pandas as pd
import openpyxl

def analyze_data():
    with open("../../data.csv", 'rb') as f:

        df_posted_books = pd.read_csv(f, names=["title", "price", "author"], encoding='cp1252')
        book_titles = df_posted_books["title"].tolist()
        price = df_posted_books["price"].tolist()


        df_books = pd.read_csv("../../bookscatelogue.csv", names=["title", "edition", "author"])

        titles = df_books["title"].tolist()
        author = df_books['author'].tolist()
        editions = df_books['edition'].tolist()

        book_avg_price = {}
        numbers = []
        authors = []
        edition = []
        for i in range(len(titles)):
            if titles[i] not in book_avg_price:
                book_avg_price[titles[i]] = 0
                num = 0
                for j in range(len(book_titles)):
                    if titles[i] in book_titles[j]:
                        if price[j] != 0:
                            num += 1
                            book_avg_price[titles[i]] += int(price[j])
                if num != 0:
                    book_avg_price[titles[i]] /= num
                numbers.append(num)
                authors.append(author[i])
                edition.append(editions[i])



        df = pd.DataFrame(data=book_avg_price, index=[0])
        df = df.T
        df["nums"] = numbers
        df["author"] = authors
        df["edition"] = edition
        df.to_excel('output.xlsx')



if __name__ == "__main__":
    analyze_data()
