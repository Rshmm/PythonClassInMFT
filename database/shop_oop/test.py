from database.shop_oop.model import ProductModel
from database.shop_oop.controller import ProductController

# add
# p1 = ProductModel("iphone 12 ", 'apple', 800)
# p2 = ProductModel("a01", 'samsung', 400)
# p3 = ProductModel("iphone 13 ", 'apple', 900)
# p4 = ProductModel("iphone 14 ", 'apple', 1000)
# p5 = ProductModel("a56", 'samsung', 560)
# p6 = ProductModel("s25 ultra", 'samsung', 1500)
# p1.save()
# p2.save()
# p3.save()
# p4.save()
# p5.save()
# p6.save()

# remove
controller = ProductController()

# ProductModel.remove_product(17)
# حذف محصول
success, msg = controller.remove_product(31)
print(success, msg)
# انتظار:
# True, "Product 1 deleted successfully"


#
# # edit
# print(ProductController.edit_product(22,"aaaaa", "bdd", "12000"))
# print(ProductController.edit_product(45,"aaaaa", "bdd", "13000"))
# ProductModel.edit_products(15,"s25 ultra","samsung", 2200)