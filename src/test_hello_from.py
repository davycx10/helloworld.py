from hello_from import helloFrom
from hello_to import helloTo

def test1():
    result1 = helloFrom("Bob")
    assert result1 == "Bob say Hello !"

def test2():
    result2 = helloFrom("Jim")
    assert result2 != "Bob say Hello !"
    
def test3():
    result3 = helloTo("Bob", 3)
    assert len(result3)== 3  ## Utilisation de len() pour vérifier la longueur 
    for entry in result3:
        assert entry == "Hello, Bob !"
    
def main():
    print("Running test 1")
    test1()
    print("Success")
    
    print("Running test 2")
    test2()
    print("Success")
    
    print("Running test 3")
    test3()
    print("success")
    

if __name__ == '__main__':
    main()