# IMPLEMENTED BY RISHI KUMAR SONI , UTA ID: 1001774020
import Queries as qi

def main():
    # OPTIONS TO SELECT DIFFERENT OPTIONS...
    print("1. View Tables")
    print("2. Add new transaction : Member or Book or BorrowBook")
    print("3. Return a book!")
    print("4. Renew membership!")
    print("5. Generate weekly report!")
    print("6. Execute triggers!")
    val = int(input("Enter your option: "))
         
    if val==1:
        
        print("\n1. Book")
        print("2. Books Available in Library")
        print("3. Books Required")
        print("4. Library Member")
        print("5. Library Staff")
        print("6. Issue Book")
        print("\n")
        select = int(input("Select Table's to Display: "))
        if select==1:
            qi.display_book()
            print("\n")
            main()
        elif select==2:
            qi.display_books_available_in_lib()
            print("\n")
            main()
        elif select==3:
            qi.display_books_required()
            print("\n")
            main()
        elif select==4:
            qi.display_library_member()
            print("\n")
            main()
        elif select==5:
            qi.display_library_staff()
            print("\n")
            main()
        else:
            qi.display_issue_book()
            print("\n")
            main()
        
    elif val==2:
        print("\n1. Add new Member")
        print("2. Insert Book")
        print("3.Borrow Book")
        print("\n")
        select = int(input("Select to Insert Library Member Or Book Or Borrow a Book : "))
        if select==1:
            qi.insert_library_member()
            print("\n")
            main()
        elif select==2:
            qi.insert_book()
            print("\n")
            main()
        elif select==3:
            qi.borrow_book()
            print("\n")
            main()
    elif val==3:
        qi.return_book()
        print("\n")
        main()
    elif val==4:
        qi.renew_membership()
        print("\n")
        main()
    elif val==5:
        qi.weekly_report()
        print("\n")
        main()
    elif val==6:
        print("\n1.Notify a member about MemberShip renewal")
        print("2.Notify a member about outstanding overdue book")
        print("\n")
        select = int(input("Select from the above two options : "))
        if select==1:
            qi.trigger_membership_renewal()
            print("\n")
            main()
        elif select==2:
            qi.trigger_outstanding_overdue_book()
            print("\n")
            main() 

if __name__ == '__main__':
    qi.db_connection()
    main()        