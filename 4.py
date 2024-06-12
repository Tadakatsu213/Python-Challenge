def counting_votes(filepath:str)-> None:
    with open(filepath) as d:
        votes={}
        headers = d.readline()
        for line in d:
            line=line.strip().split(',')
            if line[2] in votes:
                votes[line[2]]=votes.get(line[2])+1
            else:
                votes[line[2]]=1
        total_votes= sum(votes.values())
        contestants= [ name for name in votes.keys()]
        print(f'''Election Results
           
--------------------------


Total Votes: {total_votes}


---------------------------


{contestants[0]}: {calcute_percentage(votes,contestants[0])}% ({votes[contestants[0]]})


{contestants[1]}: {calcute_percentage(votes,contestants[1])}% ({votes[contestants[1]]})


{contestants[2]}: {calcute_percentage(votes,contestants[2])}% ({votes[contestants[2]]})


---------------------------


Winner:{get_winner(votes)}


---------------------------
            ''')
def calcute_percentage(numbers:dict,name) ->int:
    return round((numbers.get(name))/sum(numbers.values())* 100,3)


def get_winner(votes:dict):
    max_value=0
    winner=""
    for name ,number in votes.items():
        if number> max_value:
            max_value=number
            winner=name
    return winner










if __name__ == '__main__':
    counting_votes('PyPoll\Resources\election_data.csv')
