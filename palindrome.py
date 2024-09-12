# Palindrome

def main():
    # Skriv din lösning här nedan. Byt ut "pass" mot din kod.
    pass

if __name__ == "__main__":
    main()

def palindromecheck(a):
    return a == a[::-1]

text=str(input("Skriv något för att se om det är palindrom: "))
a= palindromecheck

if a: 
    print ("japp")
else:
    print ("nej")



