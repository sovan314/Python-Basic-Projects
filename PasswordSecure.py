

secure =(('s','$'),('a','@'),('h','#'),('i','!'))
def pass_secure(gen):
    for m,n in secure :
        gen=gen.replace(m,n)
    return gen
if __name__ == "__main__":
    gen = input("Enter the PASSWORD which you want to secure:")
    gen = pass_secure(gen)
print(f"secured form your password is {gen}")


