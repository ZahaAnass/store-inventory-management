import sqlite3

def create_table():
    conn = sqlite3.connect("inventaire.db")
    cursor = conn.cursor()
    cursor.execute("""create table if not exists products (
        nom_produit text primary key,
        refernce text unique not null,
        category text not null,
        quantity integer not null,
        prix_unitaire real not null
    )""")
    conn.commit()
    conn.close()

def get_product(nom_produit):
    conn = sqlite3.connect("inventaire.db")
    cursor = conn.cursor()
    cursor.execute("select * from products where nom_produit=?", (nom_produit,))
    product = cursor.fetchone()
    conn.close()
    return product

def get_product_by_category(category):
    conn = sqlite3.connect("inventaire.db")
    cursor = conn.cursor()
    cursor.execute("select * from products where category=?", (category,))
    products = cursor.fetchall()
    conn.close()
    return products

def ajouter_produits(nom_produit, refernce, category, quantity, prix_unitaire):
    conn = sqlite3.connect("inventaire.db")
    cursor = conn.cursor()
    cursor.execute("insert into products (nom_produit, refernce, category, quantity, prix_unitaire) values (?, ?, ?, ?, ?)",
                    (nom_produit, refernce, category, quantity, prix_unitaire))
    conn.commit()
    conn.close()

def modifier_produit(nom_produit, refernce, category, quantity, prix_unitaire):
    conn = sqlite3.connect("inventaire.db")
    cursor = conn.cursor()
    cursor.execute("""
        update products set refernce=?, category=?, quantity=?, prix_unitaire=? where nom_produit=?"""
        , (refernce, category, quantity, prix_unitaire, nom_produit))
    conn.commit()
    conn.close()

def suprimer_produit(nom_produit):
    conn = sqlite3.connect("inventaire.db")
    cursor = conn.cursor()
    cursor.execute("delete from products where nom_produit=?", (nom_produit,))
    conn.commit()
    conn.close()

def show_products():
    conn = sqlite3.connect("inventaire.db")
    cursor = conn.cursor()
    cursor.execute("select * from products")
    products = cursor.fetchall()
    conn.close()
    return products

def sort_products(clicked, order):
    conn = sqlite3.connect("inventaire.db")
    cursor = conn.cursor()
    cursor.execute(f"select * from products order by {clicked} {order}")
    products = cursor.fetchall()
    conn.close()
    return products
