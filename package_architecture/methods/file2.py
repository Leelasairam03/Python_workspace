class State:
    president='Droupadi Murmu'
    currency='rs'

    @classmethod
    def display_country(cls):
        print(cls.president)
        print(cls.currency)
    
    @classmethod
    def elect_president(cls,new_president):
        cls.president=new_president

State.display_country()
print("--------------------------------")
State.elect_president("balram")
print(State.president)

