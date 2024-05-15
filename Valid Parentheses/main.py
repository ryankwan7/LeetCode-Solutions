import valid_parentheses

def test(s:str, output: bool):
    result = valid_parentheses.valid_parentheses(s)
    assert result == output
    print("Input: s = " + str(s))
    print("Output: " + str(result) + "\n")    
    
def main():
    s = "()"
    output = True
    test(s, output)

    s = "()[]{}"
    output = True
    test(s, output)

    s = "(]"
    output = False
    test(s, output)

if __name__ == "__main__":
    main()