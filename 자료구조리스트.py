# -*- coding: utf-8 -*-
list = [] #리스트 선언

#리스트에 값을 입력
list.append(11)
list.append(11)
list.append(22)
list.append(22)
list.append(33)

for x in range(0, len(list)):
    if list[x] == 22:
        print "22의 인덱스 : ", x
#22를 찾는 반복문

#리스트의 길이 출력
print len(list)
#리스트의 내용물 출력
print list

#22를 삭제하는 반복문
for x in range(0, len(list)):
    if list.count(22): #조건문으로 22일 경우
        list.remove(22) #22를 삭제하는 메소드
        
print len(list)
print list