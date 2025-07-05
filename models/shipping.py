class ShippingService:
    def ship(self, items):
        print("** Shipment notice **")
        total_weight = 0
        item_counts = {}
        for item in items:
            key = (item.get_name(), item.get_weight())
            item_counts[key] = item_counts.get(key, 0) + 1
            total_weight += item.get_weight()
        for (name, weight), count in item_counts.items():
            print(f"{count}x {name}\t{weight}g")
        print(f"Total package weight {total_weight/1000:.1f}kg\n")
