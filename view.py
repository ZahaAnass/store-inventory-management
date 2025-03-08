import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import database

class GestionInventaire:
    def __init__(self, window):
        self.window = window
        self.window.title("Gestion d'Inventaire pour une Petite Boutique")
        self.window.geometry("1920x1080")
        self.window.resizable(False, False)

        # Les zone de recherche

        # Zone recherche par nom
        self.search_frame = LabelFrame(window, text="zone de recherche", font=("Arial", 12, "bold"), labelanchor="n")
        self.search_frame.pack(fill="x", expand="yes", padx=20)
        self.label_search = Label(self.search_frame, text="Rechercher par nom du produit:", font=("Arial", 12, "bold"))
        self.label_search.grid(row=0, column=0, padx=10, pady=10)
        self.search_entry = Entry(self.search_frame, width=150)
        self.search_entry.grid(row=0, column=1, padx=10, pady=10)
        self.search_button = Button(self.search_frame, text="Rechercher", command=self.rechercher_produit, width=30)
        self.search_button.grid(row=0, column=2, padx=10, pady=10)

        # Zone filtrage par category
        self.label_filter = Label(self.search_frame, text="Filtrer par category:", font=("Arial", 12, "bold"))
        self.label_filter.grid(row=1, column=0, padx=10, pady=10)
        self.filter_entry = Entry(self.search_frame, width=150)
        self.filter_entry.grid(row=1, column=1, padx=10, pady=10)
        self.filter_button = Button(self.search_frame, text="Filtrer", command=self.filtrer_produits, width=30)
        self.filter_button.grid(row=1, column=2, padx=10, pady=10)

        # Tableau des produits
        self.tree_frame = Frame(window)
        self.tree_frame.pack(pady=10)
        self.tree_scrool = Scrollbar(self.tree_frame)
        self.tree_scrool.pack(pady=10, side=RIGHT, fill=Y)
        self.my_tree = ttk.Treeview(self.tree_frame, yscrollcommand=self.tree_scrool.set, selectmode="extended", height=20)
        self.my_tree.pack(fill="x", expand=True)
        self.my_tree['columns'] = ("nom_produit", "refernce", "category", "quantity", "prix_unitaire")
        self.my_tree.column("#0", width=0, stretch=False)
        self.my_tree.column("nom_produit", anchor="w", width=365, minwidth=150)
        self.my_tree.column("refernce", anchor="w", width=365, minwidth=150)
        self.my_tree.column("category", anchor="w", width=365, minwidth=150)
        self.my_tree.column("quantity", anchor="w", width=365, minwidth=150)
        self.my_tree.column("prix_unitaire", anchor="w", width=365, minwidth=150)
        
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("Treeview",
                            background="#7c7c7d",
                            foreground="black",
                            rowheight=25,
                            fieldbackground="#7c7c7d")
        self.style.map('Treeview', background=[('selected', '#0e43e3')])

        self.my_tree.heading('#0', text='', anchor='w')
        self.my_tree.heading("nom_produit", text="Nom Produit", anchor="w")
        self.my_tree.heading("refernce", text="Référence", anchor="w")
        self.my_tree.heading("category", text="Catégorie", anchor="w")
        self.my_tree.heading("quantity", text="Quantité", anchor="w")
        self.my_tree.heading("prix_unitaire", text="Prix Unitaire", anchor="w")
        self.my_tree.pack(fill="both", expand=True)

        # # Grid Frame
        # self.grid_frame = Frame(window)
        # self.grid_frame.grid(row=1, column=0, padx=20, pady=10, columnspan=3, sticky="ew")

        # self.grid_frame.columnconfigure(0, weight=1)
        # self.grid_frame.columnconfigure(1, weight=2)
        # self.grid_frame.columnconfigure(2, weight=1)

        # Buttons
        self.button_frame = LabelFrame(window, text="Commandes")
        self.button_frame.pack(fill="x", expand="yes", padx=45)
        self.ajouter_button = Button(self.button_frame, text="Ajouter Produit", command=self.ajouter_produits)
        self.ajouter_button.grid(row=0, column=0, padx=20, pady=10)
        self.modifier_button = Button(self.button_frame, text="Modifier Produit", command=self.modifier_produits)
        self.modifier_button.grid(row=0, column=1, padx=20, pady=10)
        self.supprimer_button = Button(self.button_frame, text="Supprimer Produit", command=self.supprimer_produits)
        self.supprimer_button.grid(row=0, column=2, padx=20, pady=10)
        self.calcul_button = Button(self.button_frame, text="Calculer le résumé", command=self.calculer_resumer)
        self.calcul_button.grid(row=0, column=3, padx=20, pady=10) 
        self.view_product = Button(self.button_frame, text="Afficher tout les produits", command=self.load_products)
        self.view_product.grid(row=0, column=4, padx=20, pady=10)
        self.export_button = Button(self.button_frame, text="Exporter les produits", command=self.export_products)
        self.export_button.grid(row=0, column=5, padx=20, pady=10)

        # Load products
        self.load_products()
    # export products sous fichier csv
    def export_products(self):
        products = database.show_products()
        with open("products.csv", "w") as file:
            file.write("Nom Produit, Référence, Catégorie, Quantité, Prix Unitaire\n")
            for product in products:
                file.write(f"{product[0]}, {product[1]}, {product[2]}, {product[3]}, {product[4]}\n")
        messagebox.showinfo("Succès", "Produits exportés avec succès)")

    def rechercher_produit(self):
        produit = database.get_product(self.search_entry.get())
        if produit:
            self.my_tree.delete(*self.my_tree.get_children())
            self.my_tree.insert("", "end", values=produit)
            self.search_entry.delete(0, END)
        else:    
            messagebox.showwarning("Erreur", "Produit non trouvé")

    def filtrer_produits(self):
        self.my_tree.delete(*self.my_tree.get_children())
        produits = database.get_product_by_category(self.filter_entry.get())
        for produit in produits:
            self.my_tree.insert("", "end", values=produit)
        if not produits:
            self.load_products()
            messagebox.showwarning("Erreur", "Category non trouver")

    def load_products(self):
        self.my_tree.delete(*self.my_tree.get_children())
        products = database.show_products()
        for product in products:
            self.my_tree.insert("", "end", values=product)

    def calculer_resumer(self):
        products = database.show_products()
        quantity_total = 0
        prix_total = 0
        for product in products:
            quantity_total += product[3]
            prix_total += product[3] * product[4]
        messagebox.showinfo("Résumé", f'La quantité totale: {quantity_total}\nLe prix total: {prix_total}')

    def ajouter_produits(self):
        self.window_product("Ajouter un produit")

    def supprimer_produits(self):
        selected_item = self.my_tree.selection()
        if not selected_item:    
            messagebox.showwarning("Erreur", "Veuillez sélectionner un produit à supprimer")
            return
        def valider():
            item = self.my_tree.item(selected_item[0])
            database.suprimer_produit(item['values'][0])
            self.load_products()
            messagebox.showinfo("Succès", "Produit supprimé avec succès")
            new_window.destroy()

        def annuler():
            new_window.destroy()
            messagebox.showinfo("Succès", "Produit n'est pas supprimer")

        new_window = Toplevel(self.window)
        new_window.title("Supprimer un produit")
        new_window.geometry("300x80")
        new_window.resizable(False, False)
        button_valider = tk.Button(new_window, text="Valider", command=valider)
        button_valider.grid(row=0, column=0, pady=20, padx=50)
        button_annuler = tk.Button(new_window, text="Annuler", command=annuler)
        button_annuler.grid(row=0, column=1)

    def modifier_produits(self):
        selected_item = self.my_tree.selection()
        if not selected_item:
            messagebox.showwarning("Erreur", "Veuillez sélectionner un produit à modifier")
            return
        item = self.my_tree.item(selected_item[0])
        self.window_product("Modifier un produit", item['values'])

    def window_product(self, title, product=None):
        new_window = Toplevel(self.window)
        new_window.title(title)
        new_window.geometry("400x400")
        new_window.resizable(False, False)

        tk.Label(new_window, text="Nom du produit:").pack()
        product_name = Entry(new_window)
        product_name.pack()
        tk.Label(new_window, text="Référence:").pack()
        product_reference = Entry(new_window)
        product_reference.pack()
        tk.Label(new_window, text="Catégorie:").pack()
        product_category = Entry(new_window)
        product_category.pack()
        tk.Label(new_window, text="Quantité:").pack()
        product_quantity = Entry(new_window)
        product_quantity.pack()
        tk.Label(new_window, text="Prix unitaire:").pack()
        product_price = Entry(new_window)
        product_price.pack()

        if product is not None:
            product_name.insert(0, product[0])
            product_reference.insert(0, product[1])
            product_category.insert(0, product[2])
            product_quantity.insert(0, product[3])
            product_price.insert(0, product[4])

        def valider():
            if product:
                database.modifier_produit(
                    product_name.get(),
                    product_reference.get(),
                    product_category.get(),
                    int(product_quantity.get()),
                    float(product_price.get())
                )
            else:
                database.ajouter_produits(
                    product_name.get(),
                    product_reference.get(),
                    product_category.get(),
                    int(product_quantity.get()),
                    float(product_price.get())
                )
            self.load_products()
            new_window.destroy()
            messagebox.showinfo("Succès", "Produit ajouté avec succès")    

        button_valider = tk.Button(new_window, text="Valider", command=valider)
        button_valider.pack()
            