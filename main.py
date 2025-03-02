from src.Crawler import Crawler

if __name__ == "__main__" :  
    crawler = Crawler()
    keyword = input("Please input the keyword : ")
    count = int(input("Please input data count : ")) or 10
    crawler.execute(keyword=keyword, count=count)
