class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
      print(f"รหัส:{self.product_id} ชื่อ: {self.name} ราคา: {self.price} บาท" )

class FoodProduct(Product):
        def __init__(self, product_id, name, price, quantity, expiration_date):
            super().__init__(product_id, name, price, quantity)
            self.expiration_date = expiration_date

        def total_value(self):
            super().show_info()
            print(f"วันหมดอายุ: {self.expiration_date}")
            
class ElectronicsProduct(Product):
        def __init__(self, product_id, name, price, warranty_period):
            super().__init__(product_id, name, price)
            self.warranty_period = warranty_period
        def show_info(self):
            super().show_info()
            print(f"รับประกัน: {self.warranty_period} ปี")

product =[]
while True:
    print("\n Advanced Product Management System")
    print("1. เพิ่มสินค้า")
    print("2. เพิ่มสินค้าอิเล็กทรอนิกส์")
    print("2. แสดงสินค้าทั้งหมด")
    print("3. ลบสินค้า")
    print("4. ออกจากโปรแกรม")
    
    choice = input("เลือกเมนู  ")
    
    if choice == '1':
        pid = input("รหัสสินค้า: ")
        name = input("ชื่อสินค้า: ")
        price = float(input("ราคาสินค้า: "))
        exp = input("วันหมดอายุ (วว/ดด/ปปปป): ")
        product.append(FoodProduct(pid, name, price, exp))
        print("เพิ่มสินค้าอาหารเรียบร้อยแล้ว")
    
    elif choice == '2':
        pid = input("รหัสสินค้า: ")
        name = input("ชื่อสินค้า: ")
        price = float(input("ราคาสินค้า: "))
        warranty = int(input("ระยะเวลารับประกัน (ปี): "))
        product.append(ElectronicsProduct(pid, name, price, warranty))
        print("เพิ่มสินค้าอิเล็กทรอนิกส์เรียบร้อยแล้ว")
    
    elif choice == '3':
        if not product:
            print("ไม่มีสินค้าในระบบ")
        else:
            print("สินค้าทั้งหมด:")
            for idx, prod in enumerate(product):
                print(f"{idx + 1}. ", end="")
                prod.show_info()
            del_index = int(input("เลือกหมายเลขสินค้าที่ต้องการลบ: ")) - 1
            if 0 <= del_index < len(product):
                del product[del_index]
                print("ลบสินค้าสำเร็จ")
            else:
                print("หมายเลขสินค้าที่เลือกไม่ถูกต้อง")