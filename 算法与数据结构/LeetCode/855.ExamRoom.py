'''
855. Exam Room - Medium

In an exam room, there are N seats in a single row, numbered 0, 1, 2, ..., N-1.
When a student enters the room, 
they must sit in the seat that maximizes the distance to the closest person.  
If there are multiple such seats, they sit in the seat with the lowest number.  
(Also, if no one is in the room, then the student sits at seat number 0.)

Return a class ExamRoom(int N) that exposes two functions: 
ExamRoom.seat() returning an int representing what seat the student sat in, and ExamRoom.
leave(int p) representing that the student in seat number p now leaves the room.  
It is guaranteed that any calls to ExamRoom.leave(p) have a student sitting in seat p.

Example 1:

Input: 
["ExamRoom","seat","seat","seat","seat","leave","seat"], [[10],[],[],[],[],[4],[]]
Output: [null,0,9,4,2,null,5]
Explanation:
ExamRoom(10) -> null
seat() -> 0, no one is in the room, then the student sits at seat number 0.
seat() -> 9, the student sits at the last seat number 9.
seat() -> 4, the student sits at the last seat number 4.
seat() -> 2, the student sits at the last seat number 2.
leave(4) -> null
seat() -> 5, the student sits at the last seat number 5.
​​​​​​​

Note:

1 <= N <= 10^9
ExamRoom.seat() and ExamRoom.leave() will be called at most 10^4 times across all test cases.
Calls to ExamRoom.leave(p) are guaranteed to have a student currently sitting in seat number p.
'''


import bisect
class OfficialAnswerExamRoom:

    def __init__(self, N: int):
        self.students = []
        self.seats = N

    def seat(self) -> int:
        # 如果至少有一个学生，那么开始计算该坐哪
        if self.students:
            # dist从第一个学生开始
            # student就是将要返回的学生的座位号，从第一个学生开始
            dist, student = self.students[0], 0
            # 同时遍历self.students的所有元素及其下标
            for i, s in enumerate(self.students):
                # 除了第一个元素，也就是从第二个学生开始运行循环
                # 枚举不能切片，所以用这种方法
                if i:
                    # 前一个学生是第i-1个元素
                    prev = self.students[i - 1]
                    # 距离d是当前第i个学生的座位号s与前一个学生的座位号prev的中位数（取整）
                    d = (s - prev) // 2
                    # 如果距离d比dist大，那么就更新dist和student为与d相关的值
                    if d > dist:
                        dist, student = d, prev + d
            d = self.seats - 1 - self.students[-1]
            if d > dist:
                student = self.seats - 1
        # 如果没有学生，那么就让第一个学生坐0号
        else:
            student = 0
        # bisect.insort其实是默认使用insort_right，也就是从右往左数，然后插入
        # 这道题无所谓插入顺序，只要保证插入后有序即可
        bisect.insort(self.students, student)
        return student
        

    def leave(self, p: int) -> None:
        self.students.remove(p)
        


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)