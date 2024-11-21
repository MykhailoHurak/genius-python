class Journal:
    def __init__(self) -> None:
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self, position):
        del self.entries[position]

    def __str__(self) -> str:
        return "\n". join(self.entries)
    
journal_01 = Journal()

journal_01.add_entry("kettlebell workout 30min")
journal_01.add_entry("yoga 30min")
journal_01.add_entry("run 10km")

print(f"Count of entries:\n{journal_01}")

print(journal_01.entries)
print(journal_01.count)