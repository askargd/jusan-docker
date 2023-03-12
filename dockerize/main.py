from fastapi import FastAPI, Query, HTTPException

app = FastAPI()



elements = list()


# get sum1n
@app.get("/sum1n/{n}")
def get_sum1n(n: int):
    n=(n*(n+1)//2)
    return{"result": n}


# get fibo
@app.get("/fibo")
def get_fibo(n: int = Query(...)):
    n1=0
    n2=1
    count = 1
    if n <= 0:
        print ("Please enter a positive integer")
    elif n == 1:
        print('First number in fibonacchi sequence is 0')
    else:
        while count < n:
            nth=n1+n2
            #new values
            n1=n2
            n2=nth
            count += 1
        return{"result":n1}


# reverse a text
@app.post("/reverse")
def post_reverse(string: str = Query(...)):
    return{"result": string[-1::-1]}


# put data into list

@app.put("/list/{element}")
def put(element):
    elements.append(element)
    print(elements)
    return {"result":element}

# get data from list
@app.get("/list")
def get_elements():
    return{"result":elements}



#calculator
@app.post("/calculator")
def post(expr: str):  
    expr = expr.split(',')
    expr = int(expr[0]),str(expr[1]),int(expr[2])
    if expr[1] not in ["+","-","*","/"]:
        raise HTTPException(status_code=400, detail="invalid")
    if expr[1] == "/" and expr[2] == 0:
        raise HTTPException(status_code=403, detail="zerodiv")
    elif expr[1] == "+":
        num3 = expr[0] + expr[2]
    elif expr[1] == "-":
        num3 = expr[0] - expr[2]
    elif expr[1] == "*":
        num3 = expr[0] * expr[2]
    elif expr[1] == "/":
        num3 = expr[0] / expr[2]
    return(num3)