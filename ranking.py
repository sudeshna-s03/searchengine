from _typeshed import self
from operator import itemgetter
import string
class Ranking:
    def __init__(self,results,query):
        self.results = results
        self.query = query
    def serach(self):
        res=[]
        filtered=[]
        if '""' in self.query:
            x= '""'
            y= ' '
            z= ' "" '
            mytable= self.query.maketrans(x,y,z)
            res.insert(0, self.query.translate(mytable))
        else:
            if ':' in self.query:
                if ':' in self.query:
                    key= self.query.spilt(':')[0]
                    fil= self.query.split(':'[1])
                    print(key)
                    print(fil)
                    for result in self.results:
                        if fil.lower() not in result['title'].lower() or fil.lower() not in result['description'].lower():
                            filtered.append(result)
                    self.results = filtered
            elif '-' in self.query:
                if '-' in self.query:
                    key= self.query.spilt('-')[0]
                    fil= self.query.split('-'[1])
                    for result in self.results:
                        if fil.lower() not in result['title'].lower() or fil.lower() not in result['description'].lower():
                            filtered.append(result)
                    self.results = filtered
            else:
                key= self.query
            res= key.split()
        return res
            
    def ranked_results():
        keywords= self.serach()
        for key in keywords:
            for result in self.results:
                if key.lower() in result['title'].lower():
                    result['score'] +=1
        return self.results
    def sorted_results(self):
        ranked_searches = self.ranked_results()

        sorted_searches = sorted(
            ranked_searches, key=itemgetter('popularity', 'score'), reverse=True)

        return sorted_searches
    