import valid_parentheses

def test(s:str, output: bool):
    assert valid_parentheses.valid_parentheses(s) == output
    print("Input: s = " + str(s))
    print("Output: " + str(valid_parentheses.valid_parentheses(s)))    
    
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