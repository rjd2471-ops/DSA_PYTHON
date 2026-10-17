#Ques Isomorfing string.

s = "PAPERPE"

t = "TITLESL"

s_to_t = {}
t_to_s = {}

for i in range(len(s)):

    if s[i] not in s_to_t:
        s_to_t[s[i]] = t[i]
    elif s_to_t[s[i]] != t[i]:
        print(False)
        break

    if t[i] not in t_to_s:
        t_to_s[t[i]] = s[i]
    elif t_to_s[t[i]] != s[i]:
        print(False)
        break

else:
    print(True)