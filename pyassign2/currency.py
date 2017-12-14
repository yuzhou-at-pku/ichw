def exchange_convert(exchange_str):
    """The format of input is "from=source&to=target&amt=amount"
    parameter:the string to slice
    returns:2 Substrings and a float."""
        
    exchange_list=exchange_str.split("=")
    exchange_to=[]
    for i in range(len(exchange_list)):
        exchange_to +=(str(exchange_list[i]).split("&"))
    currency_from=exchange_to[1]
    currency_to=exchange_to[3]
    amount_from=float(exchange_to[5])
    return (currency_from,currency_to,amount_from)


def currency_response(currency_from,currency_to,amount_from):
    """In this procedure ,data input will make a call to the target webset,and a string
    containing relating information will be put out.
    parameter:currency_from(str);currency_to(str):amount_from(float)
    return:a string from the target webset"""
     
    from urllib.request import urlopen
    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from={}&to={}&amt={}'.format(currency_from,currency_to,amount_from))
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    return jstr

def get_from_and_to(data_feedback):
    """This procedure is used for fetching the information recieved from the target
    webset,and transform it into a tuple.
    parameter:the string from the webset
    return:a tuple including amount_from,currency_from and amount_to,currency_to"""
    
        
    if "false" in data_feedback:
        print("Error,the format of data input is wrong")
        return exit(1)
    else:
        data_feedback=str(data_feedback).split("\"")
        list_get=[]
        for i in range(len(data_feedback)):
            if (data_feedback[i]+" ")[0].isdigit():
                list_get.append(data_feedback[i])
        tuple_get=tuple(list_get)
        return tuple_get

def exchange_main(currency):
    """In this module, the modules we write is integrated together.And the final
    result is given.
    parameter:string with the format of "from=source&to=target&amt=amount"
    return:a float of the amount exchangeg to"""
    currency_from=exchange_convert(currency)[0]
    currency_to=exchange_convert(currency)[1]
    amount_from=exchange_convert(currency)[2]
    exchange_feedback=currency_response(currency_from,currency_to,amount_from)
    amount_to_str=get_from_and_to(exchange_feedback)[1].split(" ")[0]
    amount_to=float(amount_to_str)
    return amount_to

def main():
    print("The format of your input should be:from=source&to=target&amt=amount")
    currency_ex=input()
    print(exchange_main(currency_ex))
    input()

if __name__=="__main__":
    main()	