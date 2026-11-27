# --- Food truck stalls -----------------------------------------
stalls = [
    {"id": 1, "name": "Taco Tornado", "cuisine": "Mexican", "zone": "North", "queue": 22},
    {"id": 2, "name": "Ramen Rush", "cuisine": "Japanese", "zone": "East", "queue": 35},
    {"id": 3, "name": "Curry Carousel", "cuisine": "Indian", "zone": "West", "queue": 10},
    {"id": 4, "name": "Burger Byte", "cuisine": "American", "zone": "North", "queue": 28},
    {"id": 5, "name": "Green Garden Bowls", "cuisine": "Vegan", "zone": "East", "queue": 12},
    {"id": 6, "name": "Sweet Stack", "cuisine": "Desserts", "zone": "East", "queue": 40},
    {"id": 7, "name": "Mediterranean Mezze", "cuisine": "Mediterranean", "zone": "West", "queue": 8},
    {"id": 8, "name": "Spice Reactor", "cuisine": "Fusion", "zone": "North", "queue": 18},
]

# --- Menus (each row = one menu item for one stall) ------------
menus = [
    # Taco Tornado
    {"stall_id": 1, "item": "Beef Taco", "price": 4.0, "is_veg": False, "is_vegan": False, "spicy_level": 2},
    {"stall_id": 1, "item": "Veggie Taco", "price": 3.5, "is_veg": True, "is_vegan": True, "spicy_level": 1},
    {"stall_id": 1, "item": "Loaded Nachos", "price": 6.5, "is_veg": True, "is_vegan": False, "spicy_level": 3},
    {"stall_id": 1, "item": "Churros", "price": 3.0, "is_veg": True, "is_vegan": False, "spicy_level": 0},

    # Ramen Rush
    {"stall_id": 2, "item": "Shoyu Ramen", "price": 10.5, "is_veg": False, "is_vegan": False, "spicy_level": 2},
    {"stall_id": 2, "item": "Miso Ramen", "price": 11.0, "is_veg": True, "is_vegan": False, "spicy_level": 2},
    {"stall_id": 2, "item": "Spicy Tonkotsu", "price": 12.5, "is_veg": False, "is_vegan": False, "spicy_level": 4},
    {"stall_id": 2, "item": "Cold Matcha Tea", "price": 3.5, "is_veg": True, "is_vegan": True, "spicy_level": 0},

    # Curry Carousel
    {"stall_id": 3, "item": "Butter Chicken", "price": 11.0, "is_veg": False, "is_vegan": False, "spicy_level": 3},
    {"stall_id": 3, "item": "Chana Masala", "price": 8.5, "is_veg": True, "is_vegan": True, "spicy_level": 3},
    {"stall_id": 3, "item": "Garlic Naan", "price": 3.5, "is_veg": True, "is_vegan": False, "spicy_level": 0},
    {"stall_id": 3, "item": "Mango Lassi", "price": 4.5, "is_veg": True, "is_vegan": False, "spicy_level": 0},

    # Burger Byte
    {"stall_id": 4, "item": "Classic Burger", "price": 9.5, "is_veg": False, "is_vegan": False, "spicy_level": 1},
    {"stall_id": 4, "item": "Fries", "price": 3.5, "is_veg": True, "is_vegan": True, "spicy_level": 0},
    {"stall_id": 4, "item": "Double Cheese Burger", "price": 12.0, "is_veg": False, "is_vegan": False, "spicy_level": 1},
    {"stall_id": 4, "item": "Bean Burger", "price": 9.0, "is_veg": True, "is_vegan": False, "spicy_level": 1},

    # Green Garden Bowls
    {"stall_id": 5, "item": "Falafel Bowl", "price": 8.0, "is_veg": True, "is_vegan": True, "spicy_level": 1},
    {"stall_id": 5, "item": "Tofu Power Bowl", "price": 9.5, "is_veg": True, "is_vegan": True, "spicy_level": 2},
    {"stall_id": 5, "item": "Green Smoothie", "price": 5.0, "is_veg": True, "is_vegan": True, "spicy_level": 0},

    # Sweet Stack
    {"stall_id": 6, "item": "Pancake Stack", "price": 6.0, "is_veg": True, "is_vegan": False, "spicy_level": 0},
    {"stall_id": 6, "item": "Chocolate Waffles", "price": 6.5, "is_veg": True, "is_vegan": False, "spicy_level": 0},
    {"stall_id": 6, "item": "Strawberry Crepes", "price": 7.0, "is_veg": True, "is_vegan": False, "spicy_level": 0},
    {"stall_id": 6, "item": "Iced Latte", "price": 4.0, "is_veg": True, "is_vegan": False, "spicy_level": 0},

    # Mediterranean Mezze 
    {"stall_id": 7, "item": "Hummus Plate", "price": 7.5, "is_veg": True, "is_vegan": True, "spicy_level": 1},
    {"stall_id": 7, "item": "Chicken Shawarma", "price": 10.0, "is_veg": False, "is_vegan": False, "spicy_level": 2},
    {"stall_id": 7, "item": "Falafel Wrap", "price": 8.5, "is_veg": True, "is_vegan": True, "spicy_level": 1},

    # Spice Reactor
    {"stall_id": 8, "item": "Kimchi Tacos", "price": 9.5, "is_veg": False, "is_vegan": False, "spicy_level": 3},
    {"stall_id": 8, "item": "Paneer Bao", "price": 8.0, "is_veg": True, "is_vegan": False, "spicy_level": 2},
    {"stall_id": 8, "item": "Chili Fries", "price": 6.5, "is_veg": True, "is_vegan": True, "spicy_level": 3},
]

# --- Visitor preferences ----------------------------------------
visitors = [
    {
        "name": "Alice",
        "prefs": {
            "max_price": 9.0,
            "vegan_only": True,
            "avoid_spicy_above": 2,           
            "preferred_zones": ["East", "North"],
            "favorite_cuisines": ["Japanese", "Vegan"],
        },
    },
    {
        "name": "Ben",
        "prefs": {
            "max_price": 7.0,
            "vegan_only": False,
            "avoid_spicy_above": 3,
            "preferred_zones": ["North"],
            "favorite_cuisines": ["Mexican", "American"],
        },
    },
    {
        "name": "Chandra",
        "prefs": {
            "max_price": 12.0,
            "vegan_only": False,
            "avoid_spicy_above": 2,
            "preferred_zones": ["West", "East"],
            "favorite_cuisines": ["Indian"],
        },
    },
]

# --- Foot traffic per time slot and zone -----------------------
foot_traffic = [
    {"time": "12:00", "zone_counts": {"North": 160, "East": 200, "West": 90}},
    {"time": "13:00", "zone_counts": {"North": 180, "East": 260, "West": 110}},
    {"time": "14:00", "zone_counts": {"North": 140, "East": 300, "West": 95}},
]

# --- Actual orders made during the festival --------------------
orders = [
    {"order_id": 1, "stall_id": 5, "time": "12:00",
     "items": [
         {"item": "Falafel Bowl", "qty": 1},
         {"item": "Green Smoothie", "qty": 1},
     ]},

    {"order_id": 2, "stall_id": 2, "time": "12:00",
     "items": [
         {"item": "Shoyu Ramen", "qty": 1},
     ]},

    {"order_id": 3, "stall_id": 2, "time": "12:00",
     "items": [
         {"item": "Spicy Tonkotsu", "qty": 1},
         {"item": "Cold Matcha Tea", "qty": 1},
     ]},

    {"order_id": 4, "stall_id": 2, "time": "12:00",
     "items": [
         {"item": "Miso Ramen", "qty": 2},
     ]},

    {"order_id": 5, "stall_id": 2, "time": "12:00",
     "items": [
         {"item": "Cold Matcha Tea", "qty": 2},
     ]},

    {"order_id": 6, "stall_id": 6, "time": "12:00",
     "items": [
         {"item": "Pancake Stack", "qty": 2},
     ]},

    {"order_id": 7, "stall_id": 6, "time": "12:00",
     "items": [
         {"item": "Chocolate Waffles", "qty": 1},
         {"item": "Iced Latte", "qty": 1},
     ]},

    {"order_id": 8, "stall_id": 6, "time": "12:00",
     "items": [
         {"item": "Strawberry Crepes", "qty": 1},
     ]},

    {"order_id": 9, "stall_id": 5, "time": "12:00",
     "items": [
         {"item": "Tofu Power Bowl", "qty": 1},
     ]},

    {"order_id": 10, "stall_id": 4, "time": "12:00",
     "items": [
         {"item": "Classic Burger", "qty": 1},
         {"item": "Fries", "qty": 1},
     ]},

    {"order_id": 11, "stall_id": 4, "time": "12:00",
     "items": [
         {"item": "Bean Burger", "qty": 1},
     ]},

    {"order_id": 12, "stall_id": 1, "time": "12:00",
     "items": [
         {"item": "Beef Taco", "qty": 2},
     ]},

    {"order_id": 13, "stall_id": 1, "time": "12:00",
     "items": [
         {"item": "Veggie Taco", "qty": 1},
         {"item": "Churros", "qty": 1},
     ]},

    {"order_id": 14, "stall_id": 3, "time": "12:00",
     "items": [
         {"item": "Butter Chicken", "qty": 1},
         {"item": "Garlic Naan", "qty": 1},
     ]},

    {"order_id": 15, "stall_id": 7, "time": "12:00",
     "items": [
         {"item": "Hummus Plate", "qty": 1},
     ]},

    {"order_id": 16, "stall_id": 2, "time": "13:00",
     "items": [
         {"item": "Shoyu Ramen", "qty": 1},
         {"item": "Cold Matcha Tea", "qty": 1},
     ]},

    {"order_id": 17, "stall_id": 2, "time": "13:00",
     "items": [
         {"item": "Miso Ramen", "qty": 1},
     ]},

    {"order_id": 18, "stall_id": 2, "time": "13:00",
     "items": [
         {"item": "Spicy Tonkotsu", "qty": 2},
     ]},

    {"order_id": 19, "stall_id": 2, "time": "13:00",
     "items": [
         {"item": "Shoyu Ramen", "qty": 1},
         {"item": "Spicy Tonkotsu", "qty": 1},
     ]},

    {"order_id": 20, "stall_id": 5, "time": "13:00",
     "items": [
         {"item": "Falafel Bowl", "qty": 2},
     ]},

    {"order_id": 21, "stall_id": 5, "time": "13:00",
     "items": [
         {"item": "Green Smoothie", "qty": 2},
     ]},

    {"order_id": 22, "stall_id": 5, "time": "13:00",
     "items": [
         {"item": "Tofu Power Bowl", "qty": 1},
         {"item": "Green Smoothie", "qty": 1},
     ]},

    {"order_id": 23, "stall_id": 6, "time": "13:00",
     "items": [
         {"item": "Strawberry Crepes", "qty": 1},
         {"item": "Iced Latte", "qty": 1},
     ]},

    {"order_id": 24, "stall_id": 6, "time": "13:00",
     "items": [
         {"item": "Pancake Stack", "qty": 1},
     ]},

    {"order_id": 25, "stall_id": 4, "time": "13:00",
     "items": [
         {"item": "Double Cheese Burger", "qty": 1},
         {"item": "Fries", "qty": 2},
     ]},

    {"order_id": 26, "stall_id": 4, "time": "13:00",
     "items": [
         {"item": "Classic Burger", "qty": 1},
     ]},

    {"order_id": 27, "stall_id": 4, "time": "13:00",
     "items": [
         {"item": "Bean Burger", "qty": 1},
         {"item": "Fries", "qty": 1},
     ]},

    {"order_id": 28, "stall_id": 8, "time": "13:00",
     "items": [
         {"item": "Kimchi Tacos", "qty": 1},
         {"item": "Chili Fries", "qty": 1},
     ]},

    {"order_id": 29, "stall_id": 8, "time": "13:00",
     "items": [
         {"item": "Paneer Bao", "qty": 2},
     ]},

    {"order_id": 30, "stall_id": 8, "time": "13:00",
     "items": [
         {"item": "Kimchi Tacos", "qty": 1},
     ]},

    {"order_id": 31, "stall_id": 3, "time": "13:00",
     "items": [
         {"item": "Chana Masala", "qty": 1},
         {"item": "Garlic Naan", "qty": 1},
     ]},

    {"order_id": 32, "stall_id": 7, "time": "13:00",
     "items": [
         {"item": "Chicken Shawarma", "qty": 1},
     ]},

    {"order_id": 33, "stall_id": 7, "time": "13:00",
     "items": [
         {"item": "Falafel Wrap", "qty": 1},
         {"item": "Hummus Plate", "qty": 1},
     ]},

    {"order_id": 34, "stall_id": 1, "time": "14:00",
     "items": [
         {"item": "Beef Taco", "qty": 1},
         {"item": "Churros", "qty": 1},
     ]},

    {"order_id": 35, "stall_id": 1, "time": "14:00",
     "items": [
         {"item": "Veggie Taco", "qty": 2},
     ]},

    {"order_id": 36, "stall_id": 2, "time": "14:00",
     "items": [
         {"item": "Miso Ramen", "qty": 1},
         {"item": "Cold Matcha Tea", "qty": 1},
     ]},

    {"order_id": 37, "stall_id": 2, "time": "14:00",
     "items": [
         {"item": "Spicy Tonkotsu", "qty": 1},
     ]},

    {"order_id": 38, "stall_id": 3, "time": "14:00",
     "items": [
         {"item": "Butter Chicken", "qty": 1},
     ]},

    {"order_id": 39, "stall_id": 3, "time": "14:00",
     "items": [
         {"item": "Chana Masala", "qty": 1},
         {"item": "Mango Lassi", "qty": 1},
     ]},

    {"order_id": 40, "stall_id": 4, "time": "14:00",
     "items": [
         {"item": "Double Cheese Burger", "qty": 1},
     ]},

    {"order_id": 41, "stall_id": 4, "time": "14:00",
     "items": [
         {"item": "Classic Burger", "qty": 1},
         {"item": "Fries", "qty": 1},
     ]},

    {"order_id": 42, "stall_id": 5, "time": "14:00",
     "items": [
         {"item": "Falafel Bowl", "qty": 1},
         {"item": "Green Smoothie", "qty": 1},
     ]},

    {"order_id": 43, "stall_id": 5, "time": "14:00",
     "items": [
         {"item": "Tofu Power Bowl", "qty": 2},
     ]},

    {"order_id": 44, "stall_id": 5, "time": "14:00",
     "items": [
         {"item": "Green Smoothie", "qty": 2},
     ]},

    {"order_id": 45, "stall_id": 6, "time": "14:00",
     "items": [
         {"item": "Chocolate Waffles", "qty": 1},
         {"item": "Iced Latte", "qty": 1},
     ]},

    {"order_id": 46, "stall_id": 6, "time": "14:00",
     "items": [
         {"item": "Strawberry Crepes", "qty": 2},
     ]},

    {"order_id": 47, "stall_id": 7, "time": "14:00",
     "items": [
         {"item": "Chicken Shawarma", "qty": 1},
         {"item": "Falafel Wrap", "qty": 1},
     ]},

    {"order_id": 48, "stall_id": 7, "time": "14:00",
     "items": [
         {"item": "Hummus Plate", "qty": 1},
     ]},

    {"order_id": 49, "stall_id": 8, "time": "14:00",
     "items": [
         {"item": "Chili Fries", "qty": 2},
     ]},

    {"order_id": 50, "stall_id": 8, "time": "14:00",
     "items": [
         {"item": "Kimchi Tacos", "qty": 1},
         {"item": "Paneer Bao", "qty": 1},
     ]},
]