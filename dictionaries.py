# thisdict = {
# "water":"paani",
# "air":"hawa",
# "earth":"dharti",
# "fire":"aag",
# "anger":"gussa",
# }
# thisdict["laugh"]="hassi"
# thisdict.update({"love":"pyaar"})
# thisdict["love"] = "prem"
# for x in thisdict.items():
#     print(x)
# x = thisdict.keys()
# y = thisdict.values()
# print(x,"\n",y)
# if "love" in thisdict:
#     print("Yes, love is present in this dictionary")

# ----------------------------------------------------------------------------------------------------------

# numdict ={
#     "one":1,
#     "two":2,
#     "three":3,
#     "four":4,
#     "five":5,
#     "six":6,
# }
# li = []
# count=0
# for i in numdict:
#     li.append(numdict[i])
# print(li)
# for j in range(len(li)):
#     count=count+li[j]
# print(count)

# --------------------------------------------------------------------------------------------------------

# my_family = {

#     "child1" :{
#         "name" : "aradhya",
#         "year" : "2017"
#     },
#     "child2" :{
#         "name" : "alisha",
#         "year" : "2021"
#     },

# }
# print(my_family["child2"]["name"])

# x = ('key1','key2','key3')
# y = 0
# thisdict = dict.fromkeys(x,y)
# print(thisdict)

# ------------------------------------------------------------------------------------------------------

# samdict = {0: 10, 1: 20}
# samdict.update({2:30})
# print(samdict)

# ------------------------------------------------------------------------------------------------------
# numdict ={
#     "one":1,
#     "two":2,
#     "three":3,
#     "four":4,
#     "five":5,
#     "six":6,
#     "zero":0,
# }
# print(sorted(numdict.values()))
# li = []
# count=0
# for i in numdict:
#     li.append(numdict[i])
# print(li)

# for j in range(len(li)):

# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# alldict={}
# for i in (dic1, dic2, dic3):
#     alldict.update(i)
# print(alldict)


# dic = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 70, 8: 80, 9: 90, 10: 100}
# dict = {}
# for i in range(1,11):
#     dic.update({i:i*10})

# x=dic.values()

# for i in dic:
#     if dic[i]>60:
#         dic.update({i:0})

# print(dic)
        
# n = int(input("enter a random number : "))
# dict = {}
# for i in range(1,n+1):
#     dict.update({i:i*i})

# print(dict)

# dic= {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
# a=0
# for i in dic:

#     print(i ,"keys" , dic[i] ,'values' ,"index",a)
#     a+=1

#---------------------------------------------------------------------------------------------------------------
# {'red': '#FF0000', 'green': '#008000', 'blue': '#0000FF'}
# keys = ['red', 'green', 'blue']
# values = ['#FF0000','#008000', '#0000FF']
# # mydict = dict(zip(keys, values))
# dic = {}
# for i in range(len(keys)):
#     dic[values[i]] = keys[i]
# print(dic)
# print(mydict)
#---------------------------------------------------------------------------------------------------------
#                                    (how to find sum using loop)
# dic= {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
# total = 0
# for i in dic:
#     total += dic[i]
#     print(dic[i])
# print("The sum of all the values is : ", total)

#------------------------------------------------------------------------------------------------------

# dic= {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
# print(max(dic.value()))
# print(min(dic.keys()))

# dic = {1 :"dic"}
# if dic == {}:
#     print('the dictionary is empty')
# else:
#     print('the dictionary is not empty')

# dic = {1: "one", 2: "two", 3: "three", 1 : "one"}
# uni = []
# dup = []
# for i in dic:
#     if i in uni:
#         uni.append(i)
#     elif i in dup:
#         dup.append(i)
# print(uni)

# ----------------------------------------------------------------------
