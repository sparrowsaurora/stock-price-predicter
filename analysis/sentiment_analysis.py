class Sentiment:
    def __init__(self):
        self.sentiment:float = 0
        # A value -10 to 10 showing public sentiment of a stock.
        self.MIN, self.MAX = -10, 10
        # min and max value for sentiment
    
    def __repr__(self):
        return f"Sentiment is at {self.sentiment * 10}%"
    
    def change_sentiment(self, value:float):
        self.sentiment += value
        self.sentiment = 10 if self.sentiment >= 10 else self.sentiment
        self.sentiment = -10 if self.sentiment <= -10 else self.sentiment
        print(self.sentiment)
            
    def get_sentiment(self):
        '''
            Get sentiment for all news about stock from twitter or reddit.
        '''
        news = []
    
    def return_sentiment(self):
        return self.sentiment
    
    

# s = Sentiment()
# s.change_sentiment(9)
# s.change_sentiment(-20)

# print(s)
