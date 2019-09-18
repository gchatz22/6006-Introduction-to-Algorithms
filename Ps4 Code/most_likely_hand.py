def most_likely_hand(D, k):
    '''
    Input:  D | string of length n representing the deck
            k | integer representing hand size
    Output: H | string of length k representing the most likely hand
    '''

    words = {}
    i = 1
    letters = [0]*26

    curr = list(D[:k])

#     start of constructing the slices

    for el in curr:
        letters[ord(el)-97] += 1
    words[0] = tuple(letters)
 

    for j in range(1,len(D)):
        if j+k > len(D):
                j -= len(D)

        letters[ord(curr.pop(0))-97] -= 1
        curr.append(D[j+k-1])
        letters[ord(D[j+k-1])-97] += 1
        words[i] = tuple(letters)
        # print("curr", curr)
        # print("letters", stringify(letters))
        i += 1




#     Start of most likely

    freq = {}
    maxx = ("", 0)

    for el in words.values():
        if el not in freq.keys():
            freq[el] = 1
        else:
            freq[el] += 1


        # keep track of maximum
    for el in freq.keys():
        if freq[el] > maxx[1]:
                maxx = (el,freq[el])
        elif freq[el] == maxx[1]:
                pot = stringify(el)
                curr = stringify(maxx[0])
                for i in range(len(pot)):
                        if ord(pot[i]) == ord(curr[i]):
                                continue
                        elif ord(pot[i]) > ord(curr[i]):
                                break
                        elif ord(pot[i]) < ord(curr[i]):
                                maxx = (el,freq[el])
                                break

    return stringify(maxx[0])


def stringify(letters):

    word = ""

    for i in range (len(letters)):
        word += letters[i]*chr(i+97)

    return word