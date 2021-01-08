>>> import collections
>>> a = [1,2,3,3,5,6,7,5,3,4,5,6,7,3,6,3,6,4,6,4,6,4,8,9,6,7,8,6,8,6,8,6,8,6,86,5,7,6,4,5,6,5,6,5,6,4,3,5,6,7,8,6,7,8,63,3,2,4,3,5,6,5,4,5,4,3,4,5,4,3,5,1,5,7,9,7]
>>> ctr = collections.Counter(a)
>>> print("Frequency of the elements in the List:",ctr)
Frequency of the elements in the List: Counter({6: 18, 5: 14, 4: 11, 3: 10, 7: 8, 8: 7, 1: 2, 2: 2, 9: 2, 86: 1, 63: 1})
>>> thisdict = {
	1:ctr[1],
	2:ctr[2],
	3:ctr[3],
	4:ctr[4],
	5:ctr[5]
}
>>> print(thisdict)
{1: 2, 2: 2, 3: 10, 4: 11, 5: 14}
>>> 
