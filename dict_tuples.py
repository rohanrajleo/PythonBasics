stocks = {"infosys": [600,630,620], "rilence": [1430,1490,1567],
          "tata" : [234,180,160]}    #dict but value is a list
prompt = input ("ENTER : ")
if prompt=="print":
    for k,v in stocks.items():
        print (f"{k}==>{v}")
elif prompt == "add":
    company = input ("Enter Company Name : ").lower()
    price = int (input ("Enter stock price : "))
    if company in stocks:
        stocks[company].append(price)
        print (stocks)
    else :
        stocks [company]= [price] #[sq bracket] to initialize a list
        for k in stocks:
            print (f"{k}==> {stocks[k]}") 