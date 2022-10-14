from score import battingscore, bowlingscore

# list of dictionary who are batters
bat = [ {
            'name':'Virat Kohli',
            'role':'bat',
            'runs':112,
            '4':10,
            '6':0,
            'balls':119,
            'field':0
        },   
        {
            'name':'du Plessis',
            'role':'bat',
            'runs':120,
            '4':11,
            '6':2,
            'balls':112,
            'field':0
        }
    ]

# list of dictionary who are bowlers
ball = [    {
                'name':'Bhuvneshwar Kumar',
                'role':'bowl',
                'wkts':1,
                'overs':10,
                'runs':71,
                'field':1
            },

            {
                'name':'Yuzvendra Chahal',
                'role':'bowl',
                'wkts':2,
                'overs':10,
                'runs':45,
                'field':0
            },
            
            {
                'name':'Kuldeep Yadav',
                'role':'bowl',
                'wkts':3,
                'overs':10,
                'runs':34,
                'field':0
            }
    ]

for i in bat:
    print(battingscore(i))
for i in ball:
    print(bowlingscore(i))
