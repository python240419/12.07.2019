
sen = "I love to eat ice cream in the beach"

'''
• לייצר רשימה של המילים באותיות גדולות
• לייצר רשימה של אותיות- מהאות הראשונה בכל מילה
• לייצר רשימה של אותיות- מהאות השלישית בכל מילה )היכן שאפשר(
• לייצר רשימה של מספרים אשר מייצגים אורך של כל מילה ומילה
'''

print([w.upper() for w in sen.split()])
print([w[0] for w in sen.split()])
print([w[2] for w in sen.split() if len(w) >= 3])
print([len(w) for w in sen.split()])
print([10**n for n in range(1, 10)])

'''
כתוב פונקציה tryGetValue אשר מקבלת מילון + מפתח ובודקת אם המפתח קיים במילון. אם כן
היא מחזירה את ערכו אחרת- מחזירה N
'''

def tryGetValue(d, k):
    '''
    check if k exists in d
    :param d: dictionary
    :param k: key
    :return: value if key exists, otherwise None
    '''
    if k in d.keys():
        return d[k]
    else:
        return None

'''
כתוב פונקציה getSortedKeys אשר מקבלת מילון ומחזירה את רשימת המפתחות הממויינת של
אותו המילון 
'''
def getSortedKeys(d):
    '''
    return sorted keys of a given dictionary
    :param d: dictionary
    :return: sorted keys
    '''
    return sorted(d.keys())

'''
כתוב פונקציה mergeDictionary אשר מקבלת שני מילונים כפרמטר, ומחזירה מילון אחד המורכב
ממיזוג של ערכי שני המילונים שהתקבלו
'''
def mergeDictionary(d1, d2):
    '''
    returned combined dictionary of two gievn dictionary
    :param d1: first dictionary
    :param d2: second dictionary
    :return: combined dictionary
    '''
    result = d1.copy()
    for k in d2.keys():
        if result.get(k) == None:
            result[ k ] = d2[ k ]
        else:
            result[k] = [ d1[ k ] , d2 [ k ] ]
    return result

print(mergeDictionary( {1:1, 3:3}, {2:2, 3:4} ))

'''
כתוב תוכנית אשר קולטת מהמשתמש שני ערכים: מס' תעודת זהות + שם מלא. תעודת הזהות
תשמש בתור המפתח במילון, והשם שנקלט ישמש בתור הערך. ראשית בדוק אם מפתח זה קיים
במילון- אם כן, אל תדרוס את הערך הקיים והצג הודעה. אם המפתח לא קיים- הוסף ערך זה
למילון. חזור על הפעולה עד אשר המשתמש יכניס 1 -עבור מספר תעודת הזהות. לאחר שיסתיימו
כל הקלטים- הדפס את כל ערכי המילון שנצברו: מפתח + ערך
'''

d = {}
id = input("Please enter your ID: ")
while id != '-1':
    name = input("Please enter your name: ")

    if d.get(id) == None:
        d [ id ] = name
    else:
        print(f'key {id} already exists!')

    id = input("Please enter your ID: ")

for k,v in d.items():
    print(f'{k} : {v}')

