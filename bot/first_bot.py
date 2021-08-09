# txt 내용 보여주기
def show():
    with open("ww.txt", "r", encoding="utf-8") as s:
        print(s.read())

# 이름 추가
def add_name(name):
    with open('ww.txt', 'r', encoding='utf-8') as d:
        d = d.read()
    with open("ww.txt", "a", encoding="utf-8") as f:
        if d == "":
            f.write(name)
        else:
            f.write('\n')
            f.write(name)

# 전체 삭제
def delete():
    with open("ww.txt", "w", encoding="utf-8"):
        pass

# 원하는 줄 삭제 (version1 . 정확한 이름 입력했을때만 삭제됨)  맨 앞에게 삭제됨
def remove_one_lie(remove_name):
    with open("ww.txt", "r", encoding="utf-8") as g:
        all_txt = g.read()
        splitted_txt = all_txt.split('\n')
        if remove_name in splitted_txt:
            splitted_txt.remove(remove_name)
        g = '\n'.join(splitted_txt)
    with open("ww.txt", "w", encoding="utf-8"):
        pass
    with open("ww.txt", "a", encoding="utf-8") as f:
        f.write(g)

# 원하는 줄 삭제 (version2. 비슷하게만 쳐도 삭제됨)

def remove_one_line2(remove_name2):
    with open('ww.txt', 'r', encoding='utf-8') as g:
        all_txt = g.read()
        splitted_txt = all_txt.split('\n')
        for x in range(len(splitted_txt)):
            if remove_name2 in splitted_txt[x]:
                del splitted_txt[x]
                break
        g = '\n'.join(splitted_txt)
        with open("ww.txt", "w", encoding="utf-8"):
            pass
        with open("ww.txt", "a", encoding="utf-8") as f:
            f.write(g)

delete()
add_name('aaaaa')
add_name('bbbb')
add_name('cㅁㄴㅇㄹ  ㅁㄴㅇㄹ ㄹㄹc')
#################### 문제점 #####################
# 맨 윗줄이 빈칸이 돼버림.(미리 ww.txt 만들어서 해결함)

### 추가하고 싶은거
# 서버로 넘어가게되면 ww.txt 파일이 아닌 다른걸로 해야될텐데 어케 대체 할지.



