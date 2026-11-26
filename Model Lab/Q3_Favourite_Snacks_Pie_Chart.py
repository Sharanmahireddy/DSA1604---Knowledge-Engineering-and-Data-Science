import matplotlib.pyplot as plt

snacks = ["Samosa", "Puff", "Sandwich", "Vada",
          "Noodles", "Burger", "Fruit Bowl"]
students = [9, 6, 8, 5, 10, 7, 5]

plt.pie(students, labels=snacks, autopct="%1.1f%%", startangle=90)
plt.title("Favourite Evening Snacks (50 Students)")
plt.axis("equal")
plt.show()
