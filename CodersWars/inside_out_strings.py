# You are given a string of words (x), for each word within the string you need to turn the word 'inside out'.
# By this I mean the internal letters will move out, and the external letters move toward the centre.
#
# If the word is even length, all letters will move. If the length is odd,
# you are expected to leave the 'middle' letter of the word where it is.
#
# An example should clarify:
#
# 'taxi' would become 'atix' 'taxis' would become 'atxsi'

def inside_out(st):
    res = []
    for i in st.split(' '):
        if len(i) < 4:
            res.append(i)
        elif len(i) % 2 == 0:
            center = int(len(i)/2)
            p1 = i[:center][::-1]
            p2 = i[center:][::-1]
            res.append(f'{p1+p2}')
        else:
            center = int(len(i)/2)
            p1 = i[:center][::-1]
            p2 = i[center+1:][::-1]
            print(i[center])
            res.append(f'{p1+i[center]+p2}')
    return ' '.join(res)

print(inside_out('taxi michal magda'))