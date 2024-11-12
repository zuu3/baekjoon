def f(msg):
    msg_map = {
        "CU": "see you",
        ":-)": "I’m happy",
        ":-()": "I’m unhappy",
        ";-)": "wink",
        ":-P": "stick out my tongue",
        "(~.~)": "sleepy",
        "TA": "totally awesome",
        "CCC": "Canadian Computing Competition",
        "CUZ": "because",
        "TY": "thank-you",
        "YW": "you’re welcome",
        "TTYL": "talk to you later"
    }
    
    if msg in msg_map:
        msg = msg_map[msg]
        
    return msg



while True:
    try: msg = input()
    except EOFError: break
    print(f(msg=msg))