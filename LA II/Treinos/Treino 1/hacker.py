def hacker(log):

    pin_copy = ""
    pin_cracker = ""
    mail_card = {}
    resp=[]

    for tuplo in log:
        if tuplo[1] not in mail_card:
            mail_card[tuplo[1]] = tuplo[0]
        elif tuplo[1] in mail_card:
            pin_copy = mail_card[tuplo[1]]
            pin_cracker = ""
            for i in range(16):
                if tuplo[0][i] != "*":
                    pin_cracker += tuplo[0][i]
                else:
                    pin_cracker += pin_copy[i]
            mail_card[tuplo[1]] = pin_cracker
            
    for mail in mail_card:
        resp.append((mail_card[mail],mail))

    resp.sort(key=lambda x: x[1])
    resp.sort(key=lambda x: x[0].count("*"))

    return resp

# 100 %

