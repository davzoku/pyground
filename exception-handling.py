try: 
    momAge=20
    sonAge= 30
    if sonAge > momAge: 
        raise Exception

except Exception as e:
    print('ERR: The age gap does not tally')
    
else:
    ageGap = momAge - sonAge
    print('Mom is older by', ageGap)
    
finally:
# finally is always executed
    print('Mom is', momAge, 'Son is', sonAge)
