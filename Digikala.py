from tkinter import messagebox
from tkinter import *

class AddProduct:
    count = 0
    price_sum = 0  # Class variable to store the total price of all items in the cart

    def __init__(self, name, price, file_path):
        self.name = name
        self.price = price
        AddProduct.count += 1

        # Create a product frame inside the frm_shop
        self.frm_product = Frame(frm_shop, bg="white", highlightthickness=1, highlightbackground="black")
        self.frm_product.grid(row=(AddProduct.count - 1) // 3, column=(AddProduct.count - 1) % 3, padx=10, pady=10)

        # Store PhotoImage to prevent garbage collection
        self.prod_img = PhotoImage(file=file_path)
        self.prod_img = self.prod_img.subsample(2, 2)
        lbl_prod_img = Label(self.frm_product, image=self.prod_img, bg="white")
        lbl_prod_img.grid(row=0, column=0)

        # Product information label
        self.prod_info = Label(self.frm_product, text=f"{name}\n${price}", bg="white")
        self.prod_info.grid(row=1, column=0)

        # Add to cart button
        self.btn_add = Button(self.frm_product, text="Add to Cart", command=lambda: self.add_to_cart(self.price, self.name))
        self.btn_add.grid(row=2, column=0)

    def add_to_cart(self, price, name):
        AddProduct.price_sum += price
        cart_items.append(name)  # Add item to cart
        update_total_price_label()  # Update the total price label

    @staticmethod
    def checkout():
        if AddProduct.price_sum > 0:
            messagebox.showinfo("shopping cart", f"Total price: ${AddProduct.price_sum}\nItems: {', '.join(cart_items)}",)
        else:
            messagebox.showinfo("Checkout", "Your cart is empty!")

def update_total_price_label():
    lbl_total_price.config(text=f"Total Price: ${AddProduct.price_sum}")

def open_shop():
    frm_digikala.pack_forget()
    btn_shop.place_forget()
    frm_shop.pack()

window = Tk()
window.config(bg="white")
window.title("Digikala")
window.geometry("850x550")
# window.resizable(width=False,height=False)
window.wm_iconbitmap("digikala.icon.ico")

# Create frames
frm_digikala = Frame(window)
frm_digikala.pack()

frm_shop = Frame(window, bg="white")  # Initialize frm_shop before using it in AddProduct

# Background image on the first frame
digi_img = PhotoImage(file="digikala.bg.png")
lbl_digi_img = Label(frm_digikala, image=digi_img)
lbl_digi_img.pack()

# Shop button
btn_shop = Button(text="Go to shop",font="Cambria", command=open_shop)
btn_shop.place(x=380,y=425)

# Add products
products = [
    AddProduct("Laptop", 1500, "laptap.png"),
    AddProduct("Phone", 800, "phone.png"),
    AddProduct("Headphones", 200, "headphone.png"),
    AddProduct("Tablet", 400, "tablet.png"),
    AddProduct("Camera", 600, "camera.png"),
    AddProduct("Ipad", 750, "ipad.png")
]

# Cart items list
cart_items = []

# Show total price
lbl_total_price = Label(frm_shop, text="Total Price: $0", bg="white")
lbl_total_price.grid(row=3, column=0, columnspan=3)

# Checkout button
btn_checkout = Button(frm_shop, text="Checkout", command=AddProduct.checkout)
btn_checkout.grid(row=4, column=0, columnspan=3, pady=10)

window.mainloop()