class Sort:

    # This simple sorting algorithm iterates over a list,
    # comparing elements in pairs and swapping them until the larger elements "bubble up" to the end of the list,
    # and the smaller elements stay at the "bottom".
    def bubbleSort(self,nums):
        swapped=True
        l=len(nums)
        while swapped:
            swapped=False
            for i in range(l-1):
                j=i+1
                if nums[i]>nums[j]:
                    nums[i],nums[j]=nums[j],nums[i] # Swap
                    swapped=True

    def mergeSort(self,nums):
        print(nums)

    def insertionSort(self,nums):
        print(nums)

    def shellSort(self,nums):
        print(nums)

    def selectionSort(self,nums):
        print(nums)

######Quick Sort#############################################
    def partition(self, nums, low, high):
        border=low
        pivot=nums[high]
        for i in range(low,high+1):
            if nums[i]<pivot:
                border+=1
                nums[border],nums[i]=nums[i],nums[border]
        nums[border],nums[low]=nums[low],nums[border]
        return border


    def quickSort2(self,nums,low,high):
        if low<high:
            p=self.partition(nums,low,high)
            self.quickSort2(nums,low,p-1)
            self.quickSort2(nums,p+1,high)


    def quickSort(self,nums):
        if len(nums)<=1: return nums
        smaller,equal,larger=[],[],[]
        pivot=nums[len(nums)-1]

        for num in nums:
            if num<pivot: smaller.append(num)
            elif num==pivot: equal.append(num)
            else: larger.append(num)
        return self.quickSort(smaller)+equal+self.quickSort(larger)

# nums=[5,6,4,3,8,9,2,7,1,0]
# s=Sort()
# s.bubbleSort(nums)
# print(nums)
nums=[9,-3,5,2,6,8,-6,1,3]
s=Sort()
print(s.quickSort(nums))