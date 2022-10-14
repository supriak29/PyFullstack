def battingscore(data):
    """This function calculates batting score of players"""

    # fetch the details first:
    name=data.get('name')
    runs=data.get('runs')
    balls=data.get('balls')
    four=data.get('4')
    six=data.get('6')

    # 1 point for 2 runs scored
    batscore = int(runs/2)
    
    # additional 5 points for half-century
    if batscore>=50:
        batscore+=5
    # additional 10 points for century
    if batscore>=100:
        batscore+=10

    # 2 points for strike rate(runs/balls faced) of 80-100
    if runs>0:
        strike_rate = runs*100/balls
        if strike_rate>=80 and strike_rate<100:
            batscore+=2
        # additional 4 points for strike rate>100
        if strike_rate>=100:
            batscore+=4

    # 1 point for four
    batscore+=four
    # 2 point for six
    batscore=batscore+(six*2)

    # return name of player and his batting score
    return({'name':name,'batscore':batscore})

def bowlingscore(data):
    """This function calculates balling score of players"""
    name=data.get('name')
    wicket=data.get('wkts')
    over=data.get('overs')
    runs=data.get('runs')
    field=data.get('field')

    # 10 points for each wicket
    bowlscore = wicket*10

    # additional 5 points for 3 wickets in innings
    if wicket>=3:
        bowlscore+=5
    # additional 10points for 5 wickets or more in innings
    if wicket>=5:
        bowlscore+=10

    # 4 points for economy rate(runs given per over) between 3.5-4.5
    economy_rate = runs/over
    if economy_rate>3.5 and economy_rate<=4.5:
        bowlscore+=4
    # 7 points for economy rate between 2 and 3.5
    if economy_rate>2 and economy_rate<=3.5:
        bowlscore+=7
    # 10 points for an economy rate less than 2
    if economy_rate<=2:
        bowlscore+=10

    return({'name':name,'bowl score':bowlscore})
