
class Evaluator:
    @staticmethod
    def zip_evaluate(coefs, words):
        if(len(coefs) != len(words)):
            return -1
        both = zip(coefs, words)
        sum = 0
        for x, y in both:
            sum += x * len(y)
        return sum
        
    @staticmethod
    def enumerate_evaluate(coefs, words):
        if(len(coefs) != len(words)):
            return -1
        both = enumerate(words)
        sum = 0
        for x, y in both:
            sum += coefs[x] * len(y)
        return sum
    
# words = ["Le", "Lorem", "Ipsum", "est", "simple"]
# coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
# print(Evaluator.zip_evaluate(coefs, words))
# print(Evaluator.enumerate_evaluate(coefs, words))