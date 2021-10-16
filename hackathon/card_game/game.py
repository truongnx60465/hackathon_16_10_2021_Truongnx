from player import Player
class Game:
    '''
    Class chứa các chức năng chính của game

    Game chứa danh sách người chơi, và bộ bài
    '''
    listPlayer = []
    def __init__(self):
        pass
    def generateID(self):
            maxId = 1
            if (self.soluongPlayer() > 0):
                maxId = self.listPlayer[0]._id
                for numberPlayer in self.listPlayer:
                    if (maxId < numberPlayer._id):
                        maxId = numberPlayer._id
                maxId = maxId + 1
            return maxId

    def soluongPlayer(self):
        return self.listPlayer.__len__()

    def setup(self):
        '''Khởi tạo trò chơi, nhập số lượng và lưu thông tin người chơi'''
        numberPlayerID = self.generateID()
        name = input("Nhập tên người chơi : ")
        pr = Player(numberPlayerID, name)
        self.listPlayer.append(pr)

    def guide(self):
        '''Hiển thị menu chức năng/hướng dẫn chơi'''
        pass

    def list_players(self, listPlayer):
        if (listPlayer.__len__() > 0):
            for ppl in listPlayer:
                print(ppl._id,ppl._name)

    def get_listPlayer(self):
        return self.listPlayer

    def add_player(self):
        '''Thêm một người chơi mới'''
        pass

    def findByID(self, ID):
        searchResult = None
        if (self.soluongPlayer() > 0):
            for ppl in self.listPlayer:
                if (ppl._id == ID):
                    searchResult = ppl
        return searchResult

    def remove_player(self, ID):
        '''
        Loại một người chơi
        Mỗi người chơi có một ID (có thể lấy theo index trong list)
        '''
        isDeleted = False
        pr = self.findByID(ID)
        if (pr != None):
            self.listPlayer.remove(pr)
            isDeleted = True
        return isDeleted

    def deal_card(self):
        '''Chia bài cho người chơi'''
        pass

    def flip_card(self):
        '''Lật bài tất cả người chơi, thông báo người chiến thắng'''
        pass
    