class Underscore(object):
    def map(self, arr, func):
        for i in xrange(len(arr)):
            arr[i] = func(arr[i])
        return arr

    def reduce(self, arr, func, memo=None):
        if len(arr) == 1:
            return arr[0]
        elif len(arr) < 2:
            return arr
        if memo == None:
            pass
        else:
            arr.insert(0,memo)
        temp = func(arr[0],arr[1])
        for j in xrange(2,len(arr)):
            temp = func(temp,arr[j])
        return temp

    def find(self, arr, func):
        for i in xrange(len(arr)):
            if func(arr[i]):
                return arr[i]
        return None

    def filter(self, arr, func):
        temparr = []
        for i in xrange(len(arr)):
            if func(arr[i]):
                temparr.append(arr[i])
        return temparr

    def reject(self, arr, func):
        temparr = []
        for i in xrange(len(arr)):
            if func(arr[i]) != True:
                temparr.append(arr[i])
        return temparr

_ = Underscore()

print _.map([1,2,3,4],lambda x: x ** 2)
print _.find([1,2,3,4],lambda x: x % 3 == 0)
print _.filter([1,2,3,4,5,6,7,8,9,10],lambda x: x % 3 == 0)
print _.reject([1,2,3,4,5,6,7,8,9,10],lambda x: x % 3 == 0)
print _.reduce([3,4,5,6],lambda x, y: x*y, 1)
print _.reduce([],lambda x, y: x*y, 1)
print _.reduce([3],lambda x, y: x*y, 1)
