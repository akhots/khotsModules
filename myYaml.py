# Developed by Alexander Khotsianivsky
# Version 0.9 beta

def myYaml(ld, ind=0, lst=False):
    if type(ld) == list:
        for i in ld:
            myYaml(i, ind, lst=True)
    elif type(ld) == dict:
        for k in ld:
            if type(ld[k]) == dict:
                print('  '*(ind-1*lst) + '- '*lst + str(k) + ':')
                myYaml(ld[k], ind+1)
            elif type(ld[k]) == list:
                print('  '*(ind-1*lst) + '- '*lst + str(k) + ':')
                myYaml(ld[k], ind+1, lst=True)
            else:
                print('  '*(ind-1*lst) + '- '*lst + str(k) + ': ' + str(ld[k]))
            if lst: lst=False
    else:
        print('  '*(ind-1*lst) + '- '*lst + str(ld))
    if lst: lst=False

