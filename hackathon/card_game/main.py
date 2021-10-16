from game import Game
pplayer = Game()
def main():  # khó
    '''Khởi tạo trò chơi, hiển thị menu và thực thi các chức năng tương ứng'''
while (1==1):
    print("\nGame bài đếm nút")
    print("*************************MENU**************************")
    print("**  1. Thêm người chơi.                              **")
    print("**  2. Kiểm tra số người chơi.                       **")
    print("**  3. Xoá người chơi ID.                            **")
    print("**  4. Nghỉ thôi hết tiền                            **")
    print("*******************************************************")
    key = int(input("Nhập tuỳ chọn: "))
    if (key == 1):
        print("\n1. Thêm người chơi.")
        pplayer.setup()
        print("\nThêm người chơi thành công!")
    elif (key == 2):
        if (pplayer.soluongPlayer() > 0):
            print("\n7. Hiển thị danh sách player:")
            pplayer.list_players(pplayer.get_listPlayer())
        else:
            print("\nChưa có player nào")
    elif (key == 3):
        if (pplayer.soluongPlayer() > 0):
            print("\n3. Xoá player.")
            print("\nNhập ID: ")
            ID = int(input())
            if (pplayer.remove_player(ID)):
                print("\nPlayer có id = ", ID,  " Đã bị xoá.")
            else:
                print("\nPlayer có id = ", ID ," không tồn tại.")
        else:
            print("\nKhông có player nào!")
    elif (key == 4):
        print("\nNghỉ - hết tiền!")
        break
if __name__ == '__main__':
    main()
