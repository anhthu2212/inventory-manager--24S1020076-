products = [] 
 
def add_product():
    # Nhập tên, giá, số lượng -> append vào products
    name = input("Nhập tên sản phẩm: ")
    price = int(input("Nhập giá sản phẩm: "))
    qty = int(input("Nhập số lượng tồn kho: "))

    product = {
        "name": name,
        "price": price,
        "qty": qty
    }

    products.append(product)
    print("Đã nhập hàng thành công.")
 
def view_inventory():
    if not products:
        print("Kho đang trống!")
        return

    print("\n--- DANH SÁCH SẢN PHẨM ---")
    for p in products:
        print(f"{p['name']} - Giá: {p['price']} - SL: {p['qty']}")

def check_low_stock(): 
    pass 
 
def main():     
    while True: 
        print("\n--- QUẢN LÝ KHO HÀNG ---") 
        print("1. Nhập hàng mới")         
        print("2. Xem tồn k")         
        print("3. Cảnh báo hh") 
        print("4. Thoát") 
         
        choice = input("Chọn cn: ") 
         
        if choice == '1':             
            add_product()         
            
        elif choice == '2':             
            view_inventory()         
        elif choice == '3': 
            check_low_stock()         
        elif choice == '4': 
            print("Kết thúc chương trình.")             
            break         
        else: 
            print("Lựa chọn không hợp lệ.") 
 
if __name__ == "__main__":     
    main()
