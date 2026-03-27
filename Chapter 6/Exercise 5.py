s='X-DSPAM-Confidence:0.8475'
a=s.find(':')
b=s[a+1:]
print(float(b))
print(type(b))
