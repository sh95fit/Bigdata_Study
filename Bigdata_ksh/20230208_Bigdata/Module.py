class myList(list) :
    def remove_all(self, value, /) :
        while value in self :   # myList로 생성된 인스턴스 자체를 받아와 self로 활용
            self.remove(value)