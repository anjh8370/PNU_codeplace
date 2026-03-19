# [1] 5번
### 채점 결과
Accepted
### 제출 일자
2026년 03월 19일 14:12:25
### 성능 요약[추후 구현 예정]
- 메모리: N/A KB
- 시간: N/A ms
---
### 문제 링크
https://code.pusan.ac.kr/problem/1
### 난이도
보통
### 문제 설명
You are given two non-empty lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a list.You may assume the two numbers do not contain any leading zero, except the number 0 itself.Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
### 입력
주어진 두 리스트l1과 l2는0 이상 9 이하의 숫자들이 각각 1개 이상 들어있는 리스트이다.
### 출력
문제의 답을 0 이상 9 이하의 숫자들로 이루어진 리스트로 리턴한다.
### 예제 입력/출력
**예제 입력 1**
```
Input: l1 = [0], l2 = [0]
```
**예제 출력 1**
```
Output: [0]
```
**예제 입력 2**
```
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
```
**예제 출력 2**
```
Output: [8,9,9,9,0,0,0,1]
```
### 제약 사항
- 시간 제한   1000ms
- 메모리 제한   256mb