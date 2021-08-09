# txt 내용 보여주기
class kakaotalk_bot():
    def __init__(self):
        pass

    def show(self):
        with open("gg.txt", "r", encoding="utf-8") as s:
            print(s.read())

    # 이름 추가
    def add_name(self, name):
        self.name = name
        with open('gg.txt', 'r', encoding='utf-8') as d:
            d = d.read()
        with open("gg.txt", "a", encoding="utf-8") as f:
            if d == "":
                f.write(self.name)
            else:
                f.write('\n')
                f.write(self.name)

        with open("gg.txt", "r", encoding="utf-8") as d:
            print(d.read())

    # 줄 삭제
    def delete(self):
        with open("gg.txt", "w", encoding="utf-8"):
            pass

    # 원하는 줄 삭제 (version1 . 정확한 이름 입력했을때만 삭제됨)  맨 앞에게 삭제됨
    def remove_one_lie(self, remove_name):
        self.remove_name = remove_name
        with open("gg.txt", "r", encoding="utf-8") as g:
            all_txt = g.read()
            splitted_txt = all_txt.split('\n')
            if self.remove_name in splitted_txt:
                splitted_txt.remove(self.remove_name)
            g = '\n'.join(splitted_txt)
        with open("gg.txt", "w", encoding="utf-8"):
            pass
        with open("gg.txt", "a", encoding="utf-8") as f:
            f.write(g)

    # 원하는 줄 삭제 (version2. 비슷하게만 쳐도 삭제됨)

    def remove_one_line2(self, remove_name2):
        self.remove_name2 = remove_name2
        with open('gg.txt', 'r', encoding='utf-8') as g:
            all_txt = g.read()
            splitted_txt = all_txt.split('\n')
            for x in range(len(splitted_txt)):
                if self.remove_name2 in splitted_txt[x]:
                    del splitted_txt[x]
                    break
            g = '\n'.join(splitted_txt)
            with open("gg.txt", "w", encoding="utf-8"):
                pass
            with open("gg.txt", "a", encoding="utf-8") as f:
                f.write(g)

num_1 = kakaotalk_bot()

num_1.add_name('KIM SEOUNG HEE')
