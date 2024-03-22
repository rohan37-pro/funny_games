import random

class strategy():
    def _random_(n):
        # this strategy is for randomly choosing
        choose = random.randint(0,n-1)
        switch = random.choice([True, False])
        return choose, switch
    
    def sick_to_original_choice(n):
        choose = random.randint(0,n-1)
        switch = False
        return choose, switch
    
    
    def always_switch(n):
        choose = random.randint(0,n-1)
        switch = True
        return choose, switch