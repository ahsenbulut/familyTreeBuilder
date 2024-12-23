from graphviz import Digraph

class Node:
    def __init__(self, name, gender=None, bDate=None, married_with=None):
        self.name = name
        self.gender = gender
        self.bDate = bDate
        self.married_with = married_with
        self.children = []

    def add_child(self, child_node):
        """Bir node'u çocuk olarak ekleme metodu"""
        self.children.append(child_node)

    def remove_child(self, child_name):
        """Çocuk listesinden belirli bir node'u çıkarma metodu"""
        for child in self.children:
            if child.name == child_name:
                self.children.remove(child)
                print(f"{child_name} başarıyla silindi.")
                return
        print(f"{child_name} bulunamadı.")

    def print_info(self):
        """Bu node'un bilgilerini yazdırma metodu"""
        print(f"Name: {self.name}")
        print(f"Gender: {self.gender}")
        print(f"Birth Date: {self.bDate}")
        print(f"Married with: {self.married_with}\n")

    def find_node(self, name):
        """Ağaç içinde ismi verilen düğümü bulma metodu (Depth-First Search)"""
        if self.name == name:
            return self
        for child in self.children:
            result = child.find_node(name)
            if result:
                return result
        return None

    def visualize_tree(self, graph=None):
        """Ağacı görselleştirmek için Graphviz Digraph nesnesi oluşturur"""
        if graph is None:
            graph = Digraph(format='png')
            graph.attr(rankdir='TB', size='8,5')

        if self.gender or self.bDate:
            label = f"{self.name}\n{self.gender or ''}\n{self.bDate or ''}"
        else:
            label = f"{self.name}"

        graph.node(self.name, label=label)

        for child in self.children:
            graph.edge(self.name, child.name)
            child.visualize_tree(graph)

        return graph

    def __repr__(self, level=0):
        """Ağacı hiyerarşik şekilde yazdırma metodu"""
        ret = "\t" * level + repr(self.name) + "\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret

def display_menu():
    print("\n=== Aile Ağacı İşlemleri ===")
    print("1. Çocuk Ekle")
    print("2. Çocuk Sil")
    print("3. Ağaç Yapısını Görüntüle")
    print("4. Kişi Bilgilerini Görüntüle")
    print("5. Aile Ağacını Görselleştir")
    print("6. Çıkış")
    choice = input("Bir seçenek girin: ")
    return choice

def main():
    # Ağaç yapısını oluşturalım
    root = Node("Mehmet")

    while True:
        choice = display_menu()

        if choice == '1':  # Çocuk Ekle
            parent_name = input("Ebeveyn adını girin (örn. Mehmet): ")
            parent_node = root.find_node(parent_name)
            if parent_node:
                name = input("Çocuğun adı: ")
                gender = input("Cinsiyet: ")
                bDate = input("Doğum Tarihi: ")
                married_with = input("Evli Olduğu Kişi (varsa): ")
                child = Node(name, gender=gender, bDate=bDate, married_with=married_with)
                parent_node.add_child(child)
                print(f"{name} başarıyla {parent_name}'ye çocuk olarak eklendi.")
            else:
                print(f"{parent_name} bulunamadı.")

        elif choice == '2':  # Çocuk Sil
            parent_name = input("Ebeveyn adını girin (örn. Mehmet): ")
            child_name = input("Silinecek çocuğun adını girin: ")
            parent_node = root.find_node(parent_name)
            if parent_node:
                parent_node.remove_child(child_name)
            else:
                print(f"{parent_name} bulunamadı.")

        elif choice == '3':  # Ağaç Yapısını Görüntüle
            print("\nMevcut Ağaç Yapısı:\n")
            print(root)

        elif choice == '4':  # Kişi Bilgilerini Görüntüle
            person_name = input("Bilgilerini görmek istediğiniz kişinin adını girin: ")
            person_node = root.find_node(person_name)
            if person_node:
                person_node.print_info()
            else:
                print(f"{person_name} bulunamadı.")

        elif choice == '5':  # Aile Ağacını Görselleştir
            print("Aile ağacı görselleştiriliyor...\n")
            graph = root.visualize_tree()
            graph.render("family_tree", view=True)  # PNG dosyası oluşturulur ve görüntülenir

        elif choice == '6':  # Çıkış
            print("Çıkılıyor...")
            break

        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

main()
