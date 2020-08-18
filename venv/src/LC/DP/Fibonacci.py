class Fibonacci():

    # 问题描述：一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共需要多少种跳法。
    def fibFrog(self, n):
        if n<=0:
            return 0
        elif n==1:
            return 1
        elif n==2:
            return 2
        else:
            return (self.fib(n-1)+self.fib(n-2))

    # 问题描述：求Fibonacci数列的第n个数值是什么。
    def fib(self,n):
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            return self.fib(n-1)+self.fib(n-2)

    # 问题描述： 在一定时间内包含多个工作任务，每一个工作任务有开始时间和结束时间，并且工人完成每个任务都会得到对应的奖金，一个人在同一时刻只能工作。
f=Fibonacci()
print(f.fibFrog(5))
print(f.fib(6))
