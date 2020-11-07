import sys
import re
bacon = {
    'aaaaa':'a','aaaab':'b','aaaba':'c','aaabb':'d','aabaa':'e','aabab':'f','aabba':'g',
    'aabbb':'h','abaaa':'i','abaab':'j','ababa':'k','ababb':'l','abbaa':'m','abbab':'n',
    'abbba':'o','abbbb':'p','baaaa':'q','baaab':'r','baaba':'s','baabb':'t','babaa':'u',
    'babab':'v','babba':'w','babbb':'x','bbaaa':'y','bbaab':'z'
}
a=raw_input()
a=a.strip()
a=a.lower()
a=re.findall(r'.{5}', a)
length=len(a)
for i in range(length):
    if bacon.has_key(a[i]):
        sys.stdout.write(bacon[a[i]])
    else:
        sys.stdout.write("*")