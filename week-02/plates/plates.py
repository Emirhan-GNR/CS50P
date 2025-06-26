def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s)>=2 and len(s)<=6:
        if s[0].isalpha() and s[1].isalpha():
            if s.isalnum():
                for i in range(len(s)):
                    if s[i].isdigit():
                        if s[i] == "0":
                            return False
                        elif not s[i:].isdigit():
                            return False
                        else:
                            break
                return True
            else:
                return False        
        else:
            return False
    else:
        return False

main()