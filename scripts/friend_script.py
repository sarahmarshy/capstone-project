import pandas as pd

def main():
    df = pd.read_csv('../../data/PhoneNumberTransactionsSeptember.txt', sep='\t')
    df2 = df.query('HashedUserPhoneNumber in HashedExternaLPhoneNumber')
    caller_groups = df2.groupby('HashedExternaLPhoneNumber')
    for caller,called in caller_groups:
        for user in set(called['HashedUserPhoneNumber'].tolist()):
            if user in caller_groups.groups and caller in caller_groups.get_group(user)['HashedUserPhoneNumber'].tolist():
                indexes = called.loc[called['HashedUserPhoneNumber'] == user].index.tolist()
                df.loc[indexes,'Friend']=1
    print df.loc[df["Friend"]==1]

main()