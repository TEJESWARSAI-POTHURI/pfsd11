import random,string
n=random.randbytes(5)
print(n)

print(random.randrange(1,8))

mylist=("sdfa","safdf","sfaf","sdfa")
mulist1={"sdfa","safdf","sfaf","sdfa"}
mylist1=["sdfa","safdf","sfaf","sdfa"]
print(random.choice(mylist))

print(random.shuffle(mylist1))

S=5
ran=''.join(random.sample(string.ascii_uppercase+string.digits,k=S))
print(ran)

s1=4
ran1=''.join(random.sample(string.digits,k=6))
print(ran1)